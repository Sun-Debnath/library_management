from django.db import models
from category.models import Category
from django.contrib.auth.models import User
# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car/media/uploads/', blank = True, null = True)
    quantity = models.IntegerField(blank = True, null = True)
    
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"Comments by {self.name}"

class History(models.Model):
    name = models.CharField(max_length=50)
    books_id = models.IntegerField(blank = True, null = True)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE,blank = True, null = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='book/media/uploads/', blank = True, null = True)
    quantity = models.IntegerField(blank = True, null = True)

        
