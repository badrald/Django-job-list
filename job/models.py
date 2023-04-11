from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User 
# Create your models here.

JOB_TYEP=(
          ("Full-time","Full-time"),
          ("Part-time",'Part-time')
     )

class Category(models.Model):
    name=models.CharField(max_length=25)
    def __str__(self) -> str:
        return self.name
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

def upload_pics(inctence,pic):
    return f"jobs/{inctence.id}.{pic.split('.')[1]}"


class Job(models.Model):
    owner=models.ForeignKey(User,related_name='owner',on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    job_type=models.CharField(max_length=15,choices=JOB_TYEP)
    description= models.TextField(max_length=1000)
    published_at=models.DateTimeField(auto_now=True)
    vecancy= models.SmallIntegerField(default=1)
    salary=models.IntegerField(default=0)
    experience=models.SmallIntegerField(default=0)
    photo=models.ImageField(upload_to=upload_pics, height_field=None, width_field=None, max_length=None)
    category=models.ForeignKey(Category,name='category',on_delete=models.CASCADE)
    slug= models.SlugField(null=True,blank=True)

    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super(Job,self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'
        ordering = ['-published_at']
        get_latest_by ='-published_at'


class Apply(models.Model):
    user=models.ForeignKey(User,related_name='apply_user',on_delete=models.CASCADE)
    job=models.ForeignKey(Job,related_name='apply_job',on_delete=models.CASCADE)
    name= models.CharField(max_length=50)
    email=models.EmailField()
    website=models.URLField()
    cv_file=models.FileField(upload_to='apply/')
    description=models.TextField()
    created_at=models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'apply'
        verbose_name_plural = 'applies'




    
