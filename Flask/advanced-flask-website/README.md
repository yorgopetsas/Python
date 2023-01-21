Video Overview 
Project Demo
Directory Structure
Flask Setup & Installation
Creating a Flask App
Creating Routes/Views
Jinja Templating Language & HTML Templates
Sign Up Page HTML 
Login Page HTML
HTTP Requests (POST, GET, etc.)
Handling POST Requests
Message Flashing
Flask SQLAlchemy Setup
Database Models
Foreign Key Relationships
Database Creation
Creating New User Accounts
Logging In Users 
Flask Login Module
Checking if User is Logged In
Notes HTML
Adding User Notes
Deleting User Notes

After making sure you have Flask installed you need to install the flask-login module "pip/3 install flask-login"

Next thing you need to install is flask-sqlalchemy


This README file include extensive details on how to setup different part of a website/app in the Flask Framework
and can be actually used as a General Manual for website creation with Flask.

____________________________________



Flask Web App Tutorial
Setup & Installtion
Make sure you have the latest version of Python installed.

git clone <repo-url>
pip install -r requirements.txt
Running The App
python main.py
Viewing The App
Go to http://127.0.0.1:5000


____________________________________

Step:
Define this file is a blueprint file which actually means that this
file is has a bunch of routes/url. IT also allows us to have the URL structure
distribute among different files in case this helps the organization (size / organizarion needs)
In our case we are going to setup the URLs related to autorized actions in the <i>auth.py</i> file

```
views = Blueprint('views', __name__)
```

Step:

Next we have to register those views. We are going to do that by importing the blueprint files 
like this: <i>from .views import views</i> in the <i>__init__.py</i> file and then registering them like this

```
app.register_blueprint(views, url_prefix='/')
```

Step: 

We are going to etup the templates. Flask uses a framework Jinja which allows us to manage the HTML templates
with Python and now JS knowledge/use. We define base.html file that is the base design/template and with each 
next file we are going to overwrite different parts of the base template depending on the case.

Step: 

After defining the meta tags in the head section of the template we are going to import CSS Framework 
<b>Bootstrap</b>. If you are not familiar with what Bootstrap is I invite you to look that up online.

```
file: <base.html>
<link
      rel="stylesheet"
      href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
      integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
      crossorigin="anonymous"
    />
    <link
      rel="stylesheet"
      href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"
      crossorigin="anonymous"
    />
```



Below is the first part of the template which we will manipulate with Jinja syntax:

The child templates overwrite the parent tempalte (base in this case).In the example we overwrite the title tag

```
<title>{% block title %}Home{% endblock %}</title>
```

In Jinja we have a few syntax options:

```
{% YOUT PYTHON CODE HERE %}

OR

{{ YOUR PYTHON EXPRESSION }} - Addiional rules apply
```


Step: Load the JS for Bootstrap just before the closing body tag 

```
</body>
```

If you want to use your own files (.js, images, etc) you need to upload them to the "static" forlder and use
the following syntax:

```
{{ url_for('static', filename='index.js') }}

```

Step: Define navigation bar (using Bootstrap CSS classes):

```
file: <base.html>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbar">
	<span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbar">
	<div class="navbar-nav">
	  {% if user.is_authenticated %}
	  <a class="nav-item nav-link" id="home" href="/">Home</a>
	  <a class="nav-item nav-link" id="logout" href="/logout">Logout</a>
	  {% else %}
	  <a class="nav-item nav-link" id="login" href="/login">Login</a>
	  <a class="nav-item nav-link" id="signUp" href="/sign-up">Sign Up</a>
	  {% endif %}
	</div>
  </div>
</nav>

```

Step: Define which HTML documents can use the base template
- Make new template: home.html
- Setup the new template to use the base template with the following code:
	```
	{% extends "base.html" %}
	```

Import the <i>render_template</i> module from Flask and in the views function we are going to rendeer the template


```
file: <auth.html>
@views.route('/')
def home():
	return render_template("home.html")

```

We setup the navigation 

Sending variables through the Janji: <i>return render_template("login.html", text = "Testing")</i>. 
You can send as many variable es you want

```
file: <auth.html>
@auth.route('/login')
def login():
	return render_template("login.html", text = "name")

```  

Inside of the template (login.html in this case) you can access the variable like this, where <i>text</i> is 
the name of the variable:


```

{{ text }}

```

Extra: You can perform Python operation and manipulate the passed data. 
In the example below you will add the letter "s" to the string in text, so if text = name the result willl be "names":
There are limitation but you can do most of the basic operations.
```

{{ text + "s"}}

```

