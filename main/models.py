from django.db import models



class Sales (models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    product = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.CharField(max_length=100)
    profit = models.CharField(max_length=100)
    total = models.CharField(max_length=100)
    discount = models.CharField(max_length=100)
    customer = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.product
    

