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

app = Flask(__name__)
api = Api(app)

End of file:

if __name__ == "__main__":
	app.run(debug=True)

3. Make sure the setup is correct by running the empty app from your terminal.
We get the following confirmation:

 * Serving Flask app "main" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 170-895-724

- The important part is see the confirmation that the service is running. In this case it is on port 500
of the <b>IP:</b><i>127.0.0.1</i> (localhost). You can later update those settings. 

