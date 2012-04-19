from misc.choices import BOOLEAN_CHOICES
from departments.models import *

from django.contrib.auth.models import User

class Company(models.Model):
    company = models.OneToOneField(User)
    
    hr_name = models.CharField(max_length=80)
    hr_mobile = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
    fax = models.CharField(max_length=15)  
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    
class Profile(models.Model):
    company = models.ForeignKey('Company')
    
    name = models.CharField(max_length=80)
    description = models.TextField()
    bond_details = models.TextField()
    resumes = models.BooleanField(choices=BOOLEAN_CHOICES)
    aptitude_test = models.BooleanField(choices=BOOLEAN_CHOICES)
    tech_test = models.BooleanField(choices=BOOLEAN_CHOICES)
    group_discussion = models.BooleanField(choices=BOOLEAN_CHOICES)
    personal_interview = models.BooleanField(choices=BOOLEAN_CHOICES)
    departments = models.ManyToManyField(Department)
    