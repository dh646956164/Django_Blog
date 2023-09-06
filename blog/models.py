# Import necessary modules from Django
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create a Category model with a name attribute
class Category(models.Model):
    name = models.CharField(max_length=100)

    # Define a string representation of the model
    def __str__(self):
        return self.name

    # Define a method for getting the absolute URL for an instance of the model
    def get_absolute_url(self):
        return reverse('home', kwargs={'pk': self.pk})

# Create a Post model with attributes for title, content, date_posted, author, header_image, category, and views
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    header_image = models.ImageField(default='default.jpg', upload_to='header_pics')
    category = models.CharField(max_length=255, default='unassigned', null=True)
    views = models.IntegerField(default=0)

    # Define a string representation of the model
    def __str__(self):
        return self.title

    # Define a method for getting the absolute URL for an instance of the model
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

# Create a Comment model with attributes for post, name, body, and date_added
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # Define a string representation of the model
    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
