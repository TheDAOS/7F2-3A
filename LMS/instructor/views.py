from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from homeapp.models import User_types
from .forms import FileUploadForm


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
        return redirect('/redirect/')

# Testing file upload
# new_file = File.objects.create(user=user, file_path='/images/photo1.jpg', file_type='image')
@login_required
def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = form.save(commit=False)
            file_instance.user = request.user  # Set the user
            file_instance.save()
            return redirect('instructor_dashboard')  # Redirect to a success page or file list
    else:
        form = FileUploadForm()
    return render(request, 'upload.html', {'form': form})