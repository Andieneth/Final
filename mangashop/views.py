from django.shortcuts import render, redirect, get_object_or_404
from .models import ArticlesShop
from .forms import ArticlesShopForm
from django.views.generic import DetailView, UpdateView, DeleteView , ListView



def mangashop_home(request):
    #Фильтрация
    # Group_bySortir = request.GET.get('filtersbI', '')
    # if Group_bySortir:
    #     Manga = ArticlesShop.objects.exclude(price__lte=Group_bySortir)
    # else:
    #     Manga = ArticlesShop.objects.filter('price')
    # return render(request, 'mangashop/mangashop_home.html', {'Manga': Manga})

    # Сортировка
    # filter_query = request.GET.get('sort', '')
    # if filter_query:
    #     Manga = ArticlesShop.objects.order_by('-price')
    # else:
    #     Manga = ArticlesShop.objects.order_by('price')
    # return render(request, 'mangashop/mangashop_home.html', {'Manga': Manga})

    #Поиск
    search_query = request.GET.get('search', '')
    if search_query:
        Manga=ArticlesShop.objects.filter(title__icontains=search_query)
    else:
        Manga = ArticlesShop.objects.order_by('price')
    return render(request,'mangashop/mangashop_home.html', {'Manga': Manga})



class ShopDetailView(DetailView):
    model = ArticlesShop
    template_name = 'mangashop/mangashop_view.html'
    context_object_name = 'MangaArticle'
    def get_object(self, queryset=None):
        obj = super(ShopDetailView, self).get_object(queryset=queryset)
        obj.view_count += 1
        obj.save()
        return obj





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


# def product_detail(request, product_id):
#     Manga = get_object_or_404(ArticlesShop, id=product_id)
#     view_count = request.session.get('product%s_view_count' % product_id, 0)
#     view_count += 1
#     request.session['product%s_view_count' % product_id] = view_count
#     Manga.view_count = view_count
#     Manga.save()
#     return render(request, 'mangashop/mangashop_view.html', {'Manga': Manga})