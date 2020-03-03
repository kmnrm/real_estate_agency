# Generated by Django 2.2.5 on 2020-03-02 09:57

from django.db import migrations

def relate_owners_and_flats(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for owner in Owner.objects.all():
        owner.flats.set(
                Flat.objects.filter(
                        owner=owner.full_name, 
                        owners_phonenumber=owner.phonenumber,
                        owner_phone_pure=owner.phone_pure
                        )
                )

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20200304_0120'),
    ]

    operations = [
            migrations.RunPython(relate_owners_and_flats),
    ]

