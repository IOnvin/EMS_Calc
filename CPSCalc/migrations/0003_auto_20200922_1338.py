# Generated by Django 2.2.6 on 2020-09-22 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CPSCalc', '0002_drplanninglaborcostratemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpscostmodel',
            name='cpsHours',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cpscostmodel',
            name='term',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='drplanninglaborcostratemodel',
            name='DRPlanningLaborCostRate_USDPerHr',
            field=models.IntegerField(),
        ),
    ]