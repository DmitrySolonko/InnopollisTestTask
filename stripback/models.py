from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(verbose_name="Название", max_length=200)
    description = models.TextField(verbose_name="Описание")
    price = models.IntegerField(verbose_name="Цена")

    @property
    def calc_price(self):
        return self.price * 100

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = "Товары"
