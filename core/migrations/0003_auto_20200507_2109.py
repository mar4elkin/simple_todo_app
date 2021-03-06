# Generated by Django 3.0.3 on 2020-05-07 18:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20200507_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoobject',
            name='owner',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель'),
        ),
        migrations.AlterField(
            model_name='todoobject',
            name='priority',
            field=models.CharField(choices=[('#3ce305', 'Потом'), ('#d8e305', 'Терпимо'), ('#e30c05', 'Жарко')], default='#3ce305', max_length=30, verbose_name='Приоритет'),
        ),
        migrations.AlterField(
            model_name='todoobject',
            name='status',
            field=models.CharField(choices=[('inprocces', 'в процессе'), ('done', 'Выполнена')], default='inprocces', max_length=30, verbose_name='Статус задачи'),
        ),
        migrations.AlterField(
            model_name='todoobject',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
    ]
