from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import JSONField
from django.core.validators import FileExtensionValidator
from django.db import models

class RawVideo(models.Model):
    file = models.FileField(validators=[FileExtensionValidator(allowed_extensions = ['avi', 'mp4'])])

class Video(models.Model):
    user = models.ForeignKey(get_user_model(), blank=True, null=True, on_delete=models.CASCADE)
    labels = models.ImageField()
    metadata = JSONField()
    thumbnail = models.ImageField()