# Generated by Django 4.2 on 2023-04-07 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=25),
        ),
    ]
