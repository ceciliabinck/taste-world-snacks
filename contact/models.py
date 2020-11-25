from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    message = models.CharField(max_length=154)

    def __str__(self):
        return self.name
