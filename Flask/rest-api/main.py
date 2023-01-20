from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/database.db'

db = SQLAlchemy(app)

# Define DB model. In String(100) we define the max size of the field. "nullable=False" Means can't be empty.
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

# We create an Argument creation parser with 3 mandatory fields.
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video", required=True)
video_put_args.add_argument("views", type=str, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=str, help="Likes on the video", required=True)

# We create an Argument Update parser with 0 mandatory fields.
video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of the video")
video_update_args.add_argument("views", type=str, help="Views of the video")
video_update_args.add_argument("likes", type=str, help="Likes on the video")

# Resource field is a way to define how a object should be serialized. Meaning the result will be formated 
# according to the provided structure. In this case JSON dictionary. Requiers the import of "fields"
resource_fields = {
	'id': fields.Integer,
	'name': fields.String,
	'views': fields.Integer,
	'likes': fields.Integer
}

class Video(Resource):
	# Marshal decorator. Import "marshal_with". Take the return value serialize it according to the data 
	# structure provided in resource_fields (JSON)
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
