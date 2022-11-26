from django import forms

class AddContactForm(forms.Form):
    contact_name = forms.CharField(label="Contact Name:", max_length=100)
    contact_title = forms.CharField(label="Title:", max_length=50)
    contact_email = forms.EmailField(label="Email Address:")
    contact_phone = forms.CharField(label="Phone No.:", max_length=15)


class AddActivityForm(forms.Form):
    activity = forms.CharField(label="Activity:", max_length=100)
    activity_date = forms.DateTimeField(label="Date/Time:")
    activity_note = forms.CharField(label="Notes:", max_length=200)
