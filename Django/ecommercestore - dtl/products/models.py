from django.db import models

# Create your models here.
class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=20)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_description = models.TextField(null = True)
    product_category = models.CharField(max_length=30)
    product_stock = models.IntegerField()

    def __str__(self):
        return f'{self.product_name} - {self.product_price} - {self.product_description}'