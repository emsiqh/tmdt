# Generated by Django 4.1.7 on 2023-04-02 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0012_remove_product_name_alter_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, db_column='Name', max_length=255, null=True),
        ),
    ]