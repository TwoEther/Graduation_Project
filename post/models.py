from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    main_category = models.CharField(max_length=20, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'category'
        verbose_name_plural = 'Categories'
        
    def __str__(self): 
        return self.main_category

        
class Post(models.Model):
    pn = models.AutoField(db_column='PN', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateField(blank=True, null=True, auto_now_add = True)
    content = models.TextField(max_length=1000, blank=True, null=True)
    head_image = models.ImageField(upload_to="post/images/",blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, max_length=20, db_column='author')
    main_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, db_column='main_category')
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
    image = models.ImageField(upload_to="post/images/")

    class Meta:
        managed = False
        db_table = 'photo'
    
        
