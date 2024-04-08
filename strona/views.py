from django.shortcuts import render, redirect
from django.utils import timezone
from strona.models import Post


def base(request):
    return render(request, 'strona/base.html', {})


def glowna(request):
    return render(request, 'strona/glowna.html', {})


def posty(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'strona/posty.html', {'posts': posts})


def kontakt(request):
    return render(request, 'strona/kontakt.html', {})


def wiecej(request):
    return render(request, 'strona/wiecej.html', {})


def error_404_view(request, exception):
    data = {"name": 'BezpiecznaCyberPrzestrzeń'}
    return render(request, 'strona/404.html', data)


def error_500_view(request):
    data = {"name": 'BezpiecznaCyberPrzestrzenie'}
    return render(request, 'strona/500.html', data)


class PostForm:
    pass


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('posty', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'strona/posty.html', {'form': form})

