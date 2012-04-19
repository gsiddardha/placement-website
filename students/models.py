from misc.choices import GENDER_CHOICES, HOSTEL_CHOICES

from django.db import models
from django.contrib.auth.models import User
from departments.models import Department 

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    
    rollNo = models.CharField(max_length=8)#, label='Roll Number')
    mobileNo = models.CharField(max_length=10)#, label='Mobile Number')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    hostel = models.CharField(max_length=2, choices=HOSTEL_CHOICES)
    roomNo = models.CharField(max_length=10)#, label='Room Number')
    department = models.ForeignKey(Department)
    joinYear = models.IntegerField()#label='Year of Joining')
    stream = models.CharField(max_length=10)
    
    cgpa = models.FloatField()
    
    def __unicode__(self):
        return self.rollNo