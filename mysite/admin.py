from django.contrib import admin


class MyAdminSite(admin.AdminSite):
    site_header = 'Customized administration'
