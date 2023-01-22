<h1>This project aims to create a simple website with Django as fast as possible.</h1>

<h3>It is inspired by the a video published by CODEMY. I want to thank them for the content.</h3>
https://www.youtube.com/watch?v=ey8EXTjRuag&t=322s
<br />
Requerments:<br /><br />

- Setup a virtual environment<br />
- Django 4.0<br />
<br />
Step1: The first thing we do is create a virtual environment. What this basically do is limit the scope of the applications you setup to only this project. Meaning we can have one version of Django for this project and in the virtual environment of another project have another version of Django, the same goes with the version of Python and with the additional modules we install.<br /><br />

We have to navigate to the folder of the project and run the folliwing command in our terminal:

```
python3 -m venv virt
```

Then we turn it on we use this for windows:
```
source virt/Scripts/activate
```

And for Mac:
```
source virt/bin/activate
```

Then we install Django:
```
pip3 install django
```

Create new project
```
django-admin startproject mysite
```

Navigate to the newly created <i>mysite</i> folder and start the server:
```
python3 manage.py runserver
```

Test the webserver by visting the following address in your browser
```
http://localhost:8000/
```

Setup SuperUser<br />
- Gogo to the terminal and press CTRL-C in order to stop the server
- Do a migration

```
python3 manage.py migrate
```

- Create a SuperUser running the command below and follow the proccess.
```
python3 manage.py createsuperuser
```

Now you can navigate to the admin panel and login:
```
http://localhost:8000/admin/
```

Create an app:
- Stop the server (CTRL-C)
- Run python3 manage.py startapp website
- Register the app in your setting.py file 
```
INSTALLED_APPS = [
	...
	'website.apps.WebsiteConfig'
	]
```
<br />Setup the URLs
- in mysite/urls.py include the <i>include</i> module
```
from django.urls import ..., include
...
path('', include('website.urls'))
```
- Create a urls.py file in the <i>website</i> folder and add the following code:
```
from . import views

urlpatterns = [
    path('', views.index, name="index"),
]
```
<br />
In views.py add:

```
def index(request):
	return render(request, 'index.html', {})
```
<br />
Static Files (js, img, etc)<br />

- Createa static directory and them directory called website because this is the name of our app.
<br />
To use a static file in your HTML code you need to add the following snippet in the head of your template file:

```
{% load static %}
```

<br />
And then use the following sintax when you need to use the file
```
{% static 'website/style.css' %}
Example:
<link rel="stylesheet" type="text/css" href="{% static 'website/style.css' %}">
```

<br />We imported the bootstrap starter template and create a navbar again from bootstrap/components/navbar
<br /><br />
We include the navigation as a separate HTML file with the following tag:
```
{% include 'navbar.html'%}
```

<br /><br />The same way we created the view for the home page we create the following pages: <i>about, django, project</i>. The final codes for the views and urls to work are as follows:
```
file <website/urls.py>

urlpatterns = [
    path('', views.index, name="index"),
	path('about', views.about, name="about"),
	path('project', views.project, name="project"),
	path('django', views.django, name="django"),
]
```
<br /><br />
```
file <website/viewss.py>

def index(request):
	return render(request, 'index.html', {})

def about(request):
	return render(request, "about.html", {})

def project(request):
	return render(request, "project.html", {})

def django(request):
	return render(request, "django.html", {})
```