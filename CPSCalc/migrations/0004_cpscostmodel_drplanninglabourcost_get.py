# Generated by Django 2.2.6 on 2020-09-22 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CPSCalc', '0003_auto_20200922_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpscostmodel',
            name='drPlanningLabourCost_get',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CPSCalc.DRPlanningLaborCostRateModel'),
        ),
    ]