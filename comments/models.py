from django.db import models
from elements.models import Element
# Create your models here.

class Comment (models.Model):

    text = models.TextField()
    date_posted = models.DateTimeField(auto_now=True)
    elements = models.ForeignKey(Element, on_delete = models.CASCADE, null= True)

    def __str__(self) -> str:
        return f'Comment #{self.id}'
