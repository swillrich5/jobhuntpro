# Generated by Django 4.1.1 on 2022-11-28 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobhunt', '0005_job_job_application_url_job_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('AC', 'Active'), ('NS', 'Not Selected'), ('WD', 'Withdrawn')], default='AC', max_length=2),
        ),
    ]
