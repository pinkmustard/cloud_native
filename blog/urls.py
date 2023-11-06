from django. urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.single_post_page), #s_p_p함수 활용 처리 blog/뒤 정수 url 처리
    path('', views.index), #blog/로 끝나면 임포트한 views.py에 정의 index()함수 실행
]
