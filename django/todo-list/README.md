Custom Forms
https://www.youtube.com/watch?v=9jDEnSm4nt8&list=PLzMcBGfZo4-kQkZp-j9PNyKq7Yw5VYjq9&index=6

The website create for this project is live on my server. You can check it out at:

http://dtl.amanitasolutions.com/

We want to give the user the option to add an item to the list


Custom forms- very powerful, the most important part is to get a hang of the GET POST request

Next we are adding a sidebar by including a nav div in the base.html file and some css style

In order to load bootstrap we are going to add several thing to our base.html file:
- a "link rel="stylesheet" element in the <i>head</i> section
- three java script links just before the closing <i>body</i> tag
- Put the following class to our main div
```
class="row justify-content-center"
```

- Custom style de /create page and to the list.html file

- User registration

- To start with we are going to create a new form. Keep in mind that Django already does most
of the hard work for us. It is exactly those kind of things are why many people love Django.
	- The first step is to actually create a new app (user) to handle to login/out and registration. 
	By doing it in a seperate app you can later on re-use it with easy on any other Django project.
	to do that we go to the CLI and enter <i>python manage.py startapp register</i>
	- setup the urls in views.register
	- import the views file of the register app to the urls file in the mysite app
		```
		from register import views as v
		```
	- in urls.mysite
		```
		    path("register/", v.register, name="register"),
		```
	- create folders templates/register in the register app and add a file called register.html
	we extend the base template from the main folder the following way:
		```
		{% extends "main/base.html" %}
		```
	- setup a form inside the new HTML file:
		```
		<form method="POST" class="form-group">
			{{form}}
			<button type="submit" class="btn btn-success">Register</button>
		</form>	
		```
	- in views.register we import 3 modules (Prebuild form):
		```
		from django.contrib.auth import login, authenticate
		from django.contrib.auth.forms import UserCreationForm
		```
	- And we update the register function:
		```
		form = UserCreationForm()
		return render(reposnse, "register/register.html", {"form": form})
		```
	- Add the newly create app in the settings.main file (This step can done right after the new app was created)
		```	
		'register.apps.RegisterConfig',
		```
	- Now that we have our form ready, we need to handle the information that it send us. So we update the 
	views.register file as follows
	```
	def register(response):
	if response.method ==  "POST":
		form = UserCreationForm(response.POST)
		if form.is_valid():
			form.save()
	else:
		form = UserCreationForm()
		
	return render(response, "register/register.html", {"form": form})
	```
	- Redirect to a new page with account it created before the else statement. Don forget to import <i>redirect</i>
	
		```
				return redirect("/home")
		```
	- Add more fields to the form. New file in register - forms.py
	we create a new class that inherits from the UserCreationForm and we can add/modify as we please	
		
		
		```
		```
		
		
	- Now that we have the new class we need to import it in the views.register
		
		```
		from forms import RegisterForm

		```
		And remove the following imports
		
		```
		from django.contrib.auth import login, authenticate
		from django.contrib.auth.forms import UserCreationForm

		```
	Update views.register ot
		```
		form = RegisterForm(response.POST)
		```
	- Use crispy forms and bootstrap to improve the forms 
	- Install Crispy Forms
		
		```
		pip install django-crispy-forms
		```
	- Update settings file:
	```
	INSTALLED_APPS = [
	...
	"crispy_forms", 
	
	AND at the end
	
	CRISPY_TEMPLATE_PACK="bootstrap4"
	```
	- in register.html add 
	```
	{% load crispy_forms_tags %}
	```
	- And update the forms tag with a filter crisp
	```
	OLD
		{{ form }}
	NEW
		{{ form|crispy }}
	```
	
Control users login. We use the app of Django <i>django.contrib.auth</i>
```
file<main/urls.py>
urlpatterns = [
	...
	path('', include("django.contrib.auth.urls")),
]
```

Create a folders that will be open by the above module registration in register/template
Create login.html and fill
control what users see

Setup route to redirect after login
```
file<settings.py>

LOGIN_REDIRECT_URL = "/"
```

Setup route to redirect after logout
```
file<settings.py>

LOGIN_REDIRECT_URL = "/"
```

Show content only if we are logged in (NEEDS FIX FOR LOGIN)
```
file<base.html>

        {% if user.is_authenticated %}
        	{% block content %}
	        {% endblock %}
	    {% else %}
	    	<p><a href="/login">Please Login to see the content</a></p>
	    {% endif %}

```
		
		
User Specific pages and Access

- In models.py we add
```
from django.contrib.auth.models import User
```

- Add the following code. Essentially saying that every todo list will be linked to a user

```
class ToDoList(models.Model):
 	user = models.ForeignKey(User, on_delete = models.CASCADE)
	name = models.CharField(max_length = 200)

```

We have to make some migration in order to update the database accordingly

in shell
```
CTR-C to stop the server

python manage.py migrate
```

If that does not work you need to delete your db file, everything inside migration folder indluding the pycach 
but not the __init__.py files. That goes for all of your <i>migrations</i> folders.



- Setup that user can only see the list of his notes by :

```
```

- Limiting a user to not be able to access a list by ID in case he is not the owner of the list
```
	# Check if it is in the user list
	if ls in response.user.todolist.all():	

```



