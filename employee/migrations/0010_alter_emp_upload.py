# Generated by Django 4.0 on 2022-02-15 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0009_emp_project_emp_tl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='upload',
            field=models.FileField(default='Null', null=True, upload_to=''),
        ),
    ]