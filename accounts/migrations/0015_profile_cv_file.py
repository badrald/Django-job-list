# Generated by Django 4.2 on 2023-04-25 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_alter_company_options_alter_company_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cv_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
