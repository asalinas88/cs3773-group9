from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def profile(request):
    user = request.user
    context = {'user': user}
    template = 'profile.html'
    return render(request, template, context)
