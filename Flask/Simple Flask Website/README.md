The idea of this project is to create a website using the Flask Framework 
as fast as possible. The project was started @Jan 16, 8:44 and ended at 11:40

<b>UPDATE</b>: I spent a few more hours to add navigation and some content

The result is published as life website on the following URL:

https://cv.amanitasolutions.com

##It consist of the following stages:

I. Website Creation and Setup with Flask

###I will share some of the knowledge I gain while doing this project 

```
# Below you can see how you can take a paramenter from the URL
# putting it in triangle brackets <> and passing it to a function
@views.route("/profile/<username>")
def profile(username):
	return render_template("index.html", name=username)
```

###Next I will show you how to # Pass query parameters from URL using the <i>request</i> library from FLASK
```
@views.route("/profile")
def profile():
	args = request.args
	name = args.get('name')
	return render_template("index.html", name=name)
```
	
###Return JSON. Use jsonify will convert a dictionary to JSON
```
@views.route("/json")
def get_json():
	return jsonify({'name': 'yorgo', 'age', 24})  
```

###How to Redirect: Import redirect and url_for and use the below logic
```
@views.route("/go-to-home")
def go_to_home():
	return redirect(url_for("views.home"))
```

###In order to add JavaScript navigate to your HTML template file use the following command
```
<script type="text/javascript" src="{{ url_for('static', filename='index.js')}}"></script>
```

Template Inheritance: Flask uses the Jijna to manage templates. in profile.html we inherite 
the template from index.html through the tag "{% extends "index.html" %}" followed by the block 
and element we want to update. In this case we will update the H1 tag:
```
{% extends "index.html" %}
{% block content %}
<h1>This is the profile page</h1>
{% endblock %}
```

II. Setup of the environment in my hosting account through CPanel. 

- Configure a subdomain on the CPanel

- Setup ftp user and upload the script

- Setup DNS records for the subdomain in cloudflare

- Install and configure python app in CPanel
	- Import requirements
	- Install PIP Flask

INSPIRED BY: TIM https://www.youtube.com/watch?v=kng-mJJby8g&list=RDCMUC4JX40jDee_tINbkjycV4Sg&index=2
