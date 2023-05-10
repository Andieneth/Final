# Generated by Django 4.1.5 on 2023-04-26 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Безымянная новость -_-', max_length=50, verbose_name='Название новости')),
                ('anons', models.CharField(default='А анонса то нет', max_length=250, verbose_name='Текст анонса')),
                ('full_text', models.TextField(verbose_name='Статья')),
                ('date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
        ),
    ]
