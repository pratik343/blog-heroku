# Generated by Django 3.0.7 on 2020-06-23 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='quote',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AddField(
            model_name='posts',
            name='quote_head',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
