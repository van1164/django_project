from django.contrib import admin
from .models import Post,premier_league,news

admin.site.register(Post)
admin.site.register(premier_league)
admin.site.register(news)