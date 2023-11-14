from django.shortcuts import render
from blog.models import Post

#landing.html을 보여줌
def landing(request):
    recent_posts = Post.objects.order_by('-pk')[:3]

    return render(
        request,
        'single_pages/landing.html',
        {
            'recent_posts': recent_posts,
        }
    )

# about_me.html을 보여줌
def about_me(request):
    return render(
        request,
        'single_pages/about_me.html'
    )
