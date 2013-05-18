from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.contrib import auth
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sessions.models import Session
from django.http import HttpResponseRedirect
import datetime, json, string


def home(req):
	    return HttpResponse("Hello+ world!")

def place(request):
	#check location:
	location = 'Yahoo! Beijing'
	if 'loc' in request.GET:
		location = request.GET['loc']

	#check event:
	event = None
	if 'event' in request.GET:
		event = request.GET['event']
	#query database
	reponse_data = timeline.getData(location, event)
	#return json
	return HttpResponse(json.dumps(response_data), content_type = 'application/json')
	
	

	
