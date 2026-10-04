from django.db import models
class Dealer(models.Model):
    name=models.CharField(max_length=160)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=80)
    address=models.CharField(max_length=255,blank=True)
    def __str__(self): return self.name
class Review(models.Model):
    dealer=models.ForeignKey(Dealer,related_name="reviews",on_delete=models.CASCADE)
    name=models.CharField(max_length=120)
    review=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
class CarMake(models.Model):
    name=models.CharField(max_length=100,unique=True)
    def __str__(self): return self.name
class CarModel(models.Model):
    make=models.ForeignKey(CarMake,related_name="models",on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    year=models.PositiveIntegerField(default=2024)
