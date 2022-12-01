from django import forms
from django.forms import ModelForm, TextInput, Textarea
from .models import Job, Contact, Activity


class AddContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'title', 'email', 'phone']
        labels = {
                    'name': ("Contact Name:"),
                    'title': ('Title:'),
                    'email': ('Email:'),
                    'phone': ('Phone No:'),
                }
        widgets = {
                    'name': TextInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'John Smith',
                    }),
                    'title': TextInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'HR Generalist',
                    }),
                    'email': TextInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'jsmith@thiscompany.com'
                    }),
                    'phone': TextInput(attrs={
                        'class': 'form-control',
                        'placeholder': '512-459-2222'
                    })
        }
        


class AddJobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['employer', 'job_title', 'job_description', 'notes', 'status']
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
            }),
        }



class AddActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = ['activity', 'date', 'note']
        labels = {
            'activity': ('Activity:'),
            'date': ('Date:'),
            'note': ('Note:'),
        }
        widgets = {
            'activity': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '1st Interview',
            }),
            'date': TextInput(attrs={
                'class': 'form-control',
            }),
            'note': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Review company background',
            }),
        }
