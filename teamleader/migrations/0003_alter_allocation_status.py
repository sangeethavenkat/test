# Generated by Django 4.0 on 2022-02-04 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamleader', '0002_allocation_workstatus_alter_allocation_duedays_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allocation',
            name='status',
            field=models.CharField(default='pending', max_length=100),
        ),
    ]
