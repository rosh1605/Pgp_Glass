# Generated by Django 4.0.6 on 2022-08-29 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PGPapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersession',
            name='contractor',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='usersession',
            name='contractor_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
