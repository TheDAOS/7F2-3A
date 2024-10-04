from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import FileUploadForm

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

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = form.save(commit=False)
            file_instance.user = request.user  # Set the user
            file_instance.save()
            return redirect('success_url')  # Redirect to a success page or file list
    else:
        form = FileUploadForm()
    return render(request, 'upload.html', {'form': form})
