from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Articles(models.Model):
    title = models.CharField('Название', max_length=50, default='ПУСТО')
    description = models.CharField('Краткое описание (кликбейт)', max_length=250, default='ПУСТО')
    image = models.CharField('Картинка', max_length=250, default='ПУСТО')
    text = models.TextField('Полное описание')
    date = models.DateField('Дата события')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
