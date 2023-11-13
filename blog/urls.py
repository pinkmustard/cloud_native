from django. urls import path
from . import views

urlpatterns = [
    path('update_comment/<int:pk>/', views.CommentUpdate.as_view()), # 댓글 수정 페이지의 경로 추가cbv스타일
    path('update_post/<int:pk>/', views.PostUpdate.as_view()), #업데이트접근시 postupdate쿨래스 사용
    path('create_post/', views.PostCreate.as_view()), #create_post로 url을 입력하는 경우 postcreate클래스 사용
    path('tag/<str:slug>/', views.tag_page),
    path('category/<str:slug>/', views.category_page),
    path('<int:pk>/new_comment/', views.new_comment), #url에 있는 Pk로 포스트를 찾고, 그 포스트의 댓글을 달기 위해
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
    # path('<int:pk>/', views.single_post_page), #s_p_p함수 활용 처리 blog/뒤 정수 url 처리 //얘도 일단 주석
    # path('', views.index), #blog/로 끝나면 임포트한 views.py에 정의 index()함수 실행 // 얘도 일단 주석처리
]
