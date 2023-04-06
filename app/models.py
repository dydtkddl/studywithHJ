from django.db import models

# Create your models here.
class User(models.Model):
    user_id= models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=100, null=True)
    phone = models.IntegerField(null=True)
    
class Article(models.Model):
    user = models.ForeignKey(User, null = True, on_delete= models.CASCADE)
    title = models.CharField(max_length=2000, null=True)
    content = models.TextField(null=True)
    date = models.CharField(max_length=100,null=True)

class Comment(models.Model):
    article = models.ForeignKey(Article, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null = True, on_delete= models.CASCADE)
    comment = models.TextField(null=True)

