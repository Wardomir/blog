# Generated by Django 3.0.5 on 2020-05-03 20:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='created_at',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
