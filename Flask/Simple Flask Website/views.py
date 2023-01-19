from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")

@views.route("/")
def home():
	return render_template("index.html", name ="Yorgo Petsas")

@views.route("/cv")	
def cv():
	return render_template("cv.html", name ="Yorgo Petsas")
	
@views.route("/linkedin")
def LinkedIn():
	return render_template("linkedin.html", name ="Yorgo Petsas")

# Pass query parameter from URL using request from FLASK
@views.route("/profile")
def profile():
	name = "Yorgo"
	age = 40
	nationality = "Bulgaria"
	args = request.args
	if args.get('name'):
	 	name = args.get('name')
	if args.get('age'):
		age =  args.get('age')
	if args.get('nationality'):
		nationality =  args.get('nationality') 
	return render_template("profile.html", name=name, age=age, nationality=nationality)

# How to Redirect: Import redirect and url_for and use the below logic
@views.route("/go-to-home")
def go_to_home():
	return redirect(url_for("views.home"))

# Return JSON: Import jsonify will convert a dictionary to JSON
@views.route("/json")
def get_json(): 
	return jsonify({'1_' : 'DESCRIPTION: This page will show how to convert dictionary to JSON data.', '2_' : '-', '3_' : 'DETAILS: The configuration is done in the views system of Flask were we need to import the  _jsonify_ library. Then we define a route and a get_json function.', '4_': '-', '5_': 'MORE DETAILS: The data is sent as dictionary, converted and dinamically visualized with a URL rule in the views.py file.', '6_' : '', '7_' : 'EXAMPLE:','_1' : '      @views.route("/json")', '_2' : '          def get_json():', '_3' : '          return jsonify(JSON_DICTIONARY)','_4':'', '_ZX' : '<BACK>  PLEASE HIT THE BACK BUTTON OF YOUR BROWSER SO YOU CAN GO BACK TO THE WEBSITE  <BACK>'})

# Receive data in JSON format. Here we lack the funcionality that
# can send the JSON data to this route in order to test
@views.route("/data")
def get_data():
	data = request.json
	return jsonify(data)

# @views.route("/portfolio")
# def portfolio():
# 	return render_template("portfolio.html", name ="Yorgo Petsas")
	        