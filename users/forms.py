from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CunstomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'username',
                  'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CunstomUserCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'input'})
