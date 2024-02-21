from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='login')
def index(request):
    user = request.user
    return render(request, 'index.html', {'user': user})
