from django.forms import ModelForm
from .models import Comment
# from django import forms
# from .models import CarPost

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['commentBody']

# class SearchForm(forms.Form):
#     search_text = forms.CharField(
#                     required = False,
#                     label='Search!',
#                     widget=forms.TextInput(attrs={'placeholder': 'search here!'})
#                 )

#     search_year_exact = forms.IntegerField(
#         required = False,
#         label='Search year (exact match)!'
#     )

#     search_title_exact = forms.CharField(
#         required = False,
#         label='Search title (exact match)!'
#     )
