from django.urls import re_path

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

# from TeacherRating import views
from questionnaire import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^event_overview/(?P<event_id>[0-9]+)$', views.event_overview, name='event_overview'),
    re_path(r'^event_detail/(?P<event_id>[0-9]+)/(?P<classification>[0-9])/(?P<main_id>[0-9]+)$', views.event_detail, name='event_detail'),
    re_path(r'^create_result$', views.create_result, name='create_result'),
]