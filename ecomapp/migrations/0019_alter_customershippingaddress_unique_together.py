# Generated by Django 4.1.7 on 2023-04-11 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0018_remove_order_addressid'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='customershippingaddress',
            unique_together=set(),
        ),
    ]
