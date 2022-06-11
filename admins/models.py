from django.db import models

class access(models.Model):
    name=models.CharField(max_length=100,null=True)
    username=models.CharField(max_length=100,default='Null',unique=True)
    email=models.EmailField(max_length=100,null=True)
    contact=models.BigIntegerField(null=True)
    jobtitle=models.CharField(max_length=100,null=True)
    password=models.CharField(max_length=100,null=True)
    objects: models.Manager()



class adminpm(models.Model):
    name = models.CharField(max_length=100,null=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100,null=True)
    contact = models.BigIntegerField(null=True)
    jobtitle = models.CharField(max_length=100,null=True)
    password = models.CharField(max_length=100,null=True)
    approve=models.BooleanField(default=False)
    objects: models.Manager()