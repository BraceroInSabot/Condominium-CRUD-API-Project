from django.db import models

class BuildNameModel(models.Model):
    name = models.CharField("Condominium name", max_length=100)


class BuildModel(models.Model):
    name = models.ForeignKey(LocationModel, on_delete=models.CASCADE())
    CNPJ = models.IntegerField("CNPJ", max_length=14)
    address = models.CharField("Adress of it", max_length=70)
    

    def __str__(self) -> str:
        return self.name
