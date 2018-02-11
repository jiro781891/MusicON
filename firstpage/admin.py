from django.contrib import admin
from .models import *
# Register your models here.
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ["name", "email"] #ОТОБРАЖАЕТ ВСЕ ДАННЫЕ КОТОРЫЕ НАПИСАНИ В КВАДРАТНЫХ СКОБКАХ
    #list_display = [field.name for field in Subscriber.__meta__.fields] #ОТОБРАЖАЕТ ВСЕ ПОЛЯ ДАННЫХ
    #exclude = ["email"] #НЕ ОТОБРАЖАТЬ ЗАДАНЫЕ ДАННЫЕ
    #fields = ["email"] ОБРАТНОЕ EXLUCE ОТОБРАЖАЕТ ТОЛЬКО ЗАДАНЫЕ ДАННЫЕ
    #list_filter = ['name']  #ФИЛЬТР СПРАВОЙ СТОРОНЫ ПО NAME
    #search_fields = ["name"] #ДОБОВЛЯЕТ ПОИСК ПО  NAME


admin.site.register(Subscriber)
