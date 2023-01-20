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
app = Flask(__name__)<br />
api = Api(app)
```
End of file:
```
if __name__ == "__main__":<br />
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
- The important part is see the confirmation that the service is running. In this case it is on port 500
of the <b>IP:</b><i>127.0.0.1</i> (localhost). You can later update those settings. 

- Creating a Resource Class. 

- Use it to overwrite the get and post requests get, post (delete) requests.

- Create test.py and test.

- Register the class as a resource. "/helloworld" is the endpoint

```
api.add_resource(HelloWorld, "/helloworld")
```

4. Specify parameters for the requests. Register the class as a resource. "/helloworld" is the endpoint. By the triangle bracets we can define 
# parameters. Examples: <i>string, int, boolean<i>. We can have multiple parameters separating them with 
# forward slash "/". Important: When making the call have to follow the order of the parameters.
```
api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:test>")
```

INSPIRED BY: TIM from Tech with TIM:
https://www.youtube.com/watch?v=GMppyAPbLYk&list=RDCMUC4JX40jDee_tINbkjycV4Sg&index=6