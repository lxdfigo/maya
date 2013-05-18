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
from django_maya.settings import *
import datetime, json, string, uuid


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
	

def addWallJSON(msg_type, msg):
	json_loc = '%swall.json' % MEDIA_ROOT
	fp = open(json_loc, 'r')
	data = json.loads(fp)
	fp.close()

	if msg_type == 'file':
		data.append({'type' : 'file', 'location' : MEDIA_URL + msg})
	if msg_type == 'comment':
		data.append({'type' : 'comment', 'comment' : msg})

	fp = open(json_loc, 'w')
	fp.write(json.dumps(data), indent = 4)
	fp.close()
		
		

def postMessage(request):
	#check file:
	if 'file' in request.FILES:
		f = request.FILES['file']
		fname = uuid.uuid4()
		ftype = f.name[f.name.find('.') + 1: ]
		loc = '%s%s.%s' % (MEDIA_ROOT, fname, ftype)
		fp = open('%s%s.%s' % (MEDIA_ROOT, fname, ftype), 'wb')
		for chunk in f.chunks():
			fp.write(chunk)
		fp.close()
		addWallJSON('file', loc)
	if 'comment' in request.POST:
		addWallJSON('comment', request.POST['comment'])
		
		
	
	
	
	

	
