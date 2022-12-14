from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Job, Contact, Activity
from .forms import AddContactForm, AddActivityForm, AddJobForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def job_list(request):
    jobs = Job.objects.filter(user=request.user)
    return render(request, 'jobhunt/pages/job_list.html', {'jobs': jobs})



def job_detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    activities = Activity.objects.filter(pk=job_id)
    contacts = Contact.objects.filter(pk=job_id)
    print(contacts)
    print(activities)
    return render(request, 'jobhunt/pages/job_detail.html', {
                    'job': job,
                    'activities': activities,
                    'contacts': contacts,
                 })



def add_contact(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if request.method == 'GET':
        return render(request, 'jobhunt/pages/addcontactform.html',
                        {
                            'form': AddContactForm(),
                            'job': job
                        })
    else:
        try:
            name = request.POST['contact_name']
            title = request.POST['contact_title']
            email = request.POST['contact_email']
            phone = request.POST['contact_phone']
            job_id = job_id
            contact = Contact.objects.create(
                        name = name,
                        title = title,
                        email = email,
                        phone = phone,
                        job_id = job_id
            )
            return redirect('jobhunt:job_detail', job.id)
        except ValueError:
            return render(request, 'jobhunt/pages/addcontactform.html', {
                'form': AddContactForm(),
                'error': 'Bad data submitted'
            })



def add_activity(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if request.method == 'GET':
        return render(request, 'jobhunt/pages/addactivityform.html',
                        {
                            'form': AddActivityForm(),
                            'job': job
                        })
    else:
        try:
            activity_name = request.POST['activity']
            date = request.POST['date']
            note = request.POST['note']
            job_id = job_id
            activity = Activity.objects.create(
                    activity = activity_name,
                    date = date,
                    note = note
            )
            return redirect('jobhunt:job_detail', job.id)
        except ValueError:
            return render(request, 'jobhunt/pages/addactivityform.html', {
                'form': AddActivityForm(),
                'error': 'Bad data submitted'
            })



@login_required
def add_job(request):
    if request.method == 'GET':
        return render(request, 'jobhunt/pages/add_job.html', {
                        'form': AddJobForm(),
                    })
    else:
        try:
            form = AddJobForm(request.POST)
            newJob = form.save(commit=False)
            newJob.user = request.user
            newJob.save()
            return redirect('jobhunt:job_detail', newJob.id)
        except ValueError:
            return render(request, 'jobhunt/pages/add_job.html', {
                            'form': AddJobForm(),
                            'error': 'bad data passed in'
                        })