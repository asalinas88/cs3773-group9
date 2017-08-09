from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import Patient
from users.forms import UploadForm


@login_required
def profile(request):
    user = request.user
    context = {'user': user}
    template = 'profile.html'
    return render(request, template, context)


def upload(request):
    successful = False

    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            patient = Patient()
            patient.title = form.cleaned_data['title']
            patient.file = form.cleaned_data['file']
            patient.save()
            handle_uploaded_file(request.FILES['file'])
            successful = True
    else:
        form = UploadForm()
    return render(request, 'success.html', locals())


def handle_uploaded_file(f):
    with open('chunk_file.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
