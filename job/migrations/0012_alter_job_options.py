# Generated by Django 4.2 on 2023-04-11 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0011_apply_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['-published_at'], 'verbose_name': 'Job', 'verbose_name_plural': 'Jobs'},
        ),
    ]
