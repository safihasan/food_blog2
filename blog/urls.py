from django.urls import path
from . import views


urlpatterns = [
    path("", views.PostList.as_view(), name='home'),
    path('static/images/favicon/favicon.ico', serve_favicon, name='favicon'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),     
]