# Generated by Django 4.0.1 on 2022-01-14 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_question_attachments'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='attachments',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='question',
            name='attachments',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
