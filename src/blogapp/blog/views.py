from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Home(request):
	return HttpResponse('<h1>BLOG HOME</h1>')
def About(request):
	return HttpResponse('<h1>BLOG ABOUT</h1>')	