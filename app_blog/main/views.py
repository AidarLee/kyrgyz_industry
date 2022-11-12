from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout 
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse, reverse_lazy
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from .models import *

from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext

def index(request):
    trans = translate(language='ru')
    last_news = News.objects.all().order_by("-id")[:4]
    context = {'last_news': last_news, 'trans':trans}
    return render(request, "index.html", context)

def translate(language):
    cur_language = get_language()
    try:
        activate(language)
        text = gettext('hello')
    finally:
        activate(cur_language)
    return text

def error_404(request):
    return render(request, '404.html')

def error_500(request):
    return render(request, '500.html')

def error_503(request):
    return render(request, '503.html')

def index(request):
    template_name = "client/index.html"
    return render(request, template_name, {})


def detail(request):
    template_name = "client/pages/blog_detail.html"
    return render(request, template_name, {})

@csrf_exempt
def login_page(request):
    template_name = "admin/pages/forms/login.html"
    
    return render(request, template_name, {})

@csrf_exempt
def authorization(request):
    success_url = reverse_lazy('admin_panel')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(success_url)
    else:
        return redirect('login_page')

def logout_page(request):
    logout(request)
    return redirect('login_page')
# Admin-Panel Views
@login_required
def admin_index_page(request):
    template_name = "admin/admin.html"
    context = {
        "is_active" : "main-panel"
    }
    return render(request, template_name, context)

@login_required
def admin_form_page(request):
    template_name = "admin/pages/forms/basic_elements.html"

    user_name = None
    if request.user.is_authenticated:
        user_name = request.user.username
    context = {
        "user" : user_name
    }
    return render(request, template_name, context)




class NewsView(View):
    model = News
    fields = '__all__'
    success_url = reverse_lazy('news_all')
    extra_context = {
        "is_active" : "news-panel",
        "expand" : "show"
        }

class NewsListView(LoginRequiredMixin, NewsView, ListView):
    login_url = 'login_page'
    template_name = 'admin/pages/news/news-all.html'
    

  