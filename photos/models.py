from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)
    
    def __str__(self):
        return self.name
    
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    
class Location(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
    def save_location(self):
            self.save()

    def delete_location(self):
        self.delete()
    
    @classmethod
    def display_all_locations(cls):
        return cls.objects.all()
    
    
    
class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,blank=True)
    image =models.ImageField(null=False,blank=False)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True,blank=True)
    
    def __str__(self):
        return self.description   
    
    def save_image(self):
        self.save()
