# Generated by Django 4.0.1 on 2022-01-13 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_question_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
    ]