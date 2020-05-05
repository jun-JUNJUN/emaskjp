from django.db import models
from django.utils import timezone

# Create your models here.


class RFI(models.Model):
    customer_company = models.CharField(max_length=200)
    customer_name = models.CharField(max_length=200)
    customer_prefecture = models.CharField(max_length=50)
    customer_addr = models.CharField(max_length=400)
    create_dt = models.DateTimeField('date created')

    def __str__(self):
        return self.customer_name

    def was_created(self):
        return self.create_dt
