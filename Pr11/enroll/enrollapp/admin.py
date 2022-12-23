from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(tasks)
class tasksAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('name', 'desc', 'remiander', )


@admin.register(taskdate)
class taskdateAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('taskname', 'date', )


@admin.register(taskhistory)
class taskhistoryAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('taskhis', )
