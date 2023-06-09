from django.contrib.auth.models import AbstractUser
from django.db.models import ImageField, CharField, BooleanField

class Users(AbstractUser):
    image = ImageField(upload_to='user_pic', blank=True)
    login_ke = CharField(max_length=50, null=True)
    pass_ke = CharField(max_length=50, null=True)
    token = CharField(max_length=100, null=True)
    token_valid = BooleanField(default=True)
    login_valid = BooleanField(default=True)

