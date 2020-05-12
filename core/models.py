from django.db import models
from django.contrib.auth.models import User

class TodoObject(models.Model):
    title = models.CharField(max_length=50, verbose_name =(u'Название'))
    main_text = models.CharField(max_length=50, verbose_name =(u'Текст'))
    
    PRIORITY_TYPES = [
        ('#3ce305', 'Потом'),
        ('#d8e305', 'Терпимо'),
        ('#e30c05', 'Жарко'),
    ]

    STATUS_TYPES = [
        ('inprocces', 'В процессе'),
        ('done', 'Выполнена')
    ]

    JOBS_TYPES = [
        ('blank', 'blank'),
        ('backend', 'backend'),
        ('frontend', 'frontend')
    ]

    job_type = models.CharField(
        max_length = 30,
        choices = JOBS_TYPES,
        default = 'blank',
        verbose_name =(u'Тип Работы')
    
    )


    priority = models.CharField(
        max_length = 30,
        choices = PRIORITY_TYPES,
        default = '#3ce305',
        verbose_name  = (u'Приоритет')
    )

    status = models.CharField(
        max_length = 30,
        choices = STATUS_TYPES,
        default = 'inprocces',
        verbose_name = (u'Статус задачи')
    )

    class Meta:
      verbose_name = "Задачу"
      verbose_name_plural = "Задачи"

    def __str__(self):
        return str(self.title)
    

    