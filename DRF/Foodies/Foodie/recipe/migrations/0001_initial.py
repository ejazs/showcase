# Generated by Django 2.2.8 on 2020-03-06 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('ingredients', models.TextField()),
                ('method', models.TextField()),
                ('tips', models.CharField(max_length=255)),
            ],
        ),
    ]
