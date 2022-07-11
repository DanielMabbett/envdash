from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from django.views import generic
from envdash.permissions import IsOwnerOrReadOnly
from envdash.models import Environment, Cluster
from envdash.serializers import ClusterSerializer, EnvironmentSerializer, UserSerializer

@api_view(['GET'])
def api_root(request, format=None):
    """
    API Root View
    """
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'environments': reverse('environment-list', request=request, format=format),
        'clusters': reverse('cluster-list', request=request, format=format)
    })

class ClusterList(generics.ListCreateAPIView):
    queryset = Cluster.objects.all()
    serializer_class = ClusterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
class EnvironmentList(generics.ListCreateAPIView):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class EnvironmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

class GUIEnvironmentDetail(generic.DetailView):
    """
    AKA the Environment Dashboard
    """
    model = Environment
    template_name = 'app/environments_detail.html'
    context_object_name = 'environment'

class ClusterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cluster.objects.all()
    serializer_class = ClusterSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

class LandingView(generic.ListView):
    """
    AKA the first Dashboard you see, the overview page
    """
    model = Environment
    template_name = 'app/landing.html'
    context_object_name = 'object_list'
    def get_queryset(self):
        """
        Return the environments objects back to the dash
        """
        myset = {
            "environments": Environment.objects.all(),
            "clusters": Cluster.objects.all(),
        }
        return myset

class ListView(generic.ListView):
    """
    AKA the Environment Dashboard
    """
    model = Environment
    template_name = 'app/environments_list.html'
    context_object_name = 'environment_list'
    # def get_queryset(self):
    #     """Return the last five published questions."""
    #     return Question.objects.order_by('-pub_date')[:5]
    def get_queryset(self):
        """
        Return the environments objects back to the dash
        """
        return Environment.objects.all()

class ClusterListView(generic.ListView):
    """
    AKA the Cluster Dashboard
    """
    model = Cluster
    template_name = 'app/clusters_list.html'
    context_object_name = 'cluster_list'
    def get_queryset(self):
        """
        Return the environments objects back to the dash
        """
        return Cluster.objects.all()

class EnvironmentHighlight(generics.GenericAPIView):
    queryset = Environment.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        environment = self.get_object()
        return Response(environment.highlighted)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
