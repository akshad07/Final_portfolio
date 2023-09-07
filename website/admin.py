from django.contrib import admin

# Register your models here.
from .models import Contact,Blogs

class BlogsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category','created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'category': ('title',)}

admin.site.register(Contact)
admin.site.register(Blogs, BlogsAdmin)