# Generated by Django 2.2.6 on 2020-01-19 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200119_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enroll',
            name='enno',
            field=models.IntegerField(max_length=50),
        ),
    ]
