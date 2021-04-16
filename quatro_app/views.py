from django.shortcuts import render

def MainPage(request):
    print(request)

    return render(request, 'index.html', {})