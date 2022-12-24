from symbol import return_stmt
from tabnanny import verbose
from django.db import models
from django.shortcuts import render

# Create your models here.

class Kategori(models.Model):
    nama = models.CharField(max_length=20)

    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name_plural = "kategori"

class Artikel(models.Model):
    nama = models.CharField(max_length=100, blank=True, null=True)
    judul = models.CharField(max_length=100) 
    body = models.TextField(blank=True, null=True)
    kategory = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.nama, self.judul)

    
    class Meta:
        ordering =['-date']
        verbose_name_plural = "Artikel"
# Create your models here.

class Resep(models.Model):
    title = models.CharField(max_length=1000)
    porsi = models.CharField(max_length=1000)
    kunci = models.CharField(max_length=1000)
    waktu = models.CharField(max_length=1000)
    tingkat = models.CharField(max_length=1000)

    def __str__(self):
        return "{} - {}".format(self.title, self.kunci)

