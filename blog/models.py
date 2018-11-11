from django.db import models
from django.utils import timezone

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    date_published = models.DateTimeField(blank=True, null=True)    

    def publish(self):
        self.date_published = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Categorie(models.Model):
    categorie = models.CharField(max_length=30)

    def __str__(self):
        return self.categorie

class Post(models.Model):
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    blog_id = models.ForeignKey('Blog', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_published = models.DateTimeField(blank=True, null=True)
    image = models.CharField(max_length=250)    
    categories = models.ManyToManyField(Categorie)

    def publish(self):
        self.date_published = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=100)    
    post_id = models.ForeignKey('Post', on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    comment = models.TextField()
    email = models.CharField(max_length=100)
       

    def __str__(self):
        return self.comment

class CategoriePost(models.Model):
    categorie_id = models.ForeignKey('Categorie', on_delete=models.CASCADE)
    post_id = models.ForeignKey('Post', on_delete=models.CASCADE)

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    question = models.TextField()

    def __str__(self):
        return self.email