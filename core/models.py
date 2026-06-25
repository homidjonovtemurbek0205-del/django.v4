from django.db import models

# Create your models here.

# class Book(models.Model):

#     title = models.CharField(max_length=200)
#     price = models.IntegerField(default=0)
#     created_at = models.DateField(auto_now_add=True)
#     status = models.CharField('max_length=10', null=True)

        # def __str__(self):
        #     return self.nomi

class Mahsulot(models.Model):
    nomi = models.CharField(max_length=200)
    tavsifi = models.TextField(null=True, blank=True)
    narxi = models.DecimalField(max_digits=10, decimal_places=2)
    chegirmadagi_narxi = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ombordagi_soni = models.IntegerField(default=0)
    aktiv_holati = models.BooleanField(default=True)
    yaratilgan_vaqti = models.DateTimeField(auto_now_add=True)
    yangilangan_vaqti = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nomi