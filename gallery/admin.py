from django.contrib import admin
from .models import Order,Artwork,User

# Register your models here.
admin.site.register(Order)
admin.site.register(User)
admin.site.register(Artwork)
