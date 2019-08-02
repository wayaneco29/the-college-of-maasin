from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Posts



class PostForm(ModelForm):
    class Meta:
        model = Posts
        fields = [
            'title',
            'description',
            'content', 
            'author',
            ]