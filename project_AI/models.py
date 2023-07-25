from django.db import models
from django.contrib.auth.models import AbstractUser

class BaseModel(models.Model):
    
    #New subscriber date subscription made
    created_at = models.DateTimeField(auto_now_add=True)
    
    #When the infor was updated
    updated_at = models.DateTimeField(auto_now=True)

class User(BaseModel,AbstractUser):
    pass

class NewsletterPost(BaseModel):
    #Newsletter post name
    title = models.CharField(max_length=255)
    #Main Body of article
    body = models.TextField()

class NewsletterSubscriber(BaseModel):
    #user foreignKey  utilised to pull user data from user model
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    #stating if user is active or not
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.user.email

class NewsletterEmail(BaseModel):
    
    #Newsletter post name
    title = models.CharField(max_length=255)

    #Main Body of article
    body = models.TextField()

    # The description of the newsletter
    description = models.TextField()

