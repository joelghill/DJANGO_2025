from django.db import models


# Create your models here.
class Address(models.Model):
    street = models.CharField(max_length=250)
    unit_number = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    province = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.street} {self.unit_number} {self.city} {self.province} {self.postal_code} {self.country}"
