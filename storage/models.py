from django.db import models
from django.conf import settings

class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	title = models.CharField(max_length=30)
	body = models.TextField()
  
class Image(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	image = models.ImageField(upload_to="images")
	desc = models.CharField(max_length=100)

class File(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	files = models.FileField(blank=False, null=False, upload_to="files")
	desc = models.CharField(max_length=100)