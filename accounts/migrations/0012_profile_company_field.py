# Generated by Django 4.2 on 2023-04-22 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_profile_company_address_profile_company_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='company_field',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
