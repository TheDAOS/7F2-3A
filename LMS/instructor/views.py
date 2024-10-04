from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User

def instructor_dashboard(request):
    if request.user.is_authenticated:
        template = loader.get_template('dashboard.html')

        # user = User.objects.get(username=request.user.username)

        context = {
            'username' : request.user.username,
        }

        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse("You are not logged in.")


# new_file = File.objects.create(user=user, file_path='/images/photo1.jpg', file_type='image')