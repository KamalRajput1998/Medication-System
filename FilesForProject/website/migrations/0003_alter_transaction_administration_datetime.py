# Generated by Django 4.2.4 on 2023-08-16 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_drug_patient_route_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='Administration_DateTime',
            field=models.DateTimeField(verbose_name='Administration Date & Time'),
        ),
    ]
