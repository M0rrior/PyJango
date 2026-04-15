from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
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

def register(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        errors = {}

        if not username or not email or not password:
            errors['form'] = 'Все поля обязательны для заполнения'
        elif User.objects.filter(username=username).exists():
            errors['form'] = 'Пользователь с таким логином уже существует'
        else:
            user = User.objects.create_user(username, email, password)

            login(request, user)
            return redirect('archive')
        return render(request, 'register.html', {'form': request.POST, 'errors': errors})
    else:
        return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('archive')
        else:
            return render(request, 'login.html', {'error': 'Неверный логин или пароль'})
    else:
        return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('archive')