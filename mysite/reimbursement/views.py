from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login 
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.utils import simplejson

from reimbursement.forms import *
from reimbursement.models import *


def index(request):
    context = {}
    form = LoginForm() # An unbound form

    return render(request, 'index.html', {'form': form})

def login(request):
    if request.method == 'POST': # If the form has been submitted...
        form = LoginForm(request.POST) # A form bound to the POST data
        username = request.POST['email'].split('@')[0]
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print username, password
        print user
        if user is not None:
            # the password verified for the user
            if user.is_active:
                auth_login(request, user)
                #request.session['user_id']=user.id
                return redirect('home_individual')
            else:
                return HttpResponse("The password is valid, but the account has been disabled!")
        else:
            # the authentication system was unable to verify the username and password
            return HttpResponse("The username and password were incorrect.")
    else:
        form = LoginForm() # An unbound form

    return render(request, 'index.html', {
        'form': form,
    })


def signup_individual(request):
    if request.method == 'POST': # If the form has been submitted...
        form = SignupIndividualForm(request.POST) # A form bound to the POST data
        username = request.POST['email']
        password = request.POST['password']
        division = request.POST['division']
        code = request.POST['code']

        user = User.objects.create_user(username.split('@')[0], username, password)

        individual = IndividualUser()
        individual.user=user
        individual.division=division

        organization = OrganizationUser.objects.get(pk=code)
        print organization.user
        print code
        individual.company=organization

        individual.save()
        user.save()

        return redirect('/')

    else:
        form = SignupIndividualForm() # An unbound form

    return render(request, 'signupindividual.html', {
        'form': form,
    })

def signup_organization(request):
    if request.method == 'POST': # If the form has been submitted...
        form = SignupOrganizationForm(request.POST) # A form bound to the POST data
        username = request.POST['email']
        password = request.POST['password']
        name = request.POST['name']
        code = request.POST['code']

        user = User.objects.create_user(username.split('@')[0], username, password)

        organization = OrganizationUser()
        organization.user=user
        organization.code=code

        organization.save()
        user.save()

        return redirect('/')

    else:
        form = SignupOrganizationForm() # An unbound form

    return render(request, 'signuporganization.html', {
        'form': form,
    })

def home_individual(request):
    if request.user.is_authenticated():
        individual=IndividualUser.objects.get(user_id=request.user.id)
        projects=Project.objects.filter(company_id__exact=individual.company_id)
        return render_to_response('individual.html', {"user": request.user, "projects": projects})
    else:
        return HttpResponse("NOT VALID")


def home_organization(request):
    if request.user.is_authenticated():
        return render_to_response('individual.html')
    else:
        return HttpResponse("NOT VALID")

def logout_view(request):
    logout(request)
    return redirect('index')

