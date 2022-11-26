from django.contrib import admin
from .models import Job, Contact, Activity

# Register your models here.
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['employer', 'application_date']


admin.site.register(Contact)

admin.site.register(Activity)