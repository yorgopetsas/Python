In this project we are creating an API that will manage the books for a small book shop.

The result of this work can be tested live on the following link

http://django-rest-api.amanitasolutions.com/

INSTRUCTIONS:

On the website you can use the graphical interface to interact with the REST API so you can see the funcionalities and test it. In real world you would want to develop a solution that will handle big amount of
automated API calls and not do manual one by one calls.

- MAKE A GET REQUEST:
 - Get a list of all of the book and their details in JSON format:
 - <endpoint> https://django-rest-api.amanitasolutions.com/

 - Get the details of a specific book by adding the ID to the end of the URL 
 - <endpoint> https://django-rest-api.amanitasolutions.com/books/1
 
 - If you to with an ID that does not exist you will see a <b>HTTP 404 Not Found</b> response

- MAKE A POST REQUEST
 - To create a new entre/book via the API please navigate to:

 https://django-rest-api.amanitasolutions.com/books/
 
 - Then update use the following JSON template, paste it in the <i>Content</i> fields and click "POST". 
	```
	{
		"title": "Book Title",
		"number_of_pages": 100,
		"publish_date": "2021-01-10",
		"quantity": 100
	}
	```
 - On successful creation you will receive a HTTP 200 OK response and a JSON with the data you submited.

- MAKE A PUT REQUEST
 - To PUT (update) in a existing item, please navigate to it by its ID 
 - <endpoint> https://django-rest-api.amanitasolutions.com/books/1
 
 - To send the PUT request use JSON formating. For example if you want to update the available quantity get the template from below, update the quantity, pastethe snippet in the <i>Content</i> field and click PUT. 
 - If book is deleted you will get a <b>HTTP 204 No Content</b> response
```
{
    "title": "Harry Potter",
    "number_of_pages": 300,
    "publish_date": "2021-01-10",
    "quantity": 55
}
```
- MAKE A DELETE REQUEST:
 - Simply navigate to the book you want to delete and click on the DELETE button at the top right corner. Of
 course you can also send this request with code

- OTHERS:

<h2>How has this REST API build?<h2>

- I developed the application on a hosting with CPanel. Because this is educational project which most people would do on a personal computer I I haven't provided some of the setup steps like: configuring the Python Application, the Virtual Environment, reseting them from time to time to have some URL and database changes taka effect. In case you are trying to use this as a tutorial do not hesitate to drop me a line if you need help.

- After creating the virtual environment (we have selected to work with Python 3.8), we are going to intsall Django
```
pip install django
```

- Then we are going to start the new project
```
django-admin startproject books
```
- Next we are going to create a new application
```
python manage.py startapp book_api
```

- The first topic we are going to cover are the models. Those are the database models we need to setup depending on our needs
In other words translate the data from Python to SQL
```
class Book(models.Model):
	title = models.CharField(max_lenght=100)
	number_of_pages = models.IntegerField()
	publish_date = models.DateFeild()
	quantity = models.IntegerField()
	
	def __str__(self):
		return self.title
```
commit 

- In order to setup the end point at which we can access this class we are going to work with the views
book_api/views.py

```
from book_api.models import Book
from django.http import JsonResponse

def book_list(request):
	books = Book.objects.all()  #Will Return Complex Data and we need to convert to Python data type, dictionary for example
	books_python = list(books.values()) # This is Python Data Structure 
	# Convert the Python Data Structure to JSON
	# Import JsonResponse
	return JsonResponse ({
		'books': books_python
	})
	
```

- Next we create and setup the URL's in urls.py
```
from django.contrib import admin
from django.urls import path
from book_api.views import book_list

urlpatterns = [
    path('list/', book_list),
]

```

- And then we connect to the projects URL's. With the include the <i>include</i> method from the django.urls module. we are going to include the urls from book_api_
```

from django.urls import ..., include

urlpatterns = [
 	...
    path('books/', include('book_api.urls'))
]

```

- Go to <i>settings.py</i> and add the installed app
```
INSTALLED_APPS = [
    ...
    'book_api',
]
```

- Now we have to make the migrations and migrate
```
python manage.py makemigrations
python manage.py migrate

```

- Since the process we use to convert the data y the book_list functions is not optimized at all
we are going to use a technique known serialization and will actually use the DJango Rest Framework which we haven't used until now in this project
There is a build in serializer

