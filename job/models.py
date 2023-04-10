from django.db import models
from django.utils.text import slugify
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




    
