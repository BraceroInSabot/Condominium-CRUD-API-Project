from django.contrib import admin

# Model Imports
from core.models import NameModel, CNPJModel, CondominiumInfoModel

@admin.register(NameModel)
class NameAdmin(admin.ModelAdmin):
    list_display = ("name", )


@admin.register(CNPJModel)
class CNPJAdmin(admin.ModelAdmin):
    list_display = ("CNPJ", )


@admin.register(CondominiumInfoModel)
class CondominiumRegisterAdmin(admin.ModelAdmin):
    list_display = ("name", "CNPJ", "owner", "address", "email")