from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponseRedirect

from reimbursement.forms import LoginForm


def index(request):
    context = {}

    return render(request, 'index.html', context)

def signup_individual(request):
    if request.method == "POST":
        name = request.GET['name']
        password = request.GET['password']

        d = [];

        if (request.session.__contains__('fbid') and not (request.session['fbid'] == fbid)):
            d.append({'changed': True, })
        request.session['fbid'] = fbid
        usr = UserProfile.objects.filter(user=fbid)

        if(len(usr) != 0):
            return HttpResponse(simplejson.dumps(d))

        prof = UserProfile(user=fbid,name=name)
        prof.save()

        return HttpResponse()
    else :
        return render(request, 'reimbursement/signup.html')

def login(request):
    if request.method == 'POST': # If the form has been submitted...
        form = LoginForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                # the password verified for the user
                if user.is_active:
                    return HttpResponse("User is valid, active and authenticated")
                else:
                    return HttpResponse("The password is valid, but the account has been disabled!")
            else:
                # the authentication system was unable to verify the username and password
                return HttpResponse("The username and password were incorrect.")
    else:
        form = LoginForm() # An unbound form

    return render(request, 'reimbursement/login.html', {
        'form': form,
    })