To install rest framework add the following in your <i>settings.py</i>
```
INSTALLED_APPS = [
    ...
    'rest_framework",
]
```
- Create a serializer.py in book_api app folder and 
```

from rest_framework import serializers

class BookSerializer(serializers.Serializer):
	id = serializers.IntegerField()
	title = serializers.CharField()
	number_of_pages = serializers.IntegerField()
	publish_date = serializers.DateField()
	quantity = serializers.IntegerField()
```

- In views.py add:
```
from book_api.serializer import BookSerializer

def book_list(request):
	books = Book.objects.all()
	serializer = BookSerializer(books, many=True)
	return Response(serializer.data)
	
remove 
# from django.http import JsonResponse
Install Rest Framework
pip install djangorestframework
add
from rest_framework.response import Response
```

Note: <i>many=True</i> will return us a list of objects


- We need to add a decorator to specificly say if this is going to be a POST, GET, DELETE request
```
from rest_framework.decorators import api_view
@api_view('GET')
```

- Now we create a POST request that will give us the ability to build "books"
In this case we need to convert JSON to Complex data, in order words the the oposite operation to the one above

```
@api_view('POST')
def book_create(request):
	serializer = BookSerializer(data=request.data)
	#Check if the data is valid
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)
	else:
		return Response(serializer.errors)
```	

- In the urls.py
```
from book_api.views import ..., book_create


urlpatterns = [
    path('', book_create),
    ...
]

```

- Then we go back to serializer.py and create the Create Method inside tehe BookSerializar class
```
from book_api.models import Book

def create(self, data):
	return Book.objects.create(**data)
```

- We also need to add a read_only tag so the Rest Framework put the id for us
``
	id = serializers.IntegerField(read_only=True)
``

{
	"title": "Harry Potter",
	"number_of_pages": 300,
	"publish_date": "2021-01-10",
	"quantity": 400
}


- Create the next endpoint to a dynamic id. Meaning that with this view we can accesss/consult and update any id

in views.py
```
@api_view('GET', 'PUT', 'DELETE')
def book(request, pk):
	book = Book.objects.get(pk=pk)
	if request.method == 'GET':
		serializer = BookSerializer(book)
		return Response(seerializer.data)
```		

Note: pk = primary key which will be the id 

- Create dymic path
```
import book_api.views import ..., book
delete
from django.contrib import admin
path('<int:pk>', book)

<> those specify that there will be dinamic element

```

- The PUT request

```
if request.method == "PUT":
	serializer = BookSerializer(book, data=request.data)
	#validate the data
	if serializer.is_valid();
		serializer.save()
		return Response(serializer.data)
	return serializer.errors
```	
Note: We have to pass the instance <i>book</i> as we do have one now

- In serializer.py define an update function:
```
def update(self, instance, data):
	instance.title = data.get('title', instance.title)
	instance.number_of_pages = data.get('number_of_pages', instance.number_of_pages)
	instance.publish_date = data.get('publish_date', instance.publish_date)
	instance.quantity = data.get('quantity', instance.quantity)
	
	instance.save()
    return instance
```
and the DELETE 

```

    if request.method == "DELETE":
        book.delete()
        return Response({
            'delete': True
        })

```


JSON structure to make a new book 
{
    "title": "Silence of the wind",
    "number_of_pages": 180,
    "publish_date": "2019-08-05",
    "quantity": 100
}

- Statuses: All we have to do is import status method from the rest module into our views.py file

```
from rest_framework import status

```

Now we are update the reponsed returned on item deletion

```
return Response(status=status.HTTP_204_NO_CONTENT)

```

- We also want to be able to handle errors properly because now if we send bad data, we will get a warning that
the filed is wrong/missing but the actually HTTP Response is <b>200 OK</b> and we want get corret Response.
to achieve this we are going to add a second argument to the Response of the PUT method and the POST methods.
```
return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

If we can't fetch a specific book we get a general error, so we can use a try/expect: block
```
	try:
		book = Book.objects.get(pk=pk)
	except:
		return Response({
			'error' : 'Book does not exist'
		}, status=status.HTTP_404_NOT_FOUND)

```

- From this point out our application is fully funcioning and we are only going to improve, optimize the code and make it cleaner. 

INSPIRED BY: https://www.youtube.com/watch?v=mlr9BF4JomE