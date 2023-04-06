from django.db import models

# Create your models here.

JOB_TYEP=(
          ("Full-time","Full-time"),
          ("Part-time",'Part-time')
     )

class Category(models.Model):
    name=models.CharField(max_length=15)
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
class Job(models.Model):

    title=models.CharField(max_length=100)
    job_type=models.CharField(max_length=15,choices=JOB_TYEP)
    description= models.TextField(max_length=1000)
    published_at=models.DateTimeField(auto_now=True)
    vecancy= models.SmallIntegerField(default=1)
    salary=models.IntegerField(default=0)
    experience=models.SmallIntegerField(default=0)
    category=models.ForeignKey(Category,name='category',on_delete=models.CASCADE)
    def __str__(self):
        return self.title




    
