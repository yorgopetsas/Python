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
In our case we are going to setup the URLs related to autorized actions in the auth.py file

```
views = Blueprint('views', __name__)
```

Step:

Next we have to register those views. We are going to do that by importing the blueprint files 
like this "from .views import views" in the "__init__.py" file and then registering them like this

```
app.register_blueprint(views, url_prefix='/')
```

Step: 

We are going to etup the templates. Flask uses a framework Jinja which allows us to manage the HTML templates
with Python and now JS knowledge/use. We define base.html file that is the base design/template and with each 
next file we are going to overwrite different parts of the base template depending on the case.

Step: 

After defining the meta tags in the head section of the template we are going to import CSS Framework <b>Bootstrap</b>. If you are
not familiar with what Bootstrap is I invite you to look that up online.

```
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



  