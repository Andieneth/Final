from django.shortcuts import render

def index(request):
    return render(request, 'main/manga.html')

def Shop(request):
    return render(request, 'main/shop.html')
