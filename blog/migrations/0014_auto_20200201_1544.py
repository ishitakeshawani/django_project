# Generated by Django 2.2.6 on 2020-02-01 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200201_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enroll',
            name='enno',
            field=models.BigIntegerField(null=True),
        ),
    ]