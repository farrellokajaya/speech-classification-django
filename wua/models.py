from django.db import models

# Create your models here.

class divisi(models.Model):
    name = models.CharField(max_length=220)
    def __str__(self):
        return self.name
    
class tanggal(models.Model):
    date1 = models.DateField(null=True)
    date2 = models.DateField(null=True)
    def __str__(self):
        return self.date1, self.date2

class activity(models.Model):
    aktif = models.IntegerField()
    deadwood = models.IntegerField()
    def __str__(self):
        return self.aktif, self.deadwood