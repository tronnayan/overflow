# Generated by Django 4.0.1 on 2022-01-13 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_answers_reply_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]