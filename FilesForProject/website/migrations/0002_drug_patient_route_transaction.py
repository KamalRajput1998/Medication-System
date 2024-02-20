# Generated by Django 4.2.4 on 2023-08-16 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Drug_Name', models.CharField(max_length=100)),
                ('Brand_Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('System_Number', models.CharField(max_length=10)),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('DOB', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Administration_Route', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dose', models.CharField(max_length=20)),
                ('Administration_DateTime', models.DateTimeField()),
                ('Administration_Route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.route')),
                ('Drug_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.drug')),
                ('System_Number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.patient')),
            ],
        ),
    ]
