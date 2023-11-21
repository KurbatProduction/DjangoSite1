from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('news/', views.news_page, name='news_page'),
    path('contacts/', views.contacts_page, name='contacts_page'),
    path('news/<int:news_id>', views.news_detail, name='news_detail')
]
