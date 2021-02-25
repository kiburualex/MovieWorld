from datetime import date
from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now, null=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    class Meta:
        abstract = True


class Movie(BaseModel):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    recommendation = models.CharField(max_length=200, null=True, blank=True)
    rating = models.CharField(max_length=200, null=True, blank=True) # 1-5
    type = models.CharField(max_length=200, null=True, blank=True) # movie or series
    is_watched = models.BooleanField(default=False)

    def __str__(self):
        return f"id={self.id}, title={self.title}, description={self.description}"
