from django.db import models
from django.contrib.auth.models import User
from mangashop.models import ArticlesShop

borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(ArticlesShop)

    def __str__(self):
        return f"Корзина {self.user.username}"