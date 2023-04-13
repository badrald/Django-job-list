from django.db import models

from django.contrib.auth.models import User 

from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField
# Create your models here.

def upload_pics(inctence,pic):
    return f"Profiles/{inctence.id}.{pic.split('.')[1]}"

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    country=CountryField(null=True,blank=True)
    phone_number=models.CharField(max_length=15,null=True,blank=True)
    image=models.ImageField(upload_to=upload_pics,null=True,blank=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    WebsiteUrl=models.URLField(null=True,blank=True)
    GithubUrl=models.URLField(null=True,blank=True)
    TwitterUrl=models.URLField(null=True,blank=True)
    InstagramUrl=models.URLField(null=True,blank=True)
    FacebookUrl=models.URLField(null=True,blank=True)

    def __str__(self) :
        if self.first_name =='' or self.first_name == None:
            return self.user.username
        return self.first_name + " "+ self.last_name
    


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)