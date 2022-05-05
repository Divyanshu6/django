from django.contrib.auth.forms import UserCreationForm
from djangoUser.models import extendedUser


class registrationForm(UserCreationForm):
    class Meta:
        model=extendedUser
        fields='__all__'