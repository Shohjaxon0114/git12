from django.contrib import admin
from .models import NoutbooksModel, CustomerModel
# Register your models here.

class NoutbooksAdmin(admin.ModelAdmin):
    list_display = ['model','price']
    search_fields = ['model','price']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['product_id','customer_name']
    search_fields = ['product_id']

admin.site.register(CustomerModel)
admin.site.register(NoutbooksModel)