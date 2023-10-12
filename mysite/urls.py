from django.contrib import admin
from django.urls import path
from . import views
from blog import views as views_blog
urlpatterns = [
    path("admin/", admin.site.urls),
    path("about/", views.about),
    path("blog/", views_blog.index),
    path("", views.index)
]
