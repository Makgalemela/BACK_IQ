# Generated by Django 2.2.6 on 2019-11-15 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssetMgmt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='screen',
            name='control',
            field=models.IntegerField(default=0),
        ),
    ]
