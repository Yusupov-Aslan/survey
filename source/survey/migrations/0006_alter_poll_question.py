# Generated by Django 4.0 on 2022-02-05 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0005_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='question',
            field=models.TextField(default='question', max_length=2000, verbose_name='Опрос'),
            preserve_default=False,
        ),
    ]
