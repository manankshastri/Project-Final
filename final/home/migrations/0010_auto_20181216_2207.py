# Generated by Django 2.1.4 on 2018-12-17 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20181216_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_patient',
            field=models.BooleanField(default=True),
        ),
    ]