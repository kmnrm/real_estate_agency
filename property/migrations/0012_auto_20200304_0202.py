# Generated by Django 2.2.5 on 2020-03-03 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20200304_0124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_phone_pure',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
    ]