# Generated by Django 3.2.10 on 2022-01-05 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_employee_empid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='employee',
            name='EmpId',
            field=models.IntegerField(),
        ),
    ]
