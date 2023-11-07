from django.db import models
import os 

class Post(models.Model): # post모델은 models모듈의 mModel클래스 확장하여 만듦
    title = models.CharField(max_length=30) # title필드는 CharField(문자담는)클래스로 만들고 최대길이 30
    hook_text = models.CharField(max_length=100, blank=True) # 요약
    content = models.TextField() # 길이에 제한이 없는 TextField
    
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True) #이미지를 저장할 폴더의 경로 귀칙 지정
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True) # 파일을 업로드할 폴더의 경로 규칙 지정 
    
    created_at = models.DateTimeField(auto_now_add=True) # datetime필드로 만듦, 시간 자동
    update_at = models.DateTimeField(auto_now=True) #업데이트도 자동 시간 추가
    # author: 추후 작성
    def __str__(self):
        return f'[{self.pk}]{self.title}' #해당 포스트의 pk와 타이틀 값
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}' #모델의 레코드별 url 생성 규칙 정의
    
    def get_file_name(self): # 파일 경로 제외 파일명만 나오게
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self): #확장자를 찾아냄
        return self.get_file_name().split('.')[-1]