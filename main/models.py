from django.db import models
from django.utils import timezone

class Character(models.Model):
    """Модель для персонажей"""
    name = models.CharField('Имя', max_length=100)
    title = models.CharField('Титул', max_length=100, blank=True, null=True)
    image_url = models.URLField('URL изображения', max_length=500, blank=True, null=True)
    description = models.TextField('Описание')
    quote = models.CharField('Цитата', max_length=200, blank=True, null=True)
    ability = models.CharField('Способность', max_length=200, blank=True, null=True)
    is_hashira = models.BooleanField('Столп?', default=False)
    order = models.IntegerField('Порядок', default=0)
    # default=0 означает, что если при создании персонажа не пронумеровать, он будет 0. Это даст сортировать персонажей по порядку, а те, у которых порядок не написан, будут в конце списка.
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Персонаж'
        verbose_name_plural = 'Персонажи'
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

class Demon(models.Model):
    """Модель для демонов"""
    name = models.CharField('Имя', max_length=100)
    rank = models.CharField('Ранг', max_length=50, blank=True, null=True)
    image_url = models.URLField('URL изображения', max_length=500, blank=True, null=True)
    description = models.TextField('Описание', blank=True, null=True)
    blood_art = models.CharField('Кровавое искусство', max_length=200, blank=True, null=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    quote = models.CharField('Цитата', max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = 'Демон'
        verbose_name_plural = 'Демоны'

    def __str__(self):
        return self.name
