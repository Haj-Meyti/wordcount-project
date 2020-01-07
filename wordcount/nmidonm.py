from django.http import HttpResponse

from django.shortcuts import render

def yechizi(kale):
	return HttpResponse('<h3>2+2</h3>')

def hamin(khiar):
	return render(khiar,'home.html',{'typing':'haar haar'})