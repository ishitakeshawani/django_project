from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Enroll(models.Model):
    name = models.CharField(max_length=50)
    enno = models.TextField(max_length=12)
    sem = models.IntegerField()
    branch = models.CharField(max_length=8,null=True)
    subject1 = models.CharField(max_length=15,null=True)
    subject2 = models.CharField(max_length=15,null=True,blank=True)
    subject3 = models.CharField(max_length=15,null=True,blank=True)
    subject4 = models.CharField(max_length=15,null=True,blank=True)
    subject5 = models.CharField(max_length=15,null=True,blank=True)
    outofmidsub1 = models.IntegerField(null=True,blank=True)
    outofmidsub2 = models.IntegerField(null=True,blank=True)
    outofmidsub3 = models.IntegerField(null=True,blank=True)
    outofmidsub4 = models.IntegerField(null=True,blank=True)
    outofmidsub5 = models.IntegerField(null=True,blank=True)
    sub1mark = models.IntegerField(null=True,blank=True)
    sub2mark = models.IntegerField(null=True,blank=True)
    sub3mark = models.IntegerField(null=True,blank=True)
    sub4mark = models.IntegerField(null=True,blank=True)
    sub5mark = models.IntegerField(null=True,blank=True)
    remidsub1mark = models.IntegerField(null=True,blank=True)
    remidsub2mark = models.IntegerField(null=True,blank=True)
    remidsub3mark = models.IntegerField(null=True,blank=True)
    remidsub4mark = models.IntegerField(null=True,blank=True)
    remidsub5mark = models.IntegerField(null=True,blank=True)


    def __str__(self):
        return self.name
