from django.contrib import admin
# from django.contrib.admin import AdminSite
from .models import (
    Question,
    Choice
)


# class ApplicationAdminSite(AdminSite):
#     site_header = 'Тестовое приложение опросов'
#
#
# app_admin = ApplicationAdminSite(name="application_admin")
# app_admin.register(Question)
# app_admin.register(Choice)

admin.site.register(Question)
admin.site.register(Choice)