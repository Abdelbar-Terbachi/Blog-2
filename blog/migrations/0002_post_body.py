# Generated by Django 3.2.6 on 2021-08-25 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(default='some text'),
            preserve_default=False,
        ),
    ]
