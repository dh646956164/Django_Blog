from django import forms
from django.forms.widgets import ClearableFileInput
from .models import Post, Category, Comment

# Retrieve all category names and store them in a tuple
choices = Category.objects.all().values_list('name', 'name')

# Create an empty list to store category choices
choices_list = []

# Iterate through the choices and append each choice to the choices_list
for item in choices:
    choices_list.append(item)

# Create a form for adding new posts, inheriting from forms.ModelForm
class PostForm(forms.ModelForm):
    # Include the category field with a ModelChoiceField
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)

    # Define the meta class for the PostForm
    class Meta:
        # Specify the model to use (Post)
        model = Post
        # Specify the fields to include in the form
        fields = ['title', 'header_image', 'content', 'category']

        # Define the widgets for each field
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "this is the title"}),
            'header_image': ClearableFileInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'This is where you can post your content'}),
            'category': forms.Select(choices=choices_list, attrs={'class': 'form-control'})
        }

# Create a form for updating existing posts, inheriting from forms.ModelForm
class UpdateForm(forms.ModelForm):
    # Include the category field with a ModelChoiceField
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)

    # Define the meta class for the UpdateForm
    class Meta:
        # Specify the model to use (Post)
        model = Post
        # Specify the fields to include in the form
        fields = ['title', 'header_image', 'content', 'category']

        # Define the widgets for each field
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "this is the title"}),
            'header_image': ClearableFileInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'This is where you can post your content'}),
            'category': forms.Select(choices=choices_list, attrs={'class': 'form-control'})
        }

# Create a form for adding comments, inheriting from forms.ModelForm
class CommentForm(forms.ModelForm):
    # Define the meta class for the CommentForm
    class Meta:
        # Specify the model to use (Comment)
        model = Comment
        # Specify the fields to include in the form
        fields = ['name', 'body']

        # Define the widgets for each field
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'body': forms.Textarea(attrs={'placeholder': 'Leave a comment'}),
        }
