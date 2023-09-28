from typing import Any
from django.contrib import admin
from .models import Category, Article




class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    search_fields = ('title' , 'content', 'user__username')
    
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'update_at')

    

        


# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Article, CategoryAdmin)



