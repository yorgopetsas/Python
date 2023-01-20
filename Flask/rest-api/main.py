from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Creating a Resource Class. Use it to overwrite the get and post requests get, post (delete) requests.
class HelloWorld(Resource):
	def get(self, name, test):
		return{"name" : name, "test" : test}

# 	def post(self):
# 		return{"data" : "Post"}

# Register the class as a resource. "/helloworld" is the endpoint. By the triangle bracets we can define 
# parameters. Examples: <i>string, int, boolean<i>. We can have multiple parameters separating them with 
# forward slash "/". Important: When making the call have to follow the order of the parameters.
api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:test>")

if __name__ == "__main__":
	app.run(debug=True)
