1. We install the necesarry packages:
- aniso8601==8.0.0
- click==7.1.2
- Flask==1.1.2
- Flask-RESTful==0.3.8
- Flask-SQLAlchemy==2.4.3
- itsdangerous==1.1.0
- Jinja2==2.11.2
- MarkupSafe==1.1.1
- pytz==2020.1
- six==1.15.0
- SQLAlchemy==1.3.18
- Werkzeug==1.0.1

2. Initiate an app inside of an Api:

Start of file
```
app = Flask(__name__)
api = Api(app)
```
End of file:
```
if __name__ == "__main__":
	app.run(debug=True)
```

3. Make sure the setup is correct by running the empty app from your terminal. You should get something like: 
<i>
 * Serving Flask app "main" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
     Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 170-895-724
</i>
<br /><br />- The important part is see the confirmation that the service is running. In this case it is on 
port 5000 of the <b>IP:</b><i>127.0.0.1</i> (localhost). You can later update those settings. <br />

- Creating a Resource Class. 

- Use it to overwrite the get and post requests get, post (delete) requests.

- Create test.py and test.

- Register the class as a resource. "/helloworld" is the endpoint

```
api.add_resource(HelloWorld, "/helloworld")
```

4. Specify parameters for the requests. Register the class as a resource. "/helloworld" is the endpoint. 
By the triangle bracets we can define  parameters. Examples: <i>string, int, boolean</i>. 
We can have multiple parameters separating them with  forward slash "/". <b>Important</b>: When making the call have 
to follow the order of the parameters.
```
api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:test>")
```
UN-ORDERED:


# We are going to create an program that will return to us information about a video, when we sent the video ID
# On a second phase I will rewrite this so it works for my ecommerce website where I will ask for information 
# regarding the product based on product ID. I will then combine it will
# ARGUMENTS

# the help arguments is like an error that will be displaied to the user/sender

# 		return request.form['likes']
#		request.method # this will tell us that it is put request

####At minute 30:59, if anyone else gets the following error: "{'message': 'Failed to decode JSON object: Expecting value: line 1 column 1 (char 0)'}" to fix it you need to add: location='form' to the line of code: "parser.add_argument('likes', type=int, help='likes of the video')" to tell the request parser to look only in the post body for the data that PUT request needs to parse.

# Instead of using the request library we will use a library called reqparse which is much better for this app

# Creating a Resource Class. Use it to overwrite the get and post requests get, post (delete) requests.
# class HelloWorld(Resource):
# 	def get(self, name):
# 		return names[name]

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

# PROGRESS # https://www.youtube.com/watch?v=GMppyAPbLYk&list=RDCMUC4JX40jDee_tINbkjycV4Sg&index=6


<b>INSPIRED BY</b>: TIM from Tech with TIM:
https://www.youtube.com/watch?v=GMppyAPbLYk&list=RDCMUC4JX40jDee_tINbkjycV4Sg&index=6