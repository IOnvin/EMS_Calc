# Generated by Django 3.0.7 on 2021-03-31 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuoteInput', '0005_delete_hostingmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quoteinputmodel',
            name='name',
        ),
    ]
