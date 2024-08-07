from django.db import models

# Create your models here.
class User(models.Model):
    account_type = [
        ("AD", "Admin"),
        ("ST", "Student"),
        ("IN", "Instructor"),
    ]
    user_id = models.BigAutoField(primary_key=True)
    email = models.EmailField(max_length=254)
    name = models.CharField(max_length=60)
    user_type = models.models.CharField(max_length=2, choices=account_type)
