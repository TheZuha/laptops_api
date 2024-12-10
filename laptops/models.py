from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='brand_logos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Laptop(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.DateField()
    cpu = models.CharField(max_length=100)
    ram = models.CharField(max_length=50)
    memory = models.CharField(max_length=100)
    gpu = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=
    True)
    REQUIRED_FIELDS = ['email']


class Feedback(models.Model):
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.laptop.name
