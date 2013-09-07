from django.conf.urls import patterns, url

from reimbursement import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^login', views.login, name='login'),
    url(r'^signupindividual', views.signup_individual, name='signup_individual'),
    url(r'^signuporganization', views.signup_organization, name='signup_organization')

)
