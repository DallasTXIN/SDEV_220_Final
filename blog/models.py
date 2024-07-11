from django.db import models


# Create your models here.



class Car(models.Model):
    make = models.CharField(max_length=100)
    year = models.IntegerField()
    model = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.year} {self.make} {self.model} - {self.engine}"
class Part(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}-{self.description}-{self.car}"