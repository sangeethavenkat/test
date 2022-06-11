from django.db import models

class manager(models.Model):
    name=models.CharField(max_length=100,null=True)
    username=models.CharField(max_length=100,default='Null',unique=True)
    email=models.EmailField(max_length=100,null=True)
    contact=models.BigIntegerField(null=True)
    password=models.CharField(max_length=100,null=True)
    objects: models.Manager()

class accesstl(models.Model):
    name=models.CharField(max_length=100,null=True)
    username=models.CharField(max_length=100,default='Null',unique=True)
    email=models.EmailField(max_length=100,null=True)
    contact=models.BigIntegerField(null=True)
    password=models.CharField(max_length=100,null=True)
    platform=models.CharField(max_length=100,null=True)
    approved=models.BooleanField(default=False)
    objects: models.Manager()

class resources(models.Model):
    tlname=models.CharField(max_length=100,null=True)
    pmname=models.CharField(max_length=100,null=True)
    resourcename = models.CharField(max_length=100,null=True)
    need = models.CharField(max_length=100,null=True)
    projectname=models.CharField(max_length=100,null=True)
    onoroff = models.CharField(max_length=100,null=True)
    duedays = models.CharField(max_length=100,null=True)
    status=models.CharField(max_length=50,default='Null')
    priority=models.CharField(max_length=100,default=" ")
    allocatestatus=models.CharField(max_length=100,default='pending')
    sent=models.BooleanField(default=False)
    objects: models.Manager()



