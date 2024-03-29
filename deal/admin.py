from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from deal.models import  Deal ,Account


# Register your models here.


class AccountAdmin (UserAdmin):
    list_display =('email' ,'username' ,'date_joined','last_login','is_active','is_admin')
    search_fields =('email' ,'username')
    readonly_fields=('date_joined','last_login')
    filter_horizontal=()
    list_filter=()
    fieldsets=()

# admin.site.register(User_Profile)
admin.site.register(Deal)
admin.site.register(Account,AccountAdmin)
