from django.db import models
from django.contrib.auth.models import User


class MyUser(User):
    pass


class Survey(models.Model):
    name = models.CharField(verbose_name='Название опроса', max_length=100)
    date_start = models.DateField(verbose_name='Дата начала', editable=True)
    date_end = models.DateField(verbose_name='Дата завершения', editable=True)
    description = models.CharField(verbose_name='Описание', max_length=1000)

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Question(models.Model):
    survey = models.ForeignKey(Survey, verbose_name='Опрос', on_delete=models.CASCADE, related_name='questions', null=True)
    name = models.CharField(verbose_name='Название вопроса', max_length=100)
    variants = models.CharField(verbose_name='Варианты ответов', max_length=1000, null=True, blank=True)
    multiple_choice = models.BooleanField(verbose_name='Вопрос с множественным выбором ответа')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


# class Answer(models.Model):
#     user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, blank=True, null=True, related_name='user')
#     question = models.OneToOneField(Question, on_delete=models.CASCADE, blank=True, related_name='question')
