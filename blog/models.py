from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model): # django.db에서 가져온 models를 Post에 적용하여 Post 객체 생성(Model 상속), 이하 ()는 JS의 메소드에 해당
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length = 200) # CharField는 HTML의 input에 해당
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True) # 일종의 임시보관함(실질 작성 이전)에 해당

    def publish(self): # def는 JS의 function에 해당
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title