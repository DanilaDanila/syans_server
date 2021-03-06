# Generated by Django 4.0 on 2021-12-14 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('contracts', '0002_rename_user_contract_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='executor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='executor', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contract',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='auth.user'),
        ),
    ]
