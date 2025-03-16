from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


# Create your models here.
class Shoes(models.Model): 
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField(default=0)
    image = models.URLField(max_length=255)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, blank=True, related_name='shoes', null=True, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.name
    
    
class Review(models.Model): 
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200)
    shoes = models.ForeignKey(Shoes, on_delete=models.CASCADE, related_name='reviews')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self): 
        return str(self.rating) + " | " + self.shoes.name