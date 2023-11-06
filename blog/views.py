from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView): # 여러 포스트 나열은 리스트뷰
    model = Post
    ordering = '-pk' # 최신글부터 표시

class PostDetail(DetailView): # 포스트 상세 페이지 만들기
    model = Post
    
# FBV에서 CBV로 가면서 일단 주석처리
# def index(request):
#     posts = Post.objects.all().order_by('-pk')
#
#     return render(
#         request,
#         'blog/index.html',
#         {
#             'posts': posts,
#         }
#     )

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post': post,
        }
    )