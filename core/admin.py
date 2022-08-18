from django.contrib import admin

# Model Imports
from core.models import BuildCNPJModel, BuildNameModel, BuildModel

@admin.register(BuildNameModel)
class BuildNameAdmin(admin.ModelAdmin):
    list_display = ("name", )


@admin.register(BuildCNPJModel)
class BuildCNPJAdmin(admin.ModelAdmin):
    list_display = ("name", "CNPJ")


@admin.register(BuildModel)
class BuildNameAdmin(admin.ModelAdmin):
    list_display = ("name_CNPJ", "address")