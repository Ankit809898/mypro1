from django.db import models


class Email(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=1000)
    attach = models.FileField()
    message = models.CharField(max_length=1000)
