from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'first_name', 'last_name', 'mobile_no', 'image']
    
    def first_name(self, obj):
        return obj.user.first_name
    
    def last_name(self, obj):
        return obj.user.last_name
    
    first_name.admin_order_field = 'user__first_name'
    last_name.admin_order_field = 'user__last_name'

admin.site.register(Profile, ProfileAdmin)
