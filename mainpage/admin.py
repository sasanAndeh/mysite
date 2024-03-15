from django.contrib import admin
from mainpage.models import personal_details ,social_media_links , resume ,skills ,set_user
# Register your models here.


@admin.register(personal_details)
class personal_detailsAdmin(admin.ModelAdmin):
    '''Admin View for personal_details'''
    list_display = ('f_name','l_name')

@admin.register(set_user)
class personal_detailsAdmin(admin.ModelAdmin):
    '''Admin View for personal_details'''
    list_display = ('user',)
    def has_add_permission(self, request, obj=None):
        return False

    

@admin.register(social_media_links)
class personal_detailsAdmin(admin.ModelAdmin):
    '''Admin View for personal_details'''
    list_display = ('telegram',)
    
@admin.register(resume)
class personal_detailsAdmin(admin.ModelAdmin):
    '''Admin View for personal_details'''
    list_display = ('User',)
    
    
@admin.register(skills)
class personal_detailsAdmin(admin.ModelAdmin):
    '''Admin View for personal_details'''
    
    list_display = (
        'User',
        'skill',
        'percent',
        'percentage_skill',
    )