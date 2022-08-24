from itertools import product
from multiprocessing import context
from django.shortcuts import redirect, render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from django.http import JsonResponse


def home(request):

    return render(request,'home/portfolio.html',)
