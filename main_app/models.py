# Create your models here.
from django.db import models
from django.urls import reverse


# Create your models here.
class CarPost(models.Model):
    title = models.CharField(max_length=50)
    make = models.CharField(max_length=50)
    carModel = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    year = models.IntegerField()
    body = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})


class Comment(models.Model):
    commentBody = models.CharField(max_length=250)
    car = models.ForeignKey(CarPost, on_delete=models.CASCADE)

    def __str__(self):
        return self.commentBody

    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})

class Photo(models.Model):
    url = models.CharField(max_length=200)
    car = models.ForeignKey(CarPost, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for car_id: {self.car_id} @{self.url}"