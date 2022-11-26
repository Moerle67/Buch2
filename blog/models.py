from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
            .filter(status=Post.Status.PUBLISHED)
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='puplish')
    author = models.ForeignKey(User, related_name=("blog_posts"), on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now ,auto_now=False, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    status = models.CharField(max_length=2,choices=Status.choices, default=Status.DRAFT)
    objects = models.Manager()
    published = PublishedManager()
    class Meta():
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish'])]
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.id])
    
    
