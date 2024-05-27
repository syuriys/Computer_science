from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('contacts/', views.contacts, name='contacts'),
    path('news/', views.news, name='news'),
    path('news/<int:pk>/', views.news_details, name='news_details'),
    path('courses/', views.course_table, name='course_table'),
    path('tinymce/', include('tinymce.urls')),
]
