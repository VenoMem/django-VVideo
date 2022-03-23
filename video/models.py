from typing_extensions import Required
from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from django.urls import reverse

class Video(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/%Y/%m/%d', validators=[FileExtensionValidator(allowed_extensions=['mp4','mkv','avi','webm'])])
    description = models.TextField(max_length=400, blank=True)
    date_posted = models.DateTimeField(default=timezone.now(), editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("video:video_detail", kwargs={"pk": self.pk})