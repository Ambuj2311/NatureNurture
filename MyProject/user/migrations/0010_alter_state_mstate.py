# Generated by Django 3.2.4 on 2022-09-05 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='mstate',
            field=models.CharField(max_length=30),
        ),
    ]