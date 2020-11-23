from django.db import models

# Create your models here.


class Box(models.Model):

    class Meta:
        verbose_name_plural = 'Boxes'

    name = models.CharField(max_length=254)
    image = models.ImageField(null=False, blank=False)
    time = models.DecimalField(max_digits=2, decimal_places=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=False, blank=False)

    def __str__(self):
        return self.name
