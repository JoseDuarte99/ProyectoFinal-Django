from django.db import models
from django.utils import timezone
from PIL import Image
# Create your models here.


#Category
class Category(models.Model):
    name = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.name

#Post
class Post(models.Model):
    title = models.CharField(max_length=50, null=False)
    subtitle = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(null=False)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, default='Uncategorized')
    image = models.ImageField(null=True, blank=True, upload_to='media', default='media/post_default.jpg')
    published = models.DateTimeField(default=timezone.now)

    class Meta():
        ordering = ('-published',)
    
    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        self.image.delete(save=False)  # Elimina la imagen del sistema de archivos
        super().delete(using=using, keep_parents=keep_parents)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            if img.height > 520 or img.width > 450:
                output_size = (520, 450)
                img.thumbnail(output_size)
                img.save(self.image.path)

# Comment
class Comment(models.Model):
    text = models.TextField(null=False)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.text

# Tag
class Tag(models.Model):
    name = models.CharField(max_length=30, null=True)
    post = models.ManyToManyField(Post)

    def __str__(self):
        return self.name


