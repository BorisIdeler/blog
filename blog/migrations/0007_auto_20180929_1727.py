# Generated by Django 2.1.1 on 2018-09-29 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180929_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='image',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='short',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='short',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]