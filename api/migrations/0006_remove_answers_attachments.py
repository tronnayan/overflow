# Generated by Django 4.0.1 on 2022-01-13 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_question_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='attachments',
        ),
    ]
