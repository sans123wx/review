from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ("title" , "review_date" , "create_date" , 'days_between')


