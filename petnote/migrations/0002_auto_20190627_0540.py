# Generated by Django 2.2.2 on 2019-06-27 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petnote', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pets',
            name='petname',
            field=models.CharField(max_length=30),
        ),
    ]
