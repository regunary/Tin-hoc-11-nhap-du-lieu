from django.db import models

# Create your models here.
class Musician(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(verbose_name="Họ", max_length=50)
    last_name = models.CharField(verbose_name="Tên", max_length=50)
    instrument = models.CharField(verbose_name="Nhạc cụ", max_length=100)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Song(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name="Tên bài hát", max_length=100)
    musician = models.ForeignKey(Musician, verbose_name="Nhạc sĩ", on_delete=models.CASCADE)
    release_date = models.DateField(verbose_name="Ngày phát hành")

    def __str__(self):
        return self.title