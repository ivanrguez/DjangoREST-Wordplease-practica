from django.contrib import admin

from tasks.models import Post, Categorias, Comment


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Categorias)