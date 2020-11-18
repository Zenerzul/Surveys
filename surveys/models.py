from django.db import models
from django.contrib.auth.models import User


class MyUser(User):
    pass


class Survey(models.Model):
    name = models.CharField(max_length=100)
    date_start = models.DateField(editable=True)
    date_end = models.DateField(editable=True)
    description = models.CharField(max_length=1000)


class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='questions', null=True)
    name = models.CharField(max_length=100)
    variants = models.CharField(max_length=1000, null=True, blank=True)
    multiple_choice = models.BooleanField()
