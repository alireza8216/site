# Generated by Django 3.2.8 on 2022-02-24 10:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20220224_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(auto_created=datetime.datetime(2022, 2, 24, 10, 19, 12, 620736, tzinfo=utc), default=datetime.datetime(2022, 2, 24, 10, 19, 12, 620736, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='coment',
            name='date',
            field=models.DateField(auto_created=datetime.datetime(2022, 2, 24, 10, 19, 12, 621736, tzinfo=utc), default=datetime.datetime(2022, 2, 24, 10, 19, 12, 621736, tzinfo=utc)),
        ),
    ]
