from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article
def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})
def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404

@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        text = request.POST.get('text', '').strip()
        errors = []

        if not title:
            errors.append('Название статьи не может быть пустым.')
        elif Article.objects.filter(title=title).exists():
            errors.append('Статья с таким названием уже существует.')

        if not text:
            errors.append('Текст статьи не может быть пустым.')

        if not errors:
            article = Article.objects.create(
                title=title,
                text=text,
                author=request.user
            )
            return redirect('get_article', article_id=article.id)
        else:
            return render(request, 'create_post.html', {
                'errors': errors,
                'title': title,
                'text': text,
            })
    else:
        return render(request, 'create_post.html')
