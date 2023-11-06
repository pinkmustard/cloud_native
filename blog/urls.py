from django. urls import path
from . import views

urlpatterns = [
    path('', views.index), #blog/로 끝나면 임포트한 views.py에 정의 index()함수 실행
]
