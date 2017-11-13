from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
# 위의 시간대에 따라 받아온 게시글의 행렬을, 아래의 형태로 post_list.html에 뿌린다.