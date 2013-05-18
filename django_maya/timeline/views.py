# Create your views here.
from django.core.serializers import serialize
from timeline.models import *
import json


def getJSON(location, event):
	location.replace(' ', '')
	event.replace(' ', '')
	fp = open('%s_%s.json'%(location, event), 'r')
	return json.loads(fp)
	'''
	data = []
	for msg in msg_list:
		data.append({'location':msg.location, 'event':msg.event, })
	'''
		
