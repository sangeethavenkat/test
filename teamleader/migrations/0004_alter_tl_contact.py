# Generated by Django 4.0 on 2022-02-12 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamleader', '0003_alter_allocation_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tl',
            name='contact',
            field=models.BigIntegerField(null=True),
        ),
    ]
