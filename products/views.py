

# Create your views here.

from django.shortcuts import render
from products.models import Product
def show(request):
    pro=Product.objects.all()
    return render(request,'result.html',{'pro':pro})
