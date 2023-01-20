from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/database.db'

# We define the datebase just the first time we run the app in an enviroment, after that we comment it out
db = SQLAlchemy(app)

# Define model for DB. In String(100) we define the max size. nullable=False Means can't be empy
class VideoModel(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	views = db.Column(db.Integer, nullable=False)
	likes = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return f"Video(name = {name}, views = {views}, likes = {likes}])"

# IMPORTANT: Uncomment the line bellow the first time you run the program in order to create the DATABASE. 
# After that you have to comment it out or the app will overwrite your datebase with new a one each run. 
# db.create_all()

# We create a parser with 3 mandatory arguments
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video", required=True)
video_put_args.add_argument("views", type=str, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=str, help="Likes on the video", required=True)

# Update argument parser
video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of the video")
video_update_args.add_argument("views", type=str, help="Views of the video")
video_update_args.add_argument("likes", type=str, help="Likes on the video")


# Removed since we start to store in DB
# videos = {}

# Resource field is a way to define how a object should be seriolized. Need to import "fields"
resource_fields = {
	'id': fields.Integer,
	'name': fields.String,
	'views': fields.Integer,
	'likes': fields.Integer
}

class Video(Resource):
	# Marshal decorator. Import "marshal_with". When we return take the return value and serialize it using the fields from resource_fields to json
	@marshal_with(resource_fields)
	def get(self, video_id):
		result = VideoModel.query.filter_by(id=video_id).first()
		if not result:
			abort(404, message="Video with this ID does not exist.")
		return result

	#201 codes stands for "created"	, 204 "deleted sussecfully", 409 "Item Already Exists"
	@marshal_with(resource_fields)
	def put(self, video_id):
		args = video_put_args.parse_args()
		result = VideoModel.query.filter_by(id=video_id).first()
		if result:
			abort(409, message="Video creation failed, ID already taken.")
		video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
		db.session.add(video)
		db.session.commit()
		return video, 201

	@marshal_with(resource_fields)
	def patch(self, video_id):
		args = video_update_args.parse_args()
		result = VideoModel.query.filter_by(id=video_id).first()
		if not result:
			abort(404, message="Video with this ID does not exist.")
			
		if args['name']: 
			result.name = args['name']
		if args['views']:
			result.views = args['views']
		if args['likes']:
			result.likes = args['likes']

		# Once something is already in the db we don't need to add it, rather just commit it
		# That is why here we don't use "db.session.add(result)"
		db.session.commit()
		
		return result

	def delete(self, video_id):
		abort_vid_missing(video_id)
		del videos[video_id]
		return '', 204
		
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
	app.run(debug=True)

# PROGRESS # https://www.youtube.com/watch?v=GMppyAPbLYk&list=RDCMUC4JX40jDee_tINbkjycV4Sg&index=6
#
# We are going to create an program that will return to us information about a video, when we sent the video ID
# On a second phase I will rewrite this so it works for my ecommerce website where I will ask for information 
# regarding the product based on product ID. I will then combine it will
# ARGUMENTS

# the help arguments is like an error that will be displaied to the user/sender

# 		return request.form['likes']

#		request.method # this will tell us that it is put request
# 		self.likes
# 		self.name
# 		self.id

# NOTE
#Thanks Tim for the great video.
#At minute 30:59, if anyone else gets the following error: "{'message': 'Failed to decode JSON object: Expecting value: line 1 column 1 (char 0)'}" to fix it you need to add: location='form' to the line of code: "parser.add_argument('likes', type=int, help='likes of the video')" to tell the request parser to look only in the post body for the data that PUT request needs to parse.

# Instead of using the request library we will use a library called reqparse which is much better for this app

# Creating a Resource Class. Use it to overwrite the get and post requests get, post (delete) requests.
# class HelloWorld(Resource):
# 	def get(self, name):
# 		return names[name]

# 	def post(self):
# 		return{"data" : "Post"}

# names = {"tim": {"age": 19, "gender": "male"},
# 		"bill": {"age": 27, "gender": "male"}}


# Register the class as a resource. "/helloworld" is the endpoint. By the triangle bracets we can define 
# parameters. Examples: <i>string, int, boolean<i>. We can have multiple parameters separating them with 
# forward slash "/". Important: When making the call have to follow the order of the parameters.
# api.add_resource(HelloWorld, "/helloworld/<string:name>")

#Abort if we try to locate an item that does not exist. We need to add the abort module to the import line
# def	abort_vid_missing(video_id):
# 	if video_id not in videos:
# 		abort(404, message="Video ID missing or not valid")
# 
# def abort_if_vid_exists(video_id):
# 	if video_id in videos:
# 		abort(409, "Video Already exists!")

# 		return videos[video_id], 201
# 		abort_if_vid_exists(video_id)
# 		args = video_put_args.parse_args()
# 		videos[video_id] = args

		#abort_vid_missing(video_id)
		#return videos[video_id] 
