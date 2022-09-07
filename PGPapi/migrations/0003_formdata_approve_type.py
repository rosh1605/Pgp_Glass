# Generated by Django 4.0.6 on 2022-08-29 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PGPapi', '0002_usersession_contractor_usersession_contractor_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='formdata',
            name='approve_type',
            field=models.CharField(choices=[('Suspend', 'Suspend'), ('Hold', 'Hold'), ('Terminate', 'Terminate'), ('None', 'None')], default='None', max_length=20),
        ),
    ]
