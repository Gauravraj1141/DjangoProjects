from django.contrib import admin


from .models import User_Blog


@admin.register(User_Blog)
class User_BlogAdmin(admin.ModelAdmin):
    list_display = ('U_id', 'Title', 'Desc', 'Date', 'Author', )
