from django.urls import path, include , re_path
from . import views
from django.views.generic import RedirectView
urlpatterns = [
   path('', views.index,name='Home'),
   path('about', views.Shop,name='about'),
   path('account', views.Account,name='Account'),
   path('accounts/', include('django.contrib.auth.urls')),
   re_path(r'^account/add_to_cart/(?P<ArticlesShop_id>\d+)$', views.add_to_cart, name='add_to_cart'),
   path('account/buy_order/', views.buy_order, name='buy_order'),
   re_path(r'^account/(?P<ArticlesShop_id>\d+)$', views.remove_from_cart, name='remove_from_cart'),
   re_path(r'^account/add_to_cart/(?P<ArticlesShop_id>\d+)$',RedirectView.as_view(url='/account',permanent=True))
]
