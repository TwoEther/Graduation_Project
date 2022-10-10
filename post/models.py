from django.db import models

# Create your models here.
class User(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    passwd = models.CharField(max_length=20, blank=True, null=True)
    nickname = models.CharField(unique=True, max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'

class Category(models.Model):
    name = models.CharField(primary_key=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'category'
        
        # 리뷰 작성 페이지 + 카테고리
        # 로그인 회원가입
        # 장고 검색 기능
        
class Post(models.Model):
    pn = models.AutoField(db_column='PN', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateField(blank=True, null=True, auto_now_add=True)
    content = models.CharField(max_length=1000, blank=True, null=True)
    head_image = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='category', blank=True, null=True)
    author = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='author', to_field='nickname', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post' 
        
