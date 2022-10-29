from django.db import models

# Create your models here.

class tugas4(models.Model):
    divisi = models.CharField(max_length=220)
    date1 = models.DateField(null=True)
    date2 = models.DateField(null=True)
    aktif = models.IntegerField()
    deadwood = models.IntegerField()
    
    def __str__(self):
        return "{}-{}".format(self.divisi, self.date1, self.date2, self.aktif, self.deadwood)