from django.contrib import admin
from .models import Blogpost, Tag

admin.site.register(Blogpost)
admin.site.register(Tag)