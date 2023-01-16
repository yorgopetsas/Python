The idea of this project is to create a website using the Flask Framework 
as fast as possible. The project was started @Jan 16, 8:44 and ended at

I will share some of the knowledge I gain while doing this project 

```
# Below you can see how you can take a paramenter from the URL
# putting it in triangle brackets <> and passing it to a function
@views.route("/profile/<username>")
def profile(username):
	return render_template("index.html", name=username)
```