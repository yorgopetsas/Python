from website import create_app

app = create_app()
# When you set the debug to True the web server restarts automatically every time you make a change to the code
# In production you would want to set this to False
if __name__ == '__main__':
	app.run(debug=True)