# Generated by Django 3.0.5 on 2020-05-01 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0002_auto_20200501_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=345, unique=True),
        ),
    ]
