# Generated by Django 3.1.5 on 2021-01-07 06:52

from django.db import migrations, models
import watch.models


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0002_auto_20210107_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coinrate',
            name='time',
            field=models.DateTimeField(default=watch.models.current_time),
        ),
    ]
