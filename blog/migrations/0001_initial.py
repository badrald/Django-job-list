# Generated by Django 4.2 on 2023-04-27 17:15

import blog.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0015_profile_cv_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to=blog.models.get_blog_images_path)),
                ('description', models.CharField(max_length=255)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('Content', models.TextField(blank=True, null=True)),
                ('Quote', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.category')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portile_user', to='accounts.profile')),
                ('tags', models.ManyToManyField(blank=True, to='blog.tag')),
            ],
            options={
                'ordering': ['-published_at'],
            },
        ),
    ]
