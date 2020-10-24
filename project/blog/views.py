from django.shortcuts import render
# Create your views here.

def home(request):

	context = {
		'posts' : posts
	}

	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title' : 'About'})
