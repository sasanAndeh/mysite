from django.contrib import admin
from mainpage.models import personal_details ,social_media_links
# Register your models here.


@admin.register(personal_details)
class personal_detailsAdmin(admin.ModelAdmin):
    '''Admin View for personal_details'''
    list_display = ('f_name','l_name')
    

@admin.register(social_media_links)
class personal_detailsAdmin(admin.ModelAdmin):
    '''Admin View for personal_details'''
    list_display = ('telegram',)
    