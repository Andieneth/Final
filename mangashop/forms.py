from .models import ArticlesShop
from django.forms import ModelForm, TextInput

class ArticlesShopForm(ModelForm):
    class Meta:
        model = ArticlesShop
        fields = ['title', 'price', 'Text']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название манги'
            }),
            "Text": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название манги'
            }),
            "price": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена манги'
            })
        }