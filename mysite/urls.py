from django.contrib import admin
from django.urls import path
from . import views
from blog import views as views_blog
from about import views as about_views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("about/", about_views.index ),
    path("blog/", views_blog.index),
    path("", views.index)
]
