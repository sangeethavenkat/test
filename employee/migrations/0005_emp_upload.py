# Generated by Django 4.0 on 2022-02-12 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_alter_emp_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='emp',
            name='upload',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
