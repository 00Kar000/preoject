from django.contrib import admin
from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.home_page, name="home"),
    path("contact-us", views.contact_us, name="contact"),
    path("about-us", views.about_us, name="about"),
    path("blog-detail/<int:pk>", views.blog_detail, name="blog_detail"),
]
