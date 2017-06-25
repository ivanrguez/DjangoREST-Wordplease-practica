from django  import forms

from tasks.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['categoria', 'titulo', 'intro', 'descripcion', 'imagen']