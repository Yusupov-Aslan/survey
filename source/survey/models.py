from django.core.validators import BaseValidator
from django.db import models


# Create your models here.
from django.utils.deconstruct import deconstructible


class Poll(models.Model):
    question = models.TextField(max_length=2000, verbose_name="Опрос")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def __str__(self):
        return f"{self.pk}. {self.question} - {self.created_at}"

    class Meta:
        db_table = 'polls'
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Choice(models.Model):
    option_text = models.TextField(max_length=2000, verbose_name="Текст варианта")
    poll = models.ForeignKey('survey.Poll', on_delete=models.CASCADE, null=True, related_name='choices',
                             verbose_name='Опросы')

    def __str__(self):
        return f"{self.pk}. {self.option_text} - {self.poll}"

    class Meta:
        db_table = 'choices'
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'


class Answer(models.Model):
    poll = models.ForeignKey('survey.Poll', on_delete=models.CASCADE, null=True, related_name='answers',
                             verbose_name='Опрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    choice = models.ForeignKey('survey.Choice', on_delete=models.CASCADE, null=True, related_name='answers',
                               verbose_name='Вариант')
