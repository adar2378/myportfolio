from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:blog_id>/', views.detail, name='detail')
]
