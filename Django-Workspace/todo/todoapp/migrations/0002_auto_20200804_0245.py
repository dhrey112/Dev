# Generated by Django 3.0.3 on 2020-08-04 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='datePulished',
            new_name='datePublished',
        ),
        migrations.AlterField(
            model_name='todo',
            name='todo',
            field=models.CharField(max_length=128),
        ),
    ]
