from django.conf.urls import patterns, url

from reimbursement import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^login', views.login, name='login'),
    url(r'^signupindividual', views.signup_individual, name='signup_individual'),
    url(r'^signuporganization', views.signup_organization, name='signup_organization'),
    url(r'^individual_home', views.home_individual, name='home_individual'),
    url(r'^organization_home', views.home_organization, name='home_organization'),
    url(r'^logout', views.logout_view, name="logout_view"),
    url(r'^addproject', views.add_project, name="add_project"),
    url(r'^approve', views.approve_project, name="approve_project"),

)
