from django.shortcuts import render

# models
from cars_items.models import Car

def MainPage(request):
    print(request)

    return render(request, 'index.html', {})

def ListPage(request):
    print(request)
    
    items = Car.objects.all()

    return render(request, 'list.html', { 'items': items })

def DetailsPage(request):
    print(request)

    return render(request, 'details.html', {})

def ContactUsPage(request):
    print(request)

    return render(request, 'contact_us.html', {})