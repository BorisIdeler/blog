# Generated by Django 2.1.1 on 2018-09-26 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180923_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.CharField(default='default@example.com', max_length=100),
            preserve_default=False,
        ),
    ]
