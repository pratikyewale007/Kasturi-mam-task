from django import forms
from .models import Product

class Prodregister(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'product_name' : 'Enter Product Name',
            'product_price' : 'Enter Product Price',
            'product_description' : 'Enter Product Description',
            'product_category' : 'Enter Product Category',
            'product_stock' : 'Enter Product Stock',
        }