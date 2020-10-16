from django.conf import settings
from django.db import models
from django.utils import timezone

class Jugdments(models.Model):
    title = models.TextField()
    keyword = models.TextField()
    count = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class UploadPdf(models.Model):
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)