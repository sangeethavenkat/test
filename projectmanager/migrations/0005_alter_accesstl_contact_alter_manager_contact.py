# Generated by Django 4.0 on 2022-02-12 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanager', '0004_alter_accesstl_contact_alter_accesstl_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesstl',
            name='contact',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='manager',
            name='contact',
            field=models.BigIntegerField(null=True),
        ),
    ]
