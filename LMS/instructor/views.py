from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from homeapp.models import User_types
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def instructor_dashboard(request):
    user_type = User_types.objects.get(user_id=request.user.id)

    # Check if the user is an instructor (user_type = 'INS')
    if user_type.user_type == 'INS':
        template = loader.get_template('dashboard.html')
        context = {
            'username': request.user.username,
        }
        return HttpResponse(template.render(context, request))
    else:
        return redirect('/Redirect/')
