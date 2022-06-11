from django.db import models


class emp(models.Model):
    name = models.CharField(max_length=100,null=True)
    username = models.CharField(max_length=100, default='Null', unique=True)
    email = models.EmailField(max_length=100,null=True)
    contact = models.BigIntegerField(null=True)
    team=models.CharField(max_length=100,null=True)
    status=models.CharField(max_length=100,null=True)
    password = models.CharField(max_length=100,null=True)
    upload=models.FileField(null=True,default='Null')
    empid=models.IntegerField(null=True,unique=True)
    send=models.BooleanField(default=False)
    project=models.CharField(max_length=100,null=True)
    tl=models.CharField(max_length=100,null=True)
    objects: models.Manager()

