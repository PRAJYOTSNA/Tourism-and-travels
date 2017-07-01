from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class State(models.Model):
          state=models.CharField(max_length=100)
          
          def __str__(self):
                 return self.state
                 
class Cities(models.Model):
          cities=models.CharField(max_length=100)
          
          def __str__(self):
                 return self.cities

class Areas(models.Model):
          areas=models.CharField(max_length=100)
          
          def __str__(self):
                 return self.areas
                 
class Profile(models.Model):
          #User = models.IntegerField()
          fname = models.CharField(max_length = 200)
          lname = models.CharField(max_length = 50, null=True, blank=True, default=None)
          address = models.CharField(max_length = 100, null=True, blank=True, default=None)
          phone_number = models.IntegerField()
          email = models.EmailField()
          
@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

@receiver(post_save, sender = User)
def create_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
    
