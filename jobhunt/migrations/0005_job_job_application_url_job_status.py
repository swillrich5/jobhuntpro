# Generated by Django 4.1.1 on 2022-11-27 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobhunt', '0004_contact_activity'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_application_url',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='job',
            name='status',
            field=models.TextField(choices=[('AC', 'Active'), ('NS', 'Not Selected'), ('WD', 'Withdrawn')], default='AC', max_length=2),
        ),
    ]
