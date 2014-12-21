from django.db import models
from django import forms
from django.utils import dateparse
from django.contrib.auth.models import User


class Blog(models.Model):
    """ Basic blog entry - pub date, title, entry.
    """
    title = models.CharField(max_length=200)
    body = models.TextField()
    published = models.DateTimeField("date published")
    author = models.ForeignKey(User, null=True)

    def __unicode__(self):
        return self.title


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        widgets = {
            'published': forms.DateTimeInput(attrs={'class': 'datetimepicker'})
        }

    def clean_published(self):
        pub = str(self.cleaned_data['published'])
        return dateparse.parse_datetime(pub)