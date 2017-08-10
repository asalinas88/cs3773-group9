from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import UploadFileForm


@login_required
def profile(request):
    user = request.user
    context = {'user': user}
    template = 'profile.html'
    return render(request, template, context)


def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            #handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
