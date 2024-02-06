from django.conf import settings
from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=256) 
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def save(self, *args, **kwargs):
    
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    artwork = models.ForeignKey('Artwork', on_delete=models.CASCADE)
    county = models.CharField(max_length=20)
    address = models.CharField(max_length=40)
    phone = models.CharField(max_length=20)
    order_date = models.DateTimeField(auto_now_add=True)
    payment = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"Order #{self.id} by {self.user.email} for {self.artwork.title} on {self.order_date}"

class Artwork(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    image = models.ImageField(upload_to='art_photos/')
    description = models.TextField()
    availability = models.CharField(max_length=20)

    def __str__(self):
        return self.title