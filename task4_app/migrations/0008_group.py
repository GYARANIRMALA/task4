# Generated by Django 4.0.5 on 2022-10-12 07:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('task4_app', '0007_alter_user_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
    ]