from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
import datetime
import string
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.contrib import auth
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sessions.models import Session
from django.http import HttpResponseRedirect


def home(req):
	    return HttpResponse("Hello world!")
