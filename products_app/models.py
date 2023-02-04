from django.db import models
from task4_app.models import User

class Product(models.Model):
    product_name = models.CharField(max_length=100, default="")
    product_description = models.CharField(max_length=100, default="")
    product_inventory_count = models.IntegerField(default=0)
    created_by = models.ForeignKey(User, related_name="created_by", on_delete=models.CASCADE, null=True, blank=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.product_name
