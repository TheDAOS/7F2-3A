from django.db import models
from django.contrib.auth.models import User

class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_path = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    file_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.file_path} uploaded by {self.user.username}"
