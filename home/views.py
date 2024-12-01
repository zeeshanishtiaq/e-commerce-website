from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request, 'index.html') 

def shop(request):
    return render (request, 'shop.html') 

def about(request):
    return render (request, 'about.html') 

def contact(request):
    return render (request, 'contact.html')  

def produce(request):
    return render (request, 'produce.html') 

def cart(request):
    return render (request, 'cart.html') 

def checkout(request):
    return render (request, 'checkout.html')

def homemenu(request):
    return render (request, 'homemenu.html')

def menu(request):
    return render (request, 'menu.html')

def login(request):
    return render (request, 'login.html')

def register(request):
    return render (request, 'register.html')

def product(request):
    return render (request, 'product.html')

