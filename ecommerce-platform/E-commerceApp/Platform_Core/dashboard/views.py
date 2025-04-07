from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_home(request):
    if request.user.role != 'seller':
        return redirect('home')
    return render(request, 'dashboard/dashboard_home.html')

