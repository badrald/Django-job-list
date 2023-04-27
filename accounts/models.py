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
    city= models.CharField(max_length=50, blank=True, null=True)
    phone_number=models.CharField(max_length=15,null=True,blank=True)
    image=models.ImageField(upload_to=upload_pics,null=True,blank=True)
    profession=  models.CharField(max_length=50, blank=True, null=True)
    cv_file= models.FileField(blank=True, null=True)
    WebsiteUrl=models.URLField(null=True,blank=True)
    GithubUrl=models.URLField(null=True,blank=True)
    TwitterUrl=models.URLField(null=True,blank=True)
    LinkeInUrl=models.URLField(null=True,blank=True)
    FacebookUrl=models.URLField(null=True,blank=True)
    def __str__(self) :
        if self.user.first_name =='' or self.user.first_name == None:
            return self.user.username
        return self.user.first_name + " "+ self.user.last_name
    
    
    
class Company(models.Model):
    company_name = models.CharField(max_length=255)
    compnay_logo= models.ImageField(upload_to='Companies/')
    company_size = models.CharField(max_length=255)
    company_field = models.CharField(max_length=255)
    company_address = models.CharField(max_length=255)
    company_founded = models.DateField(null=True, blank=True)
    company_revenue = models.CharField(max_length=255, null=True, blank=True)
    company_ceo = models.CharField(max_length=255, null=True, blank=True)
    company_phone_number = models.CharField(max_length=20)
    company_website_url = models.URLField(null=True, blank=True)
    company_twitter_url = models.URLField(null=True, blank=True)
    company_linkedin_url = models.URLField(null=True, blank=True)
    company_facebook_url = models.URLField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile= models.ForeignKey(Profile,related_name='profile_name',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.company_name
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

class Service(models.Model):
    name = models.CharField(max_length=255)
    company = models.ManyToManyField(Company, related_name='services')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)