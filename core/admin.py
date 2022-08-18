from django.contrib import admin

# Model Imports
from core.models import NameModel, CNPJModel, BuildRegisterModel, BuildInfoModel

@admin.register(NameModel)
class NameAdmin(admin.ModelAdmin):
    list_display = ("name", )


@admin.register(CNPJModel)
class CNPJAdmin(admin.ModelAdmin):
    list_display = ("CNPJ", )


@admin.register(BuildRegisterModel)
class BuildRegisterAdmin(admin.ModelAdmin):
    list_display = ("name", "CNPJ", "owner")


@admin.register(BuildInfoModel)
class BuildRegisterAdmin(admin.ModelAdmin):
    list_display = ("name", "CNPJ", "address", "email")