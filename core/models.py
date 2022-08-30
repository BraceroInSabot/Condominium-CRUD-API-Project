from django.db import models

class NameModel(models.Model):
    name = models.CharField("Condominium name", max_length=100)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = " BUILD NAME"
        verbose_name_plural = " BUILDS NAMES"

class CNPJModel(models.Model):
    CNPJ = models.IntegerField("CNPJ")

    def __str__(self) -> str:
        return str(self.CNPJ)

    class Meta:
        verbose_name = " BUILD CNPJ"
        verbose_name_plural = " BUILDS CNPJ"


class BuildRegisterModel(models.Model):
    name = models.ForeignKey(NameModel, on_delete=models.CASCADE)
    CNPJ = models.ForeignKey(CNPJModel, verbose_name="CNPJ", on_delete=models.CASCADE)
    owner = models.CharField("Owner", max_length=50)
    
    def __str__(self) -> str:
        return f"{self.name} - {self.CNPJ}"

    class Meta:
        verbose_name = " BUILD REGISTER INFO"
        verbose_name_plural = " BUILDS REGISTER INFOS"

class BuildInfoModel(models.Model):
    name = models.ForeignKey(NameModel, on_delete=models.CASCADE)
    CNPJ = models.ForeignKey(CNPJModel, verbose_name="CNPJ", on_delete=models.CASCADE)
    address = models.CharField("Adress", max_length=70)
    email = models.EmailField("Email")

    
    class Meta:
        verbose_name = " BUILD CONTACT INFO"
        verbose_name_plural = " BUILDS CONTACT INFOS"
