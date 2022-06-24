from snippets.views import EnvironmentViewSet, UserViewSet, api_root
from rest_framework import renderers

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

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

# API endpoints
urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('environments/',
        views.EnvironmentList.as_view(),
        name='snippet-list'),
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
        name='user-detail')
])

