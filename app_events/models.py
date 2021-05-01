import uuid
from django.db import models


class Event(models.Model):
    slug = models.SlugField(unique=True, blank=False, null=False, editable=False, max_length=50)
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    number_of_participants = models.PositiveIntegerField(null=False, blank=False)

    def save(self, **kwargs):
        if not self.slug:
            self.slug = uuid.uuid4()
        super().save(**kwargs)
