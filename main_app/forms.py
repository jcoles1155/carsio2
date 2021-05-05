from django.forms import ModelForm
from .models import Comment
from django.contrib.auth.models import User

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['commentBody']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

