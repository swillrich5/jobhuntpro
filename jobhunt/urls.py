from django.urls import path
from . import views

app_name = 'jobhunt'

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('detail/<int:job_id>', views.job_detail, name='job_detail'),
    path('detail/<int:job_id>/create/', views.add_contact, name="add_contact"),
    path('detail/<int:job_id>/add/', views.add_activity, name="add_activity"),
]