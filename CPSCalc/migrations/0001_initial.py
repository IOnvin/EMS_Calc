# Generated by Django 2.2.6 on 2020-09-22 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CPSCostModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpsHours', models.IntegerField(max_length=2)),
                ('term', models.IntegerField(max_length=2)),
            ],
        ),
    ]