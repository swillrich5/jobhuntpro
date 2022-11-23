from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Job

# Create your views here.
@login_required
def job_list(request):
    jobs = Job.objects.filter(user=request.user)
    return render(request, 'jobhunt/pages/job_list.html', {'jobs': jobs})

def job_detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobhunt/pages/job_detail.html', {'job': job })
