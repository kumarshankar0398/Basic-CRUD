# Generated by Django 3.2.10 on 2022-01-04 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_employee_empaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='EmpId',
            field=models.IntegerField(max_length=20),
        ),
    ]
