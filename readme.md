# Flask MongoDB CRUD APP

## Project Setup

1. Create main (`flaskMongoDB`) project folder

2. create virtual environment inside of it(main project folder)


```
### Linux and Mac
python -m venv venv

```

### windows users
```
python -m venv venv
```

3. Activate the virtual environment

```bash
# Linux and Mac
source venv/bin/activate
#Windows users
venv\Scripts\activate
```

4. Install all project dependencies

```bash
pip install flask Flask-PyMongo Flask-WTF
python -m pip install "pymongo[srv]
```

5. Setup the mongoDB cluster

## Project Structure

```
project_root_dir
│
|
|
|__ application
|    |
|    |__ templates
|    |__ __init__.py
|    |__ routes.py
|    |__ forms.py
|
|
|__ venv
|
|
|
|__ README.md
|
|
|__ run.py
```

# HOW DID I CREATE THIS APP

1. Simple Hello world app
2. Setup database connection [Sign Up For mongoDB cloud](https://account.mongodb.com/account/login)
3. Setup **init**.py file (project configurattions)
4. Setup base template
5. Setup view_todos.html file
6. Create Flask forms
7. Create insert
8. Implement Sweet alerts
9. Create retrieve
10. Implemet delete
11. Implement update functionality
12. Setup .gitignore file
