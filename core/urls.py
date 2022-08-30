from django.urls import path

# APIS
from core.views import NameAPI, NameSearchAPI, CNPJAPI, CNPJSearchAPI, BuildRegisterAPI, BuildRegisterSearchAPI, BuildInfoAPI, BuildInfoSearchAPI

urlpatterns = [
    

    # API
    path("builds/", NameAPI.as_view()),
    path("cnpjs/", CNPJAPI.as_view()),

    path("build/<int:pk>/", NameSearchAPI.as_view()),
    path("cnpj/<int:pk>/", CNPJSearchAPI.as_view()),

    path("info/", BuildInfoAPI.as_view()),
    path("contact/", BuildRegisterAPI.as_view()),

    path("info/<int:pk>/", BuildInfoSearchAPI.as_view()),
    path("contact/<int:pk>/", BuildRegisterSearchAPI.as_view()),
]