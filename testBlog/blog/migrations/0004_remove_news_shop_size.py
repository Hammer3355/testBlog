# Generated by Django 4.2 on 2024-04-22 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_news_shop_size_news_views_alter_news_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='shop_size',
        ),
    ]
