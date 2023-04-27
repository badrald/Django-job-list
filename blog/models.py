from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from accounts.models import Profile

# Create your models here.

def get_blog_images_path(instance, filename):
    # Construct the file path for the image based on the instance ID and filename
    ext = filename.split('.')[-1]
    path = f'blogs/{instance.id}/{instance.id}.{ext}'
    return path
    


class Blog(models.Model):
    title = models.CharField(max_length=50)
    image_1 = models.ImageField(upload_to=get_blog_images_path, blank=True, null=True)
    description = models.CharField(max_length=255)
    published_at = models.DateTimeField(auto_now=True)
    Content = models.TextField(blank=True, null=True)
    Quote = models.TextField(blank=True, null=True)
    profile = models.ForeignKey(Profile,related_name='portile_user',on_delete=models.CASCADE)
    # Add a slug field to generate a URL-friendly version of the title
    slug = models.SlugField(max_length=50, unique=True)

    # Add a foreign key to associate the blog with a category
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    # Add a many-to-many field to associate the blog with multiple tags
    tags = models.ManyToManyField('Tag', blank=True)

    # Add a method to get the absolute URL of the blog
    def get_absolute_url(self):
        return reverse('singal_blog', args=[self.slug])

    class Meta:
        ordering = ['-published_at']
    
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super(Blog,self).save(*args, **kwargs)


    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
