from django.db import models

# Create your models here. Structure of the database of the order app.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    message = models.CharField(max_length=154)

    def __str__(self):
        return self.name
