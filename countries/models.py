from django.db import models

# Create your models here.


class Supplier(models.Model):

    name = models.CharField(max_length=254)
    email = models.CharField(max_length=254)


class Country(models.Model):

    class Meta:
        verbose_name_plural = 'Countries'

    name = models.CharField(max_length=254)
    Supplier.country = models.ForeignKey('Supplier', null=True, unique=True, blank=True, on_delete=models.SET_NULL)
    about = models.CharField(max_length=500, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to='countries', null=True, blank=True)

    def __str__(self):
        return self.name
