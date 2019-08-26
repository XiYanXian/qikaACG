from django.contrib import admin
from .models import UserInfo, Comment, CommentLike, AnimeCollection
# Register your models here.
admin.site.register(UserInfo)
admin.site.register(CommentLike)
admin.site.register(Comment)
admin.site.register(AnimeCollection)
