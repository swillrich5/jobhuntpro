from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
    employer = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100, blank=True)
    job_description = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    application_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'self.job_title + ": " + self.employer'


class Contact(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=11)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

class Activity(models.Model):
    activity = models.CharField(max_length=50)
    date = models.DateTimeField()
    note = models.TextField()
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

