# Generated by Django 2.2.5 on 2020-03-02 08:46

from django.db import migrations

def copy_owners_to_new_model(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        Owner.objects.get_or_create(
                full_name=flat.owner, 
                phonenumber=flat.owners_phonenumber, 
                phone_pure=flat.owner_phone_pure,
                )


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_owner'),
    ]

    operations = [
            migrations.RunPython(copy_owners_to_new_model),
    ]
