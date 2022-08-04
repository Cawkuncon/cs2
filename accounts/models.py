from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.apps import apps

# Create your models here.
from csinf.models import SkinInfo


class MyUser(AbstractUser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    favorite_skins = models.ManyToManyField(SkinInfo, blank=True)

# class MyUserManager(UserManager):
#
#     def _create_user(self, email, first_name, last_name, password, **extra_fields):
#         """
#         Create and save a user with the given username, email, and password.
#         """
#         if not email:
#             raise ValueError("The given username must be set")
#         email = self.normalize_email(email)
#         # Lookup the real model class from the global app registry so this
#         # manager method can be used in migrations. This is fine because
#         # managers are by definition working on the real model.
#         GlobalUserModel = apps.get_model(
#             self.model._meta.app_label, self.model._meta.object_name
#         )
#         first_name = GlobalUserModel.normalize_username(first_name)
#         last_name = GlobalUserModel.normalize_username(last_name)
#         user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
#         user.password = make_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_user(self, first_name, last_name, email=None, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", False)
#         extra_fields.setdefault("is_superuser", False)
#         return self._create_user(email, first_name, last_name,  password, **extra_fields)
#
#     def create_superuser(self, first_name, last_name, email=None, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)
#
#         if extra_fields.get("is_staff") is not True:
#             raise ValueError("Superuser must have is_staff=True.")
#         if extra_fields.get("is_superuser") is not True:
#             raise ValueError("Superuser must have is_superuser=True.")
#         return self._create_user(email, first_name, last_name,  password, **extra_fields)
#
#
#
# class MyUser(AbstractUser):
#     email = models.EmailField(
#         verbose_name='email address',
#         max_length=255,
#         unique=True,
#         error_messages={
#             "unique": _("A user with that username already exists."),
#         },
#     )
#     first_name = models.CharField(_("first name"), max_length=255)
#     last_name = models.CharField(_("last name"), max_length=255)
#     is_active = models.BooleanField(default=True)
#     is_superuser = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     favorite_skins = models.ManyToManyField(SkinInfo, blank=True)
#
#     objects = MyUserManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']
#
#     def __str__(self):
#         return self.email
#
#     def has_perm(self, perm, obj=None):
#         return True
#
#     def has_perms(self, perm_list, obj=None):
#         return True
