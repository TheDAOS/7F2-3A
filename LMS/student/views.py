from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User

def student_dashboard(request):
    if request.user.is_authenticated:
        template = loader.get_template('student_dashboard.html')

        # user = User.objects.get(username=request.user.username)

        context = {
            'username' : request.user.username,
        }

        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse("You are not logged in.")