from django.urls import path

from . import views
from .feeds import LatestPostsFeed

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),   
    path('question-submitted/', views.question_submitted, name='question-submitted'),
    path('<pk>/post/', views.post, name='post'),
    path('feed/', LatestPostsFeed(), name='feed'), 
    path('<pk>/categorie/', views.categorie, name='categorie'),
]