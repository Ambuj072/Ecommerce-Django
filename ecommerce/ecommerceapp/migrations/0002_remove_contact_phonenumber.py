# Generated by Django 5.1.2 on 2024-10-21 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='phonenumber',
        ),
    ]
