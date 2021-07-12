from django.urls import path

from curriculum import views

from curriculum.models import major, lecture

app_name = 'curriculum'
urlpatterns = [
    #/curriculum/
    path('', views.index, name='index'),
    #/curriculum/1/
    path('<int:major_id>/', views.select_major, name='select_major'),
    #/curriculum/1/2/
    path('<int:major_id>/<int:lecture_id>/', views.review, name='review'),
    #/curriculum/1/2/add_review
    path('<int:major_id>/<int:lecture_id>/add_review/', views.add_review, name='add_review'),
    #/curriculum/1/2/del_review
    path('<int:major_id>/<int:lecture_id>/<int:class_review_id>/del_review/', views.del_review, name='del_review'),
]