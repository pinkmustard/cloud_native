from django.db import models

class Post(models.Model): # post모델은 models모듈의 mModel클래스 확장하여 만듦
    title = models.CharField(max_length=30) # title필드는 CharField(문자담는)클래스로 만들고 최대길이 30
    content = models.TextField() # 길이에 제한이 없는 TextField
    
    created_at = models.DateTimeField(auto_now_add=True) # datetime필드로 만듦, 시간 자동
    update_at = models.DateTimeField(auto_now=True) #업데이트도 자동 시간 추가
    # author: 추후 작성
    def __str__(self):
        return f'[{self.pk}]{self.title}' #해당 포스트의 pk와 타이틀 값