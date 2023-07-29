from django.db import models
from django.contrib.auth.models import AbstractUser

class BaseModel(models.Model):
    
    class Meta:
        abstract = True

    #New subscriber date subscription made
    created_at = models.DateTimeField(auto_now_add=True)
    
    #When the infor was updated
    updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
class User(BaseModel,AbstractUser):
    pass
