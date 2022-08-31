from django.db import models


class CNPJModel(models.Model):
    CNPJ = models.IntegerField("CNPJ", unique=True, help_text="Insert a valid brazilian CNPJ model with 14 numbers.")

    def __str__(self) -> str:
        return str(self.CNPJ)

    class Meta:
        verbose_name = "CONDOMINIUM CNPJ"
        verbose_name_plural = "CONDOMINIUMS CNPJ"


class NameModel(models.Model):
    name = models.CharField("Condominium name", max_length=100, help_text="Insert the condominium name.")
    CNPJ = models.ForeignKey(CNPJModel, on_delete=models.CASCADE, verbose_name="CNPJ", help_text="Match the condominium name with his CNPJ.")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "CONDOMINIUM NAME"
        verbose_name_plural = "CONDOMINIUM NAMES"


class CondominiumInfoModel(models.Model):
    name = models.ForeignKey(NameModel, on_delete=models.CASCADE)
    CNPJ = models.ForeignKey(CNPJModel, verbose_name="CNPJ", on_delete=models.CASCADE)
    address = models.CharField("Adress", max_length=70)
    email = models.EmailField("Email")
    owner = models.CharField("Owner", max_length=50)

    def __str__(self) -> str:
        return f"{self.name} - {self.CNPJ}"

    class Meta:
        verbose_name = "CONDOMINIUM CONTACT INFO"
        verbose_name_plural = "CONDOMINIUM CONTACT INFOS"
