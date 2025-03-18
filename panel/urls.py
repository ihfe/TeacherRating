from django.urls import re_path
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

# from TeacherRating import views
from panel import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^class_admin$', views.class_admin, name='class_admin'),
    re_path(r'^class_admin/create_class$', views.create_class, name='create_class'),
    re_path(r'^class_admin/delete_class$', views.delete_class, name='delete_class'),
    re_path(r'^lesson_admin$', views.lesson_admin, name='lesson_admin'),
    re_path(r'^lesson_admin/create_lesson$', views.create_lesson, name='create_lesson'),
    re_path(r'^lesson_admin/delete_lesson$', views.delete_lesson, name='delete_lesson'),
    re_path(r'^teacher_admin$', views.teacher_admin, name='teacher_admin'),
    re_path(r'^teacher_admin/create_teacher$', views.create_teacher, name='create_teacher'),
    re_path(r'^teacher_admin/delete_teacher$', views.delete_teacher, name='delete_teacher'),
]