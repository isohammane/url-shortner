# Generated by Django 3.1.7 on 2021-04-01 08:14

from django.db import migrations, models
import short.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original', models.CharField(max_length=500, null=True)),
                ('short', models.CharField(default=short.models.unique_link, max_length=8)),
            ],
        ),
    ]