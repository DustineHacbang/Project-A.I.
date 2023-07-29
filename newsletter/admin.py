from django.contrib import admin
from newsletter.models import NewsletterPost, NewsletterEmail, NewsletterSubscriber
# Register your models here.

@admin.register(NewsletterPost)
class NewsletterPostAdmin(admin.ModelAdmin):
    pass

@admin.register(NewsletterEmail)
class NewsletterEmailAdmin(admin.ModelAdmin):
    pass

@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    pass