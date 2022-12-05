from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User


class Category1(models.Model):
    category = models.CharField(max_length=20)
    class Meta:
        managed = False
        db_table = 'category1'
        verbose_name_plural = 'Categories1'
        
    def __str__(self): 
        return self.category
    
class Category2(models.Model):
    category = models.CharField(max_length=20)
    class Meta:
        managed = False
        db_table = 'category2'
        verbose_name_plural = 'Categories2'
        
    def __str__(self): 
        return self.category

    
class Post(models.Model):
    pn = models.AutoField(db_column='PN', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateField(blank=True, null=True, auto_now_add = True)
    content = models.TextField(max_length=1000, blank=True, null=True)
    head_image = models.ImageField(upload_to="post/images/%Y/%m/%d",blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, max_length=20, db_column='author')
    category1 = models.ForeignKey(Category1, on_delete=models.CASCADE, null=True, db_column='category1')
    category2 = models.ForeignKey(Category2, on_delete=models.CASCADE, null=True, db_column='category2')
    # sub_category = models.CharField(max_length=20, blank=True, null=True)  보류

    class Meta:
        managed = False
        db_table = 'post'
        
    def __str__ (self):
        return self.title
    
    def get_absolute_url(self):
        return f'{self.pk}/'

    def get_image_url(self):
        return self.head_image[:].decode()


class Photo(models.Model):
    postnum = models.ForeignKey('Post', models.CASCADE, db_column='postnum', blank=True)
    image = models.ImageField(upload_to="post/images/%Y/%m/%d")

    class Meta:
        managed = False
        db_table = 'photo'
        
class Comment(models.Model):
    postnum = models.ForeignKey(Post, models.CASCADE, db_column='postnum')
    author = models.ForeignKey(User, models.CASCADE, db_column='author')
    content = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'comment'
    
        
