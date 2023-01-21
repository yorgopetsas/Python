from flask import Flask

def create_app():
	app = Flask(__name__)
	# We are going to secure/incript the key for the session
	#app.config['SECRET_KEY'] = 'laksjfonaoushvoanoaeetg'
	
	#from .views import views
	#from .auth import auth
	
	#app.register_blueprint(views, url_prefix='/')
	
	return app
	