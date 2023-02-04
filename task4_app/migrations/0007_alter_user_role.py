# Generated by Django 4.0.5 on 2022-10-01 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task4_app', '0006_alter_user_options_remove_user_date_joined_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('manager', 'Manager'), ('staff', 'Staff')], default='', max_length=50),
        ),
    ]
