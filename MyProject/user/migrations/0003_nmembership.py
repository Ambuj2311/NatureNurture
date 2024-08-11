# Generated by Django 3.2.4 on 2022-09-04 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_myblog'),
    ]

    operations = [
        migrations.CreateModel(
            name='nmembership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nname', models.CharField(max_length=40)),
                ('npincode', models.CharField(max_length=40)),
                ('ncity', models.CharField(max_length=30)),
                ('nemail', models.EmailField(max_length=254)),
                ('nbankacount', models.CharField(max_length=60)),
                ('ncompanyaddress', models.CharField(max_length=40)),
                ('naddress', models.CharField(max_length=40)),
            ],
        ),
    ]