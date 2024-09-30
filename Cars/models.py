from django.db import models

# Create your models here.
    
class Car_details(models.Model):
    content = models.TextField()
    Car_Model = models.CharField(max_length=100, blank=False, null=False)
    car_Price = models.IntegerField(max_length=15, blank=False, null=False)
    car_photo=models.ImageField(upload_to='carPhoto/',null=True,blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    car_Name = models.CharField(max_length=100, blank=False, null=False )
    
    
