from django.urls import path

# APIS
from core.views import NameAPI, NameSearchAPI, CNPJAPI, CNPJSearchAPI, CondominiumInfoAPI, CondominiumInfoSearchAPI

urlpatterns = [
    

    # API
    path("conds/", NameAPI.as_view()),
    path("cnpjs/", CNPJAPI.as_view()),

    path("cond/<int:pk>/", NameSearchAPI.as_view()),
    path("cnpj/<int:pk>/", CNPJSearchAPI.as_view()),

    path("infos/", CondominiumInfoAPI.as_view()),

    path("info/<int:pk>/", CondominiumInfoSearchAPI.as_view()),
]