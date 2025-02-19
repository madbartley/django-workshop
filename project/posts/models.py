from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    slug = models.SlugField()

    # Adding a Post class method that returns the title of a post
    def __str__(self):
        return self.title