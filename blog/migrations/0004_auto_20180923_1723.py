# Generated by Django 2.1.1 on 2018-09-23 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='comment',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user_id',
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
    ]
