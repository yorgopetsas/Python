from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")

@views.route("/")
def home():
	return render_template("index.html", name ="Yorgo Petsas")

# Pass query from URL using request from FLASK
@views.route("/profile")
def profile():
	args = request.args
	name = args.get('name')
	return render_template("profile.html")
	
# Return JSON: Import jsonify will convert a dictionary to JSON
@views.route("/json")
def get_json(): 
	return jsonify({'name': 'yorgo', 'age' : 24})

# Receive data in JSON format. Here we lack the funcionality that
# can send the JSON data to this route in order to test
@views.route("/data")
def get_data():
	data = request.json
	return jsonify(data)

# How to Redirect: Import redirect and url_for and use the below logic
@views.route("/go-to-home")
def go_to_home():
	return redirect(url_for("views.home"))

@views.route("/cv")	
def cv():
	return render_template("cv.html", name ="Yorgo Petsas")
	
@views.route("/pdf")
def pdf():
	return render_template("index.html", name ="Yorgo Petsas")
	
@views.route("/linkedin")
def LinkedIn():
	return render_template("linkedin.html", name ="Yorgo Petsas")
	
@views.route("/portfolio")
def portfolio():
	return render_template("index.html", name ="Yorgo Petsas")