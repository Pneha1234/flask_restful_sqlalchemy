# flask_restful_sqlalchemy

A sample project blog project for implemeting flask Restful and sqlalchemy using sqlite as database server

### Prerequisites

Create a virtual environment(venv) in your project directory using the command
```python
virtualenv venv
```

if virtual environment is not installed in your system, install virtual env using the command
```python
pip3 install virtualenv
```
and then create a virtual env for your project

activate the virtual environment, using command
```python
source venv/bin/activate
```

### Installing

Install all the requirements mentioned in requirments.txt file using command
```python
pip install -r requirments.txt
``` 
incase you are using python3 use the command:
```python
pip3 install -r requirements.txt
```

## Getting Started
open terminal and move to your project directory, use the following command to create models in your database
```python
from app import db
db.create_all()
exit()
```
check if the models are created or not using the following command
```python
sqlite3 database_name
.tables
```
example
```python
neha@neha-Latitude-3400:~/Documents/moru_flask_restful_sqlalchemy$ sqlite3 blog.db
SQLite version 3.31.1 2020-01-27 19:55:54
Enter ".help" for usage hints.
sqlite> .tables
blog_model
```
to run the project, use command
```python
python file_name
```
example
```python
(venv) neha@neha-Latitude-3400:~/Documents/moru_flask_restful_sqlalchemy$ python app.py
```

### endpoints:
to create a blog
```python
url: {{url}}/blogs
body:
{
	"text":"sample blog",
	"views":20,
	"likes":30
}
Method: POST
```

to get all blogs
```python
url: {{url}}/blogs
Method: GET
```

to get an individual blog
```python
url: {{url}}/blogs/{{blog_id}}
Method: GET
```
to update a blog
```python
url: {{url}}/blogs/{{blog_id}}
body:
{
	"text":"sample blog",
	"views":20,
	"likes":30
}
Method: PUT
```
to delete a blog
```python
url: {{url}}/blogs/{{blog_id}}
Method: DELETE
```
