from django.db import models
from django.contrib.auth.models import User

#class UserProfile(models.Model):
#    user = models.ForeignKey(User)
    #some common fields here, which are shared among both corporate and individual profiles

class OrganizationUser(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=30) 
    #corporate fields here

    class Meta:
        db_table = 'corporate_user'

class IndividualUser(models.Model):
    user = models.ForeignKey(User)
    company = models.ForeignKey(OrganizationUser)
    #Individual user fields here

    class Meta:
        db_table = 'individual_user'

class Ticket(models.Model):
    company=models.ForeignKey(OrganizationUser)
    created_date=models.DateTimeField()
    modified_date=models.DateTimeField()

class Project(models.Model):
    ticket=models.ForeignKey(Ticket)
    name = models.CharField(max_length=30)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

class Expense(models.Model):
    project=models.ForeignKey(Project)
    name = models.CharField(max_length=30)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
