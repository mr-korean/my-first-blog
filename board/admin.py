from django.contrib import admin
from board.models import Bost

# Register your models here.
class BostAdmin(admin.ModelAdmin):
    list_display  = ('title', 'modify_date')
    list_filter   = ('modify_date',)
    search_fields = ('title', 'content')

admin.site.register(Bost, BostAdmin)