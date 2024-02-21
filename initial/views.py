from django.shortcuts import render


def home(request):
    return render(request, "index.html")


def men(request):
    return render(request, 'categories.html')


def women(request):
    return render(request, 'categories.html')


def baby(request):
    return render(request, 'categories.html')
