from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def blog_single(request):
    return render(request, 'blog_single.html')

def blog(request):
    return render(request, 'blog.html')

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def portfolio(request):
    return render(request, 'portfolio')

def QRdev(request):
    return render(request, 'QRdev')

