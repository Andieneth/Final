from django.shortcuts import render, redirect
from .models import ArticlesShop
from .forms import ArticlesShopForm
from django.views.generic import DetailView, UpdateView, DeleteView




def mangashop_home(request):
    Manga = ArticlesShop.objects.order_by('price')
    return render(request,'mangashop/mangashop_home.html', {'Manga': Manga})


class ShopDetailView(DetailView):
    model = ArticlesShop
    template_name = 'mangashop/mangashop_view.html'
    context_object_name = 'MangaArticle'


class ShopUpdateView(UpdateView):
    model = ArticlesShop
    template_name = 'mangashop/createmanga.html'

    form_class = ArticlesShopForm

class ShopDeleteView(DeleteView):
    model = ArticlesShop
    success_url = '/mangashop/'
    template_name = 'mangashop/deletemanga.html'


def createmanga(request):
    error=''
    if request.method == 'POST':
        Form = ArticlesShopForm(request.POST)
        if Form.is_valid():
            Form.save()
            return redirect('/mangashop')
        else:
            error = 'Не правильно форму заполнил'

    Form = ArticlesShopForm()

    datas ={
        'Form': Form,
        'error': error
    }

    return render(request, 'mangashop/createmanga.html',datas)