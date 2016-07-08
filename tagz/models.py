from django.db import models

class Chunks(models.Model):
    text = models.CharField(max_length=10000, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

class Tagz(models.Model):
    text = models.CharField(max_length=255, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    chunks = models.ManyToManyField(Chunks, blank=True, null=True)

class User(models.Model):
    username = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=255, blank=True)
    date_created = models.DateField(auto_now_add=True)
    login_count = models.IntegerField(default=0)
    last_login = models.DateTimeField(blank=True, null=True)
    tagz = models.ManyToManyField(Tagz, blank=True, null=True)