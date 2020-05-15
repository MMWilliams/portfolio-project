from django.shortcuts import render
from .models import Job #import jobs model/data schema

# Create your views here.
def home(request):
    #passing the data as python objects
    jobs = Job.objects

    #serving up the data objects in a dictionary
    return render(request, 'jobs/home.html', {'jobs':jobs})

