# Generated by Django 3.0.5 on 2020-05-03 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0003_auto_20200501_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_activity',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
