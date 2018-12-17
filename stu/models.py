from django.db import models

# Create your models here.
class Clazz(models.Model):
    cno = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=30)

    def __str__(self):
        return 'cname:{}'.format(self.cname)


class Student(models.Model):
    sno = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=20)
    clazz = models.ForeignKey(Clazz)
    def __str__(self):
        return 'sname:{}'.format(self.sname)
