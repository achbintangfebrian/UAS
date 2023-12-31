from django.db import models


class Shop(models.Model):
    barang = models.CharField(max_length=200)
    publish = models.DateTimeField("tanggal beli")
    harga =  models.CharField(max_length=200)

    def __str__(self):
        return self.barang
