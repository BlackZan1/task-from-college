from django.shortcuts import render

def MainPage(request):
    print(request)

    return render(request, 'index.html', {})

def ListPage(request):
    print(request)

    return render(request, 'list.html', {})

def DetailsPage(request):
    print(request)

    return render(request, 'details.html', {})