from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, default='uncategorized')

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=200, unique=True, null=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Generate a slug format even if the user doesn't enter one
        slug = slugify(self.slug)
        # Check if a Post object with this slug already exists
        if Post.objects.filter(slug=slug).exists():
            # Add a numeric suffix until we find a unique slug
            suffix = 1
            while Post.objects.filter(slug=f"{slug}-{suffix}").exists():
                suffix += 1
            slug = f"{slug}-{suffix}" # return the slug with the suffix added, so that it is unique
        self.slug = slug
        super().save(*args, **kwargs) # Call the "real" save() method.

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})
