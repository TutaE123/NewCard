from django.contrib import admin
from .models import Post
from .models import Denunc, Cart, Koloda

admin.site.register(Post)
admin.site.register(Denunc)
admin.site.register(Cart)
admin.site.register(Koloda)
