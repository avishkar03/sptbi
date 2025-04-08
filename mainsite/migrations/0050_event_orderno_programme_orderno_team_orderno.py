# Generated by Django 4.1.6 on 2023-08-27 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0049_banner_site_alter_incubatee_startup_sector'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='orderno',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='programme',
            name='orderno',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='team',
            name='orderno',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
