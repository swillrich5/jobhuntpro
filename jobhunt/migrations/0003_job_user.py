# Generated by Django 4.1.1 on 2022-11-23 17:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobhunt', '0002_job_job_title_alter_job_job_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]