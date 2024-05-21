from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import reverse_lazy


def index(request):
    return render(request, 'genshinapp/index.html')


def themes(request):
    if request.method == 'POST':
        form = ThemesForm(request.POST,request.FILES)
        if form.is_valid():
            themeauthor_id = request.user.id
            themeimg = form.cleaned_data['themeimg']
            themecontent = form.cleaned_data['themecontent']
            themename = form.cleaned_data['themename']
            theme = Themes(themeauthor_id=themeauthor_id,themeimg=themeimg, themecontent=themecontent, themename=themename)
            theme.save()
            return redirect('../themes')
    else:
        form = ThemesForm()
    themes = Themes.objects.all()
    data = {
        'themes': themes,
    }
    return render(request, 'genshinapp/themes.html', data)


def reg(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # создание объекта без сохранения в БД
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegForm()
    data = {
        'form': form,
    }
    return render(request, 'genshinapp/reg.html', data)


def themesinside(request, theme_id):
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            user_id = request.user.id
            commentcontent = form.cleaned_data['commentcontent']
            commentimg = form.cleaned_data['commentimg']
            theme_id = theme_id
            comments = Comments(commentcontent=commentcontent, user_id=user_id, theme_id=theme_id,
                                commentimg=commentimg)
            comments.save()
            return redirect(f'/themes/{theme_id}')
    else:
        form = CommentForm()
    themes = Themes.objects.filter(id=theme_id)
    comments = Comments.objects.filter(theme=theme_id)
    data = {
        'themes': themes,
        'comments': comments,
    }
    return render(request, 'genshinapp/insidethemes.html', data)


def logout_view(request):
    logout(request)
    return redirect('../main')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'genshinapp/login.html'
    extra_context = {'title': "Авторизация"}

    def get_success_url(self):
        return reverse_lazy('main')


def lk(request):
    themesvar = Themes.objects.filter(themeauthor=request.user.id)
    data={
        'themesvar':themesvar,
    }
    return render(request, 'genshinapp/lk.html', data)
