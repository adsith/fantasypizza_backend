from django.db import models

class IngredientType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Ingredients(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    type = models.ForeignKey(IngredientType, on_delete=models.DO_NOTHING)
    
    def __str__(self) -> str:
        return self.name
