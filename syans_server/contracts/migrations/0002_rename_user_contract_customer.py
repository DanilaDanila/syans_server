# Generated by Django 4.0 on 2021-12-14 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contract',
            old_name='user',
            new_name='customer',
        ),
    ]