from django.contrib import admin
from myapp.models import *
# Register your models here.

admin.site.site_title = 'myapp页面'
admin.site.site_header = 'myapp'
# admin.site.register(Person)


@admin.register(Person)
class AdminPerson(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

    list_per_page = 10

    search_fields = ['first_name', 'last_name']