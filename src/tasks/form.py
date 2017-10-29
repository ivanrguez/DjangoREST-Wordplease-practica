from django  import forms

from tasks.models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['categoria', 'titulo', 'intro', 'descripcion', 'imagen', 'estado']

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)