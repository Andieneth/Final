# Generated by Django 4.2 on 2023-05-27 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangashop', '0008_articlesshop_order_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlesshop',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
