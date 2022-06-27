from envdash.models import Snippet
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

snippet_list = EnvironmentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

snippet_detail = EnvironmentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

snippet_highlight = EnvironmentViewSet.as_view({
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
    path('dashboard', views.ListView.as_view()),
    path('', views.api_root),
    path('environments/',
        views.EnvironmentList.as_view(),
        name='environment-list'),
    path('environments/<int:pk>/',
        views.EnvironmentDetail.as_view(),
        name='snippet-detail'),
    path('environments/<int:pk>/highlight/',
        views.SnippetHighlight.as_view(),
        name='snippet-highlight'),
    path('users/',
        views.UserList.as_view(),
        name='user-list'),
    path('users/<int:pk>/',
        views.UserDetail.as_view(),
        name='user-detail'),
])