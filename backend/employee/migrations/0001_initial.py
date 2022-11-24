# Generated by Django 4.1.3 on 2022-11-24 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departaments',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('departament_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('employee_name', models.CharField(max_length=100)),
                ('departament_name', models.CharField(max_length=100)),
                ('date_of_joining', models.DateField()),
                ('photo_file_name', models.CharField(max_length=100)),
            ],
        ),
    ]