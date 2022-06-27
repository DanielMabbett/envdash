from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    """
    Snippets Serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        """
        Meta Class
        """
        model = Snippet
        fields = [
            'url',
            'id',
            'title',
            'group',
            'description',
            'highlight',
            'owner',
            # 'language',
            # 'style',
            'version_mke',
            'version_release'
        ]

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Users Serializer
    """
    snippets = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='snippet-detail',
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
            'snippets'
        ]
