from django.shortcuts import render, get_object_or_404

# models
from cars_items.models import Car

def MainPage(request):
    print(request)

    return render(request, 'index.html', {})

def ListPage(request):
    print(request)

    items = Car.objects.all()

    return render(request, 'list.html', { 'items': items })

def DetailsPage(request, pk):
    current_item = get_object_or_404(Car, pk = pk)

    print(request)

    print(current_item)

    return render(request, 'details.html', { 'item': current_item })

def ContactUsPage(request):
    print(request)

    return render(request, 'contact_us.html', {})