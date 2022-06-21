from dataclasses import field
from django.shortcuts import render,get_object_or_404,redirect
from django.forms import  modelform_factory
from django import forms
from products.models import Product,User

# Create your views here.

def Products(request):
    return render(request, 'products/Products.html',
                  {
                   "range": range(5),
                   "products":Product.objects.all()
                  }
                 )


def Product_Details(request, id):
    product = get_object_or_404(Product,pk=id)
    return render(request, 'products/Product_Detail.html',
                  {"product": product}
                  )

ProductForm = modelform_factory(Product,exclude=[])

class UserForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model =  User
        fields = {'Name','Email','Password'} 

def Add_New_User(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = UserForm()
    return  render(request,'products/Add_New_User.html',{"form":form})

def Add_New_Product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = ProductForm()
    return  render(request,'products/Add_New_Product.html',{"form":form})
