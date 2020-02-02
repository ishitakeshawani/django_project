# Generated by Django 2.2.6 on 2020-01-18 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200118_1155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enroll',
            old_name='outofmid',
            new_name='outofmidsub1',
        ),
        migrations.AddField(
            model_name='enroll',
            name='outofmidsub2',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='enroll',
            name='outofmidsub3',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='enroll',
            name='outofmidsub4',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='enroll',
            name='outofmidsub5',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='enroll',
            name='subject1',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='enroll',
            name='subject2',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='enroll',
            name='subject3',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='enroll',
            name='subject4',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='enroll',
            name='subject5',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
