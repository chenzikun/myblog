from django.shortcuts import render
from django.http import HttpResponse

from .models import User


def home_page(request):
    users = User.objects.order_by('age').all()
    return render(request, 'blog/index.html', users)
