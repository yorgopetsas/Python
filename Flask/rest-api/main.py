from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Creating a Resource class that we will use for handling get, post, delete requests.
class HelloWorld(Resource):
	def get(self):
		return{"data" : "Hello World"}
	# Next step we overwrite the post request and test it.
	def post(self):
		return{"data" : "Post"}


#Register the class as a resource. "/helloworld" is the endpoint
api.add_resource(HelloWorld, "/helloworld")


if __name__ == "__main__":
	app.run(debug=True)
