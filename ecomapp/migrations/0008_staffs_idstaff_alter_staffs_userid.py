# Generated by Django 4.1.7 on 2023-04-01 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0007_users_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffs',
            name='idStaff',
            field=models.CharField(db_column='ID', default=0, max_length=255, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='staffs',
            name='userid',
            field=models.OneToOneField(blank=True, db_column='UsersID', null=True, on_delete=django.db.models.deletion.CASCADE, to='ecomapp.users'),
        ),
    ]
