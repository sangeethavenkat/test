from django.db import models


class tl(models.Model):
    name = models.CharField(max_length=100,null=True)
    username = models.CharField(max_length=100, default='Null', unique=True)
    email = models.EmailField(max_length=100,null=True)
    contact = models.BigIntegerField(null=True)
    password = models.CharField(max_length=100,null=True)
    objects: models.Manager()

class allocation(models.Model):
    employeename=models.CharField(max_length=100,null=True)
    work=models.CharField(max_length=100,null=True)
    duedays =models.IntegerField(null=True)
    workstatus=models.CharField(max_length=200,null=True)
    status=models.CharField(max_length=100,default='pending')
    objects: models.Manager()




