# Generated by Django 3.1 on 2020-08-22 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date']},
        ),
    ]
