from django.shortcuts import render

def index(request):
    data = {
        'title': 'Приветствую тебя на сайте MangaLib!'
    }
    return render(request, 'main/manga.html',data)

def Shop(request):
    return render(request, 'main/shop.html')
