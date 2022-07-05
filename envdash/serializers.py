from rest_framework import serializers
from envdash.models import Environment, Cluster, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class EnvironmentSerializer(serializers.HyperlinkedModelSerializer):
    """
    Environments Serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='environment-highlight', format='html')
    # clusters = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     view_name='cluster-detail',
    #     read_only=True
    # )
    
    class Meta:
        """
        Meta Class
        """
        model = Environment
        fields = [
            'url',
            'id',
            'title',
            'group',
            'location',
            'description',
            'highlight',
            'owner',
            # 'clusters',
            'version_mke',
            'version_release'

        ]

class ClusterSerializer(serializers.HyperlinkedModelSerializer):
    """
    Environments Serializer
    """
    #owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='cluster-highlight', format='html')

    class Meta:
        """
        Meta Class
        """
        model = Cluster
        fields = [
            'url',
            'id',
            'title',
            'type',
            'description',
            'environment',
            'highlight',
            'version'
        ]

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Users Serializer
    """
    environments = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='environment-detail',
        read_only=True
    )

    class Meta:
        """
        Meta Class
        """
        model = User
        fields = [
            'url',
            'id',
            'username',
            'environments'
        ]