Step: 

How to write if statement inside of the template

First we can pass a boolean through the render_template function

```
file: <auth.html>
@auth.route('/login')
def login():
	return render_template("login.html", text = "name", boolean=True)

```

Then in the template file use the <i>{% %}</i> tag. Only one <i>{% endif %}</i> is neccesary:

```
file: <login.html>
{% if boolean == True%}
	Yes it is true.
{% else %}
	No, it is not true.
{% endif %}
```


Step: Create the Sign Up page/form. In <i>sign_up.html</i> we create a simple <b>HTML</b> form, use the 
<br /><i>POST</i> method and apply css style from <b>Bootstrap</b>.


By default we can only accept GET requests (for security reasons) so in order to accept <i>POST</i> request we
<br />do the following:

```
file: <auth.py>
@auth.route('/login', methods=['GET', 'POST'])
``` 

Now to GET the information that was sent (posted) by the form we have to import the <i>request</i> module and 
<br />add this code:

```
file: <auth.py>
data = request.form
```

You can include the following like below in order to print the content of the POST request in the terminal 
where your web server(Flask) is running

```
print(data)
```

Next Chapter is to save the data from the POST request in a database

- Before we save the data we have to check if it is valid. We do the following: 

```
if len(email) < 4:
			pass
		elif len(firstName) < 2:
			pass
		elif password1 != password2:
			pass
		elif len(password1) < 7
			pass
		else:
```



Flask Flash Message: Import <i>flash</i>. To flash the user with a message we need to use the syntax you can
<br /> see below: 

```
	flash('Account Created', category='success')
OR
	flash('Passwords don\'t match ', category='error')
```
And then you need to add the following to your template. Below is example for an Error Alert: 

```
file: <base.html>
    {% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
    	{% for message in messages %}
    		<div class="alert alert-danger alert-dismissable fade show" role="alert">
    			{{ message }}
    			<button type="button" class="close" data-dismiss="alert">
    				<span aria-hidden="true">&times;</span>
    			</button>
    		</div>
    	{% endfor %}
    {% endwith %}
```

```
<div class="alert alert-success alert-dismissable fade show" role="alert">
    			{{ message }}
    			<button type="button" class="close" data-dismiss="alert">
    				<span aria-hidden="true">&times;</span>
    			</button>
    		</div>
```

And to combine those with if statement inside the HTML template we do the following:

```

{% with messages = get_flashed_messages(with_categories=true) %}
	{% if messages %}
		{% for category, message in messages %}
			{% if category == 'error' %}    		
				<div class="alert alert-danger alert-dismissable fade show" role="alert">
					{{ message }}
					<button type="button" class="close" data-dismiss="alert">
						<span aria-hidden="true">&times;</span>
					</button>
				</div>
			{% else %}
				<div class="alert alert-success alert-dismissable fade show" role="alert">
					{{ message }}
					<button type="button" class="close" data-dismiss="alert">
						<span aria-hidden="true">&times;</span>
					</button>
				</div>
			{% endif %}
		{% endfor %}
	{% endif %}
{% endwith %}
    
```

Step: Setup your DataBase
- In <i>__init__.py</i> import <b>SQLAlchemy</b>

```
from flask_sqlalchemy import SQLAlchemy
```

Then we create a database:

```
db = SQLAlchemy()

```

We set a variable to point to the <i>database.db</i> file in the <i>database</i> directory:
```
DB_NAME = "database/database.db"
```

Next we configure the database in our <i>def create_app():</i>function:
```

	app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
```

Then we are going to initializa the DB in the same function:

```
	db.init_app(app)
```

Now we are going to define de DB Model (scheme). We will create two models: one for our yours and one for notes 


This means from this package (this being our app) import the db (found in the <i>__init__.py</i> file)
```
from . import db
```

Next we import: 
```
from flask_login import UserMixin
```

Define the DB colums like this. First we define a class for the model

Then we use this 

```
file <modules.py>

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(150), unique=True)
	...
	notes = db.relationship('Note')	

class Note(db.Model):
	...
	date = db.Column(db.DateTime(timezone=True), default=func.now())
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	


```
Notes: 
- <i>primary_key=True</i> means that this will be the field/column that will be used to diferantiate the
different elements in this table. I other words this will be the Unique ID!
- <i>unique=True</i> means no user can have the same email. 
* Now I understand it is hard to see the difference but the first one is related to the way you manage your
SQL database and the second is more of an input filter.
- <i>String(150)</i> means that the string can be maximum 150 charecters
- from <i>sqlalchemy.sql import func<i> in combination with <i>default=func.now()</i>will import the data/time for us
- Associate the notes with a user. We need to setup a relationship between both objects. We do this with a 
<i>foreign_key</i> it is essentianl a column in your db table that contains the <i>primery_key / id<i> of an 
item in another table. So what we do is store the <i>id</i> of the user that stores this note. Classic one to
many relations ship (one user has many notes). 
- </i>notes = db.relationship('Note')</i> Tells flask/sql every time a note is created add to this notes 
relationship. This will be a list of all of the id of the users notes  

