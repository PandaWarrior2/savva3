# Generated by Django 2.1.2 on 2018-11-18 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_auto_20181118_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='md5',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
