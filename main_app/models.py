from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Controller(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('controller_detail', kwargs={'pk': self.id })

    def __str__(self):
        return f"A {self.color} {self.name}"


class Platform(models.Model):
  name = models.CharField(max_length=50)
  release_year = models.IntegerField()
  controllers = models.ManyToManyField(Controller)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
      return self.name
  
  def get_absolute_url(self):
    return reverse('platform_detail', kwargs={'platform_id': self.id})

class Game(models.Model):
  name = models.CharField(max_length=100)
  release_date = models.IntegerField()
  platform = models.ForeignKey(Platform, on_delete=models.CASCADE)

  def __str__(self):
      return self.name


class Photo(models.Model):
    url = models.CharField(max_length=200)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for platform_id: {self.platform_id} @{self.url}"