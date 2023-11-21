from django.shortcuts import render
from .models import Articles


def image_url_fixer(image_url):
    image_url = 'https://drive.google.com/uc?export=view&id=' + image_url.split('/')[5]
    return image_url


def main_page(request):
    return render(request, 'sitik/main.html')


def news_page(request):
    news = Articles.objects.order_by('date')
    for el in news:
        el.image = image_url_fixer(el.image)
    return render(request, 'sitik/news.html', {'news': news})


def contacts_page(request):
    return render(request, 'sitik/contacts.html')


def news_detail(request, news_id):
    single_new = Articles.objects.get(id=news_id)
    single_new.image = image_url_fixer(single_new.image)
    return render(request, 'sitik/news_detail.html', {'single_new': single_new})
