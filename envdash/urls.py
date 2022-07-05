from envdash.models import Environment
from envdash.views import EnvironmentViewSet, UserViewSet, api_root
from rest_framework import renderers
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from envdash import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from envdash import views

# Adding this is causing issues with loading the views
# app_name = 'snippets'

environment_list = EnvironmentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

environment_detail = EnvironmentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

environment_highlight = EnvironmentViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
    'get': 'list'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

# API endpoints
urlpatterns = format_suffix_patterns([
    path('', views.ListView.as_view()),
    path('api', views.api_root),
    path('api/environments/',
        views.EnvironmentList.as_view(),
        name='environment-list'),
    path('api/environments/<int:pk>/',
        views.EnvironmentDetail.as_view(),
        name='environment-detail'),
    path('api/environments/<int:pk>/highlight/',
        views.EnvironmentHighlight.as_view(),
        name='environment-highlight'),
    path('api/users/',
        views.UserList.as_view(),
        name='user-list'),
    path('api/users/<int:pk>/',
        views.UserDetail.as_view(),
        name='user-detail'),
])
