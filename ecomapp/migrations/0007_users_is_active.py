# Generated by Django 4.1.7 on 2023-04-01 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0006_remove_address_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='is_active',
            field=models.BooleanField(db_column='IsAcitve', default=True),
        ),
    ]