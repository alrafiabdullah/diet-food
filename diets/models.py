from django.db import models
from django.contrib.postgres.fields import ArrayField

from accounts.models import User


# Create your models here.
class ImageAlbum(models.Model):
    name = models.CharField(max_length=500, unique=True)

    def __str__(self):
        return self.name


class ImageCDN(models.Model):
    album = models.ForeignKey(
        ImageAlbum, related_name="images", on_delete=models.CASCADE)
    file_id = models.CharField(max_length=100)
    name = models.CharField(max_length=500)
    url = models.URLField(
        default="https://ik.imagekit.io/alrafiabdullah/default-image.jpg")
    thumbnail = models.URLField(
        default="https://ik.imagekit.io/alrafiabdullah/default-image.jpg")
    file_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Nutrition(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ingredients = models.JSONField(null=True)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=250, default="")
    photo = models.OneToOneField(ImageAlbum, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    calorie_count = models.PositiveIntegerField(default=0)
    nutritions = models.OneToOneField(Nutrition, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=500, default="")
    description = models.TextField(max_length=9999, default="")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    foods = models.ManyToManyField(Food, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Custom(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=500, default="")
    description = models.TextField(max_length=9999, default="")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    foods = models.ManyToManyField(Food, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
