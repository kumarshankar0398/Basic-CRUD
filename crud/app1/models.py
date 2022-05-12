from django.db import models


class Employee(models.Model):
    EmpId = models.IntegerField()
    EmpName = models.CharField(max_length=100)
    EmpContact = models.CharField(max_length=20)
    EmpSal = models.IntegerField()
    EmpEmail = models.EmailField()
    EmpAddress = models.TextField(max_length=500)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.EmpName


