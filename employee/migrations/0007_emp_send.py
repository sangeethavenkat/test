# Generated by Django 4.0 on 2022-02-12 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_emp_empid'),
    ]

    operations = [
        migrations.AddField(
            model_name='emp',
            name='send',
            field=models.BooleanField(default=False),
        ),
    ]