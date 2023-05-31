from django.urls import path,re_path
from . import views

urlpatterns = [
   path('', views.mangashop_home, name='mangashop_home'),
   path('createmanga',views.createmanga,name='createmanga'),
   path('<int:pk>', views.ShopDetailView.as_view(), name='Shop_detail'),
   path('<int:pk>/update', views.ShopUpdateView.as_view(), name='Shop_update'),
   path('<int:pk>/delete', views.ShopDeleteView.as_view(), name='Shop_delete'),

]
