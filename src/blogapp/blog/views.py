from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
posts = [
	{
		'author'		:'hrishi jadhav',
		'title'			:'blog post 1',
		'content'		:'First post content',
		'date_posted'	:'january 13,2020'
	},
	{
		'author'		:'corey schafer',
		'title'			:'blog post 2',
		'content'		:'Second post content',
		'date_posted'	:'february 13,2020'
	}
]
def Home(request):
	context={
		'posts':posts
	}
	return render(request, 'blog/home.html',context)
def About(request):
	return render(request, 'blog/about.html',{'title':'about'})