from django.contrib import admin
from .models import Character, Demon

# Убираем декораторы и регистрируем модели по-другому

class CharacterAdmin(admin.ModelAdmin):
    """Настройки админки для персонажей"""
    list_display = ['name', 'title', 'is_hashira', 'order', 'created_at']
    # list_display - это атрибут, который определяет, какие поля модели будут отображаться в списке объектов в админке. 
    # В данном случае, для модели Character будут отображаться поля name, title, is_hashira, order и created_at.
    list_filter = ['is_hashira', 'created_at']
    # list_filter - это атрибут, который добавляет боковую панель фильтров в админке, позволяя администратору быстро отфильтровать объекты по указанным полям.
    search_fields = ['name', 'description']
    # search_fields - это атрибут, который добавляет строку поиска в админке, позволяя администратору искать объекты по указанным полям. 
    # В данном случае, администратор сможет искать персонажей по имени и описанию.
    list_editable = ['order', 'is_hashira']
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'title', 'description', 'quote')
        }),
        ('Изображение', {
            'fields': ('image_url',)
        }),
        ('Характеристики', {
            'fields': ('ability', 'is_hashira', 'order')
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)  # Скрываем по умолчанию
        }),
    )
    readonly_fields = ['created_at', 'updated_at']

class DemonAdmin(admin.ModelAdmin):
    """Настройки админки для демонов"""
    list_display = ['name', 'rank', 'created_at']
    list_filter = ['rank', 'created_at']
    search_fields = ['name', 'description', 'blood_art']
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'rank', 'description', 'quote')
        }),
        ('Способности', {
            'fields': ('blood_art',)
        }),
        ('Изображение', {
            'fields': ('image_url',)
        }),
    )

# Регистрируем модели без декораторов
admin.site.register(Character, CharacterAdmin)
admin.site.register(Demon, DemonAdmin)