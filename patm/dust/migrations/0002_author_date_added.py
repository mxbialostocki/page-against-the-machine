# Generated by Django 2.1.15 on 2020-11-18 02:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dust', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=datetime.datetime(2020, 11, 18, 2, 19, 15, 783405, tzinfo=utc)),
            preserve_default=False,
        ),
    ]