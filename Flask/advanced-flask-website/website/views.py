from flask import Blueprint, 

# Define this file is a blueprint file which actually means that this
# file is has a bunch of routes/url. IT also allows us to have the URL structure
# distribute among different files in case this helps the organization (size / organizarion needs)
# In our case we are going to setup the URLs related to autorized actions in the auth.py file
#views = Blueprint('views', __name__)

@views.routes('/')
def home():
return "<h1>Test</h1>"
	
# Next we have to register those views. We are going to do that by importing the blueprint files 
# like this "from .views import views" in the "__init__.py" file and then registering them like this
# app.register_blueprint(views, url_prefix='/')
# 

