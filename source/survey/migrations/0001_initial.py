# Generated by Django 4.0 on 2022-02-05 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_text', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Текст варианта')),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Вопрос')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
            ],
        ),
    ]
