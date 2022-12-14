from django.contrib import admin
from .models import Myblog

# Register your models here.


@admin.register(Myblog)
class MyblogAdmin(admin.ModelAdmin):
    '''Admin View for '''
    list_display = ('title', 'desc', )
