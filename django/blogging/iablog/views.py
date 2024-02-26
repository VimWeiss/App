from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post

# Create your views here.

class PostView(View):
    #вывод записей
    def get(self, request):
        #request информация принятая от пользователя
        posts = Post.objects.all()
        return render(request, 'iablog/iablog.html', {'post_list': posts})

class PostDetail(View):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'iablog/blog_detail.html', {'post':post})

class AddComments(View):
    def post(self, request, pk):
        print(request.POST)
        return redirect('/')
