from django.shortcuts import render,get_object_or_404,redirect
from django.forms import  modelform_factory
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

UserForm = modelform_factory(User,exclude=[])

def Add_New_User(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = UserForm()
    return  render(request,'products/Add_New_User.html',{"form":form})
