# Generated by Django 3.2.8 on 2022-02-16 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_rename_pat_vid_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vid',
            name='path',
            field=models.FileField(upload_to=''),
        ),
    ]
