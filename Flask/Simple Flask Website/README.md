<h1>Simple Flask Website</h1>
The idea of this project is to create a website using Flask as fast as possible. 
The project was started @Jan 16, 8:44 and ended at 11:40
<br /><br />
<b>UPDATE</b>: I spent 2 additional hours making the documentation, adding navigation and content.

The result is published as life website on the following URL:

https://cv.amanitasolutions.com

<h2>It consist of the following stages:</h2>

I. Website Creation and Setup with Flask

II. Views.py: Setup of the URL rules the templates and the content. 

On each page of this site I have tried to represent different functionalities and short explanation on how to set them up in Flask

1. <b>Home</b>: Here we setup a basic template with navigation after creating the app, import the following libraries <i>Blueprint</i>, <i>render_template</i>, <i>request</i>, <i>jsonify</i>, <i>redirect</i>, <i>url_for</i> and setup the @views

2. <b>Profile</b>: On this page you can see how we can pass parameter queries thought the URL, using the <i>request</i> library which will dinamically use them to filter and display data. To do the test you simply need to simply add a question mark "?" followed by the parameter name, followed by "=" and the value. Before any next parameter simply add the "&" charecter.

Parameters:

```
name=NAME
age=AGE
nationality=NATIONALITY
```

Example:

```
/profile?<b>name=john&age=dough&nationality=usa</b>

```

The setup in views.py with predefined default values is as follows:

```
@views.route("/profile")
def profile():
     name = "Yorgo"
     age = 40
     nationality = "Bulgaria"
     args = request.args
     if args.get('name'):
         name = args.get('name')
     if args.get('age'):
         age = args.get('age')
     if args.get('nationality'):
         nationality = args.get('nationality')
     return render_template("profile.html", name=name, age=age, nationality=nationality)
```

3. <b>LinkedIn</b>: This page we show you how we inherit the template used in the home page, we overwrite the content block while leaving everything else untouched. Flask uses the Jijna to manage templates and the way to configure it to start the new templates with the following tag:


```
{% extends "index.html" %}
```

And we then add the things we want to overwrite. In the example below we update the the H1 tag:

```
{% block content %}
<h1>This is the profile page</h1>
{% endblock %}

```

Additionally you can see an alternative way to embbed some of my IT related posts in my LinkedIn profile. 

4. <b>CV</b>: On this page I have embedded my CV through <i>iframe</i> HTML tag.

5. <b>Go To Home</b>: Redirects are important part of any big and dynamic website, here you can see some basic redirections with Flask. We use the <i>redirect</i> and <i>url_for</i> libraries and set it up as follows:

```
    @views.route("/go-to-home")
    def go_to_home():
        return redirect(url_for("views.home"))
```

6. <b>JSON</b>: This page will show the posibility to convert dictionary to JSON data and display it. You need to use the <i>jsonify</i> library which will convert a dictionary to JSON. Views.py setup below:

```
	@views.route("/json")
	def get_json(): 
		return jsonify({'1_' : 'DESCRIPTION: This page will show how to convert dictionary to JSON data.', '2_' : '-', '3_' : 'DETAILS: The configuration is done in the views system of Flask were we need to import the  _jsonify_ library. Then we define a route and a get_json function.', '4_': '-', '5_': 'MORE DETAILS: The data is sent as dictionary, converted and dinamically visualized with a URL rule in the views.py file.', '6_' : '', '7_' : 'EXAMPLE:','_1' : '      @views.route("/json")', '_2' : '          def get_json():', '_3' : '          return jsonify(JSON_DICTIONARY)','_4':'', '_ZX' : '<BACK>  PLEASE HIT THE BACK BUTTON OF YOUR BROWSER SO YOU CAN GO BACK TO THE WEBSITE  <BACK>'})

```

II. Setup of the environment in my hosting account through CPanel. 

- Configure a subdomain on the CPanel

- Setup ftp user and upload the script

- Setup DNS records for the subdomain in cloudflare

- Install and configure python app in CPanel
	- Import requirements
	- Install PIP Flask

INSPIRED BY: TIM from Tech with Tim:<br />
https://www.youtube.com/watch?v=kng-mJJby8g&list=RDCMUC4JX40jDee_tINbkjycV4Sg&index=2


