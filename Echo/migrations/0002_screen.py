# Generated by Django 2.2.6 on 2019-11-19 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Echo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(verbose_name='status')),
            ],
        ),
    ]
