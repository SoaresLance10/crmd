# Generated by Django 2.2.4 on 2020-10-11 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CalculatedScores',
            new_name='CalculatedScore',
        ),
    ]