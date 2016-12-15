from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render
import datetime

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "In %s hour(s), it will be %s." % (offset, dt)
	return HttpResponse(html)

def hours_ahead2(request, offset):
	try:
		offset = int(offset)
	except:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	return render(request, 'hours_ahead.html', {
		'hour_offset': offset,
		'next_time': dt,
	})

def hello(request):
	return HttpResponse("Hello World")

def current_datetime(request):
	now = datetime.datetime.now()
	return render(request, 'current_datetime.html', {'current_date': now})

def current_datetime2(request):
	now = datetime.datetime.now()
	t = get_template('current_datetime.html')
	html = t.render(Context({'current_date': now}))
	return HttpResponse(html)

def inherit_test(request):
	return render(request, 'inherit.html')