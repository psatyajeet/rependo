from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField()

class SignupOrganizationForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField()
    name = forms.CharField(max_length=30) 

class SignupIndividualForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField()
    name = forms.CharField(max_length=30) 
    company = forms.CharField(max_length=30)

