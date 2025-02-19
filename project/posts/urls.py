from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
        path('blog/<slug:slug>/', views.blog, name="entry"), 
    ]