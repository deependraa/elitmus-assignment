from django.urls import path
from django.urls.conf import include

from . import views
app_name = 'posts'
urlpatterns = [
    path('',views.PostListCreate,name='PostListCreate'),
    path('advertisement/<int:advertisement_id>',views.advertisement,name='advertisement'),
    # path('edit_post/<int:post_id>',views.edit_post,name='edit_post'),
    path('post/create_new_post',views.create_post,name='create_post'),
    path('post/<pk>/delete',views.PostDeleteView.as_view(),name='post_delete'),
    path('post/<pk>/update',views.PostUpdateView.as_view(),name='post_update'),
    
]

