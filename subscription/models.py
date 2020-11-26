from django.db import models

# Create your models here.


class Length(models.Model):
    name = models.CharField(max_length=10)
    length = models.DecimalField(max_digits=2, decimal_places=0)

    def __str__(self):
        return self.name


class Box(models.Model):

    class Meta:
        verbose_name_plural = 'Boxes'

    length = models.ForeignKey('Length', on_delete=models.PROTECT)
    name = models.CharField(max_length=254)
    image = models.ImageField(upload_to='images', null=False, blank=False)
    about = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    month_price_1 = models.DecimalField(max_digits=6, decimal_places=2)
    month_price_2 = models.DecimalField(max_digits=6, decimal_places=2)
    month_price_3 = models.DecimalField(max_digits=6, decimal_places=2)

    image_url = models.URLField(max_length=1024, null=False, blank=False)

    def __str__(self):
        return self.name



