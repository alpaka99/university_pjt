from django.urls import path

from majorreviews import views

app_name = 'majorreviews'
urlpatterns = [
    path('', views.index, name='index'),
    path('review/<int:pk>/', views.detail, name='detail'),
    path('review/write', views.write, name='write'),
    path('review/<int:pk>/edit', views.edit, name='edit'),
    path('review/<int:pk>/delete', views.delete, name='delete'),
    path('review/comment/<int:pk>/edit', views.comment_edit, name='comment_edit'),
    #path('review/comment/<int:pk>/approve', views.comment_approve, name='comment_approve'),
    path('review/comment/<int:pk>/delete', views.comment_delete, name='comment_delete'),
    path('review/comment/<int:pk>/write', views.comment_write, name='comment_write'),
]
