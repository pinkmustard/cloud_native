from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown
import os 

# 태그 모델 만들기
class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}/'

# 카테고리 모델 만들기
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self): #url 처리
        return f'/blog/category/{self.slug}/'

    class Meta:
        verbose_name_plural = 'categories'

class Post(models.Model): # post모델은 models모듈의 mModel클래스 확장하여 만듦
    title = models.CharField(max_length=30) # title필드는 CharField(문자담는)클래스로 만들고 최대길이 30
    hook_text = models.CharField(max_length=100, blank=True) # 요약
    content = MarkdownxField() #마크다운
    
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True) #이미지를 저장할 폴더의 경로 귀칙 지정
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True) # 파일을 업로드할 폴더의 경로 규칙 지정 
    
    created_at = models.DateTimeField(auto_now_add=True) # datetime필드로 만듦, 시간 자동
    update_at = models.DateTimeField(auto_now=True) #업데이트도 자동 시간 추가
    
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    
    tags = models.ManyToManyField(Tag, blank=True) # 포스트 모델에 태그 필드 추가
    
    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}' #해당 포스트의 pk와 타이틀 값
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}/' #모델의 레코드별 url 생성 규칙 정의
    
    def get_file_name(self): # 파일 경로 제외 파일명만 나오게
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self): #확장자를 찾아냄
        return self.get_file_name().split('.')[-1]
    
    def get_content_markdown(self): #작성한 내용 마크다운으로 보이도록 매서드 만들기
        return markdown(self.content)

# 댓글 기능, 여러 댓글이 한 포스트의 댓글이 되기 때문에 외래키 사용
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author}::{self.content}'

    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'