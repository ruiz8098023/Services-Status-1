# Generated by Django 2.0.5 on 2020-04-06 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0002_auto_20200406_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='services',
            field=models.ManyToManyField(to='status.Service'),
        ),
    ]
