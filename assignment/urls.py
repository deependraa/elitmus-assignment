from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views
from .views import home_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('posts.urls')),
    path('accounts/',include('accounts.urls')),
    
]
