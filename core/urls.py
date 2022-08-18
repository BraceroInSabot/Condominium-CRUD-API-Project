from django.urls import path, include

# Pages
from core.views import IndexView

# APIS
from core.views import BuildAPI, BuildNameAPI, BuildCNPJAPI

urlpatterns = [
    path("", IndexView.as_view(), name="index"),

    # API
    path("builds/", BuildAPI.as_view()),
    path("builds/<str:name>/", BuildNameAPI.as_view()),
    path("builds/<str:CNPJ>/", BuildCNPJAPI.as_view()),
]