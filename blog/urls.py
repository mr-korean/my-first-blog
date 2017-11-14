from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    # 도메인 다음에 아무것도 없을 경우(정규 표현식),
    # views 파일의 post_list 클래스로 이동시킨다.
]