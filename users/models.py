from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.


class CustomUser(AbstractUser):
    is_reader = models.BooleanField(default=False, help_text=_('Designates user as a reader.'))
    is_lib_staff = models.BooleanField(default=False, help_text=_('Designates user as a library staff.'))

    def __str__(self):
        return self.username
