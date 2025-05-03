from django.db import models


class magasin(models.Model):
    id_magasin = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class client(models.Model):
    id_client = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name


class centre_social(models.Model):
    id_centre_social = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class beneficiaire(models.Model):
    id_beneficiaire = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name


class article(models.Model):
    name = models.CharField(max_length=50)
    code_barre = models.BigIntegerField(primary_key=True)
    qte_suspendus = models.IntegerField()
    qte_disponible = models.IntegerField()

    def __str__(self):
        return self.name


class panier(models.Model):
    id_panier = models.BigIntegerField(primary_key=True)
    retire = models.BooleanField(default=False)
    complet = models.BooleanField(default=False)

    def __str__(self):
        return self.id_panier
