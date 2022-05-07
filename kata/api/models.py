import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Member(models.Model):
    class Gender(models.IntegerChoices):
        MALE = 1
        FEMALE = 2

    id = models.AutoField(
        primary_key=True
    )
    first_name = models.CharField(
        max_length=100,
        blank=False
    )
    last_name = models.CharField(
        max_length=100,
        blank=False
    )
    gender = models.IntegerField(
        choices=Gender.choices
    )
    date_of_birth = models.DateField()
    email = models.CharField(
        max_length=100,
        blank=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
