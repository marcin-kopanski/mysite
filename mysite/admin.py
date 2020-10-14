from django.contrib import admin


class MyAdminSite(admin.AdminSite):
    index_title = "index_title"
    site_title = "site_title"
    site_header = "site_header"
