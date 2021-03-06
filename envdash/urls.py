from envdash.models import Environment
# from envdash.views import EnvironmentViewSet, UserViewSet, api_root
from envdash.views import api_root
from rest_framework import renderers
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from envdash import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from envdash import views

urlpatterns = format_suffix_patterns([
    # gui
    path('', views.LandingView.as_view()),
    path('environments', views.ListView.as_view()),
    path('environments/<int:pk>/',
        views.GUIEnvironmentDetail.as_view(),
        name='gui-environment-detail'),
    path('clusters', views.ClusterListView.as_view()),

    # api
    path('api', views.api_root),
    path('api/clusters/',
        views.ClusterList.as_view(),
        name='cluster-list'),
    path('api/clusters/<int:pk>/',
        views.ClusterDetail.as_view(),
        name='cluster-detail'),
    path('api/clusters/<int:pk>/highlight/',
        views.EnvironmentHighlight.as_view(),
        name='cluster-highlight'),
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
