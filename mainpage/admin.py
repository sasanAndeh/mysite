from django.contrib import admin
from mainpage.models import personal_details
# Register your models here.


@admin.register(personal_details)
class personal_detailsAdmin(admin.ModelAdmin):
    '''Admin View for personal_details'''
    list_display = ('f_name','l_name')
    