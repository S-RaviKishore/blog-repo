from django.shortcuts import render
from myApp.models import Post

def post_list_view(request):
    post_list = Post.objects.all()
    d = {'post_list': post_list}
    return render(request, 'myApp/post_list.html', d)
