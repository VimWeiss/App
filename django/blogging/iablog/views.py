from django.shortcuts import render
from django.views.generic.base import View
from .models import Post

# Create your views here.

class PostView(View):
    #вывод записей
    def get(self, request):
        #request информация принятая от пользователя
        posts = Post.objects.all()
        return render(request, 'iablog/iablog.html', {'post_list': posts})
