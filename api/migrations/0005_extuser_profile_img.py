# Generated by Django 4.0.1 on 2022-01-15 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_answers_attachments_alter_question_attachments'),
    ]

    operations = [
        migrations.AddField(
            model_name='extuser',
            name='profile_img',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
