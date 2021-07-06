from django  import forms

from .models import CustomUser,Post
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    class Meta:

        model = CustomUser
        fields =(
        'first_name',
        'last_name',
        'email',
        'username',
        'password1',
        'password2',
        )

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        for fieldname in [ 'password1', 'password2']:
            self.fields[fieldname].help_text = None   

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Post
        fields = (
        'title',
        'text',
        'thumbnail'
        )

