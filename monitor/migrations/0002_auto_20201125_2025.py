# Generated by Django 3.1.3 on 2020-11-25 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stat',
            old_name='source',
            new_name='source_id',
        ),
    ]
