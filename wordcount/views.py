from django.shortcuts import render
from django.http import HttpResponse
import operator

def count(req):

	fulltext = req.GET['fulltext']
	wordlist = fulltext.split()

	dictionary={}

	for word in wordlist:
		if word in dictionary:
			dictionary[word]+=1
		else:
			dictionary[word]=1


	sort= sorted(dictionary.items() , key=operator.itemgetter(1) , reverse=True)
	
	return render(req, 'count.html' , {'fulltext':fulltext , 'tedad':len(wordlist), 'dictionary': sort } )

def home(req):
	return render(req, 'home.html')

def about(req):
	return render(req, 'about.html')