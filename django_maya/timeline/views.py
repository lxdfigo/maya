# Create your views here.
from django.core.serializers import serialize
from timeline.models import *

def getData(location, event):
	msg_list = Message.objects.filter(location = location, event = event)
	return serialize('json', msg_list)
	'''
	data = []
	for msg in msg_list:
		data.append({'location':msg.location, 'event':msg.event, })
	'''
		
