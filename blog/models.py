from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(delfault=timezone.now ,auto_now=False, auto_now_add=False)
    created = models.DateTimeField(auto_now_=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now_=True, auto_now_add=False)
    status = models.CharField(max_length=2,choises=Status.choices, default=Status.DRAFT)
    class Meta():
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish'])]
    def __str__(self):
        return self.title
    
