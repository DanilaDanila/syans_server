# Generated by Django 4.0 on 2021-12-18 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0004_alter_contract_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='status',
            field=models.CharField(default='offered', max_length=15),
            preserve_default=False,
        ),
    ]
