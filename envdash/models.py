from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class Environment(models.Model):
    """
    Environment Model
    """
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    location = models.CharField(max_length=24, blank=True, default='')
    description = models.TextField()
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey('auth.User', related_name='environments', on_delete=models.CASCADE)
    highlighted = models.TextField()
    version = models.CharField(max_length=24, blank=True, default='')
    group = models.CharField(max_length=24, blank=True, default='')

    class Meta:
        ordering = ['created']
        
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(
            style=self.style,
            full=True,
            **options
        )
        self.highlighted = highlight(
            self.description,
            lexer,
            formatter
        )
        super().save(*args, **kwargs)

class Cluster(models.Model):
    """
    Cluster Model
    """
    environment = models.ForeignKey(Environment, related_name="clusters", on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='clusters', on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    type = models.CharField(max_length=24, blank=True, default='')
    version = models.CharField(max_length=24, blank=True, default='')
    description = models.TextField()

    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    highlighted = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']
