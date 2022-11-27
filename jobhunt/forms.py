from django import forms
from django.forms import ModelForm, TextInput, Textarea
from .models import Job

class AddContactForm(forms.Form):
    contact_name = forms.CharField(label="Contact Name:", max_length=100)
    contact_title = forms.CharField(label="Title:", max_length=50)
    contact_email = forms.EmailField(label="Email Address:")
    contact_phone = forms.CharField(label="Phone No.:", max_length=15)


class AddActivityForm(forms.Form):
    activity = forms.CharField(label="Activity:", max_length=100)
    activity_date = forms.DateTimeField(label="Date/Time:")
    activity_note = forms.CharField(label="Notes:", max_length=200)


class AddJobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['employer', 'job_title', 'job_description', 'notes']
        labels = { 'employer': ('Employer'),
                   'job_title': ('Job Title'),
                   'job_description': ('Job Description'),
                   'notes': ('Notes'),
                 }
        widgets = {
            'employer': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Employer'
                }),
            'job_title': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Job Title',
            }),
            'job_description': Textarea(attrs={
                'rows': 5
            }),
            'notes': Textarea(attrs={
                'rows': 3
            })
        }