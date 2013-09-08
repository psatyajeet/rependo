from django.db import models
from django.contrib.auth.models import User

from datetime import *

#class UserProfile(models.Model):
#    user = models.ForeignKey(User)
    #some common fields here, which are shared among both corporate and individual profiles

class OrganizationUser(models.Model):
    user = models.ForeignKey(User)
    code = models.CharField(max_length=30)
    #corporate fields here

    class Meta:
        db_table = 'organization_user'

class IndividualUser(models.Model):
    user = models.ForeignKey(User)
    company = models.ForeignKey(OrganizationUser)
    #Individual user fields here
    division = models.CharField(max_length=30)

    class Meta:
        db_table = 'individual_user'

class Project(models.Model):
    company=models.ForeignKey(OrganizationUser)
    name = models.CharField(max_length=30)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(default=datetime.now,blank=True)
    is_accepted = models.BooleanField(default=False)
    is_denied = models.BooleanField(default=False)

class Expense(models.Model):
    project=models.ForeignKey(Project)
    name = models.CharField(max_length=30)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
