# Generated by Django 4.0.1 on 2022-01-15 08:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0006_alter_extuser_profile_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='vote_count',
        ),
        migrations.RemoveField(
            model_name='question',
            name='vote_count',
        ),
        migrations.AlterField(
            model_name='extuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='extuser', to=settings.AUTH_USER_MODEL),
        ),
    ]
