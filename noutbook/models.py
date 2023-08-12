import datetime
from django.db import models

# Create your models here.
class NoutbooksModel(models.Model):
    model = models.CharField(max_length=200,default='')
    protcessor = models.CharField(max_length=50,default='')
    ram = models.IntegerField(default=0)
    ssd = models.IntegerField(default=0)
    hdd = models.IntegerField(default=0)
    price = models.FloatField()
    buy_date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.model

    class Meta:
        db_table = 'noutbooks'

class CustomerModel(models.Model):
    product_id = models.ForeignKey(NoutbooksModel,on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=200)

    def __str__(self):
        return self.customer_name

    class Meta:
        db_table = 'customer'


