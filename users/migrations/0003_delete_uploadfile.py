# Generated by Django 2.1.7 on 2019-03-26 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190326_0326'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UploadFile',
        ),
    ]