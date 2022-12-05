from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField

class Profile(models.Model):
    user = models.OneToOneField(User, null= True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    
    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("home")


class Post(models.Model):
    title = models.CharField(max_length=100)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    sub_title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="blog_posts")
    
    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse("home")

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE) 
    name = models.CharField(max_length=100)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s - %s" % (self.post.title, self.name)

