from django.contrib import admin
from .models import Post #.models의 Post를 가져옴

# Register your models here.
admin.site.register(Post)