from django.shortcuts import render
#landing.html을 보여줌
def landing(request):
    return render(
        request,
        'single_pages/landing.html'
    )

# about_me.html을 보여줌
def about_me(request):
    return render(
        request,
        'single_pages/about_me.html'
    )