MOVE THE VARIABLES TEST ON SEPARATE URL TEST.HTML

Step: Just now we are ready to actually create the database. For the purpose we prepare a script that will check
before you run the server if we have created the DB here.

Step: Create an account;

- We need to
```
import from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
```

 Note: The password hash is converted version of the password so it can't be stolen on its way from the client
 computer to the server. We use hash function which is basically an non-inverse function, again for use this 
 for security reasons




#define user
			new_user = User(email=email, firstName=firstName, password=generate_password_hash(password1, method='sha256') 
			#add user to the DB
			db.session.add(new_user)
			db.session.commit()

Then we sign the user in and redirect them to the home page			

Import redirect and url_for





Step: Login



/ 		#Check the email is not in use


Flask Login Module
```
file <auth.py>
from flask_login import login_user, login_required, logout_user
```

The actuall login is done with
```
file <auth.py>
	login_user(user, remember=True)
```
- <i>remember=True</i> keeps the user logged in unless browser history is deleted or web server restarted



Step: Logout

```
	logout_user()
```

We also setup that the Logout is accessible only if you are logged in. We do it with the following decorator
for the <i>logout</i> function.

```
@login_requiered
```

We also limit the access to the Home Page if you are not logged in as follows:
```
file <views.py>
@views.route('/')
@login_required()
def home():
	return render_template("home.html")
```

To actually manage the loged in users we import in <i>__init__.py</i>:
```
from flask_login import LoginManage
```




Check if user is loged in: we are going to pass to our home template the current_user data
```
file <views.pu>	
	return render_template("home.html")
```


Step: Creating Notes: we are going to put a form on the homepage. For this step we use all of the techniques 
we learned until here. The changes are as follows. Keep in mind on several places we need to add the 
corresponding modules as we did until now.

```
file <views.py>

from flask import request, flash 
from .models import Note
from . import db

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
	if request.method == 'POST':
		note = request.form.get('note')
		
		if len(note) < 1:
			flash('Note is to short!', category='error')
		else:
			new_note = Note(data=note, user_id=current_user.id)
			db.session.add(new_note)
			db.session.commit()
			flash('Note Added!', category='success')
	return render_template("home.html", user=current_user)
 
 

```

```
file <home.html>

<ul class="list-group list-group-flush" id="notes">
	{% for note in user.notes %}
	<li class="list-group-item">
		{{ note.data }}
	</li>
	{% endfor %}
</ul>

<form method="POST">
	<textarea name="note" id="note" class="form-control"></textarea><br />
		<div align="center">

			<button type="submit" class="btn btn-primary">Add Note</button>	
		</div>
	
</form>


```


Step: Delete a note. To delete the note we are adding a small button on each note. The code for the button is
visible bellow:
```
```
In order to have it work in such fancy way (the JS sends a request to the back-end with refresh required) we 
are going to use a JavaScript that we will write on our own.

˜˜˜
functions deleteNote(noteId) {
	fetch('/delete-note', {
		method: 'POST',
		body: JSON.stringify({ noteID: noteId}),
	}).then((_res) => {
		window.location.href = "/";
	});
}
˜˜˜

- At the end we are going to add another view 
```
@views.route('/delete-note', methods=['POST'])
def delete_note():
	note = json.loads(request.data)
	noteID = data['note']
	note = Note.query.get(noteId)
	if note:
		if note.user_id == current_user.id:
			db.session.delete(note)
			db.session.commit()
			return jsonify({})
```
- Look for the note id. We send the request through the data parameter in the request object so we need to 
load it as JSON. therefor we need to <i>import json</i>
```
import json
``` 
- 	so here we take the string that the JS send us and return it as Python dictionary object and last we find
	 this note

- We also do a check that the note we want to delete is owned by the current user
```
	if note:
		if note.user_id = current_user.id
			db.session.delete
``
- For <i>return jsonify({})</ i> we need to import jsonify. This actually returns an empty reponse as we need 
to return something in the views