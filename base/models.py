from django.db import models


class Meal(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    type = models.CharField(
        max_length=7,
        choices=[
            ('food', 'food'),
            ('drink', 'drink'),
            ('alcohol', 'alcohol'),
            ('extra', 'extra'),
            ]
        )

    def __str__(self):
        return self.name


class Cart(models.Model):
    name = models.CharField(null=True, max_length=200)
    amount = models.PositiveIntegerField()
    cost = models.FloatField()

    def __str__(self):
        return self.name


class Order(models.Model):
    meals = models.JSONField(default=dict)
    costs = models.FloatField()
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return "Order #"+str(self.id)
# Create your models here.
