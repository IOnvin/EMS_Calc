from django.db import models
from django.urls import reverse


class DRPlanningLaborCostRateModel(models.Model):
    DRPlanningLaborCostRate_USDPerHr = models.IntegerField(null=False)

    def __str__(self):
        return f'{self.DRPlanningLaborCostRate_USDPerHr}'

    def get_DRPlanningLaborCostRate(self):
        if __name__ == '__main__':
            return self.DRPlanningLaborCostRate_USDPerHr


class CPSCostModel(models.Model):
    drPlanningLabourCost_get = models.ForeignKey(DRPlanningLaborCostRateModel, on_delete=models.SET_NULL, null=True)
    cpsHours = models.IntegerField(null=False)
    term = models.IntegerField(null=False)

    def get_cpsCalculatedCost(self):
        return self.cpsHours * self.term * self.drPlanningLabourCost_get.DRPlanningLaborCostRate_USDPerHr
