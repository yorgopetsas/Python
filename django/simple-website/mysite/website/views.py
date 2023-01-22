from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'index.html', {})

def about(request):
	return render(request, "about.html", {})

def project(request):
	return render(request, "project.html", {})

def django(request):
	return render(request, "django.html", {})
