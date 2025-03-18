from django.urls import re_path

# from TeacherRating import views
from rating import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^event_admin$', views.event_admin, name='event_admin'),
    re_path(r'^event_admin/create_event$', views.create_event, name='create_event'),
    re_path(r'^event_admin/delete_event$', views.delete_event, name='delete_event'),
    re_path(r'^event_admin/event_detail$', views.event_detail, name='event_detail'),
    re_path(r'^item_admin$', views.item_admin, name='item_admin'),
    re_path(r'^item_admin/create_item$', views.create_item, name='create_item'),
    re_path(r'^item_admin/delete_item$', views.delete_item, name='delete_item'),
    re_path(r'^event_admin/event_detail/detail_class$', views.detail_class, name='detail_class'),
    re_path(r'^event_admin/event_detail/detail_answer$', views.detail_answer, name='detail_answer'),
    re_path(r'^event_admin/event_detail/detail_aver$', views.detail_aver, name='detail_aver'),
]