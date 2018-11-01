from django.db import models

# Create your models here.
class Meal(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return self.name

class Order(models.Model):
    table_number = models.IntegerField()
    meals = models.ManyToManyField(Meal)

    #n@property
    def total_price(self):
        qs = self.meals.all().aggregate(total_price=models.Sum('price'))
        return qs['total_price']

    def __str__(self):
        return self.table_number