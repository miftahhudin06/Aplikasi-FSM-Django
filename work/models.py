import datetime
from io import BytesIO
from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from work.managers import CustomUserManager
from django.utils import timezone
from django.core.files import File
# Create your models here.


class Karyawan(AbstractUser):
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField('is_admin', default=False)
    is_teknisi = models.BooleanField('is_teknisi', default=False)
    foto = models.ImageField(upload_to='profil_images', blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.foto.path)
        if img.height > 160 or img.width > 160:
            new_img = (160, 160)
            img.thumbnail(new_img, Image.ANTIALIAS)
            img.save(self.foto.path, "JPEG")

    def __str__(self):
        return self.first_name + " " + self.last_name


class Gedung(models.Model):
    namaGedung = models.CharField(max_length=100)
    pengelola = models.CharField(max_length=100)

    def __str__(self):
        return self.namaGedung


class TipeGondola(models.Model):
    gedung = models.ForeignKey(Gedung, on_delete=models.CASCADE)
    tower = models.CharField(max_length=100)
    tipe = models.CharField(max_length=100)

    def __str__(self):
        return self.gedung.namaGedung + " Tower " + self.tower


class BAK(models.Model):
    gondola = models.ForeignKey(TipeGondola, on_delete=models.CASCADE)
    tgl = models.DateField(null=True)
    sparepart = models.CharField(max_length=100)
    spesifikasi = models.CharField(max_length=200)
    teknisiSatu = models.ForeignKey(Karyawan, on_delete=models.CASCADE, null=True,
                                    related_name='teknisi1', limit_choices_to={'is_teknisi': True})
    teknisiDua = models.ForeignKey(Karyawan, on_delete=models.CASCADE, null=True,
                                   related_name='teknisi2', limit_choices_to={'is_teknisi': True})
    qty = models.CharField(max_length=100)
    analisa = models.CharField(max_length=100)
    solusi = models.CharField(max_length=100)
    fotoKerusakan = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.gondola


class Note(models.Model):
    gedung = models.ForeignKey(Gedung, on_delete=models.CASCADE)
    picSatu = models.ForeignKey(Karyawan, on_delete=models.CASCADE, null=True,
                                related_name='pic1', limit_choices_to={'is_teknisi': True})
    picDua = models.ForeignKey(Karyawan, on_delete=models.CASCADE, null=True,
                               related_name='pic2', limit_choices_to={'is_teknisi': True})
    bulan = models.CharField(max_length=100, null=True, blank=True)
    tgl = models.DateField(null=True, blank=True)
    tipeGondola = models.ForeignKey(
        TipeGondola, on_delete=models.CASCADE, null=True)
    service = models.CharField(max_length=20)
    catatan = models.CharField(max_length=1000)
    fotoKerusakan = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=50)

    def _str_(self):
        return self.tipeGondola


class Jadwal(models.Model):
    tgl = models.DateField(null=True)
    gedung = models.ForeignKey(Gedung, on_delete=models.CASCADE)
    teknisiSatu = models.ForeignKey(Karyawan, on_delete=models.CASCADE, null=True,
                                    related_name='pekerja1', limit_choices_to={'is_teknisi': True})
    teknisiDua = models.ForeignKey(Karyawan, on_delete=models.CASCADE, null=True,
                                   related_name='pekerja2', limit_choices_to={'is_teknisi': True})
    pekerjaan = models.CharField(max_length=200)
    hasilPekerjaan = models.CharField(max_length=100, blank=True, null=True)
    catatanKhusus = models.CharField(max_length=100, blank=True, null=True)

    def _str_(self):
        return self.tgl
