# Generated by Django 4.1.5 on 2023-01-14 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Answer',
            new_name='Choice',
        ),
    ]
