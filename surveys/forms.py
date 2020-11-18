from django.contrib.auth.forms import UserCreationForm

from surveys.models import MyUser


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': 'Логин',
        }
