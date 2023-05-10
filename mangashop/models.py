from django.db import models

class ArticlesShop(models.Model):
    title = models.CharField('Название манги',max_length=50)
    price = models.IntegerField('Цена')
    Text = models.CharField('Описание манги',max_length=500,default="0")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/mangashop/{self.id}'


    class Meta:
        verbose_name = 'Манга'
        verbose_name_plural = 'Манга'
