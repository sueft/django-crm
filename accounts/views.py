from django.shortcuts import render,redirect,get_object_or_404
from .models import Product
from .forms import ProductForm,SignUpForm
from django.contrib import messages
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def product(request):
    products= Product.objects.all()
    return render(request,'products/product.html',{'products':products})

@login_required
def create(request):
    if request.method == 'POST':
       form = ProductForm(request.POST)
       if form.is_valid():
          form.save()
          messages.success(request,"product created successfully")
          return redirect('product')
    else:
        form=ProductForm()
    return render(request,'products/create.html',{'form':form})

@login_required
def update(request,product_id):
    product=get_object_or_404(Product, id=product_id)
    if request.method=='POST':
       form=ProductForm(request.POST,instance=product)
       if form.is_valid():
           form.save()
           messages.success(request,"product updated successfully")
           return redirect('product')
    else:
       form=ProductForm(instance=product)
    return render(request,'products/update.html',{'form':form,'product': product})

@login_required
def delete(request,product_id):
    product=get_object_or_404(Product, id=product_id)
    if request.method=='POST':
       product.delete()
       messages.success(request,"product deleted successfully")
       return redirect('product')
    return render(request,'products/delete.html',{'product':product})



def logout_user(request):
    logout(request)
    messages.success(request,"user logged out successfully")
    return redirect('index')


def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"user logged in successfully")
            return redirect('product')  # Redirect to a desired page
    else:
        messages.error(request, 'Invalid username or password.')
    return render(request, 'index.html')

def register(request):
    if request.method =="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
           form.save()
           messages.success(request,'registration successful')
           return redirect('index')
    else:
        form=SignUpForm()
    return render(request,'register.html',{'form':form})
