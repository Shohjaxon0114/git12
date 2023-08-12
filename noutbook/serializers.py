from rest_framework import serializers
from .models import NoutbooksModel, CustomerModel

class NoutbooksModelSerializers(serializers.ModelSerializer):
    # model = serializers.CharField()
    # protcessor = serializers.CharField()
    # ram = serializers.IntegerField()
    # ssd = serializers.IntegerField()
    # hdd = serializers.IntegerField()
    # price = serializers.FloatField()
    # buy_date = serializers.DateTimeField()

    class Meta:
        model = NoutbooksModel
        fields = ('model','protcessor','protcessor','ram','ssd','hdd','price')

class CustomerModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomerModel
        fields= ('product_id','customer_name')

