# Generated by Django 2.2.6 on 2020-02-01 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200201_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enroll',
            name='enno',
            field=models.BigIntegerField(blank=True),
        ),
    ]
