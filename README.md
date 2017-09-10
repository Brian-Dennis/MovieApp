# WebFlix

This project was created for the Udacity Full Stack Web Developer Nanodegree.
It is a movie_trailer site made with python and flask.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
You need Git, Python 3.6, flask, sqlite, sqlalchemy, virtualenv, pip.
```

### Installing

A step by step series of instructions that tell you how to get a development env running

first go to the directory storing the source code. Inside your terminal, in the directory that the source code is in you should run:

```
mkdir venv
virtualenv venv/
source venv/bin/acitvate (linux/unix)
source venv/scripts/activate (windows)
```

After that you should have an active virtualenv and see a (venv) next to the prompt in the terminal. Then you will want to use pip to install your dependecies.

```
pip install flask
pip install sqlalchemy
```

Example of terminal after running virtualenv venv
```
$ virtualenv venv/
Using base prefix 'd:\\program files'
New python executable in D:\Projects\Python_Projects\udacity-projects\movie-trailer-project\favorite_movies\assets\venv\Scripts\python.exe
Installing setuptools, pip, wheel...done.
```
Example of terminal after running source venv/scripts/activate
```
brian@Brians-Desktop MINGW64 /d/Projects/Python_Projects/udacity-projects/movie-trailer-project/favorite_movies/assets
$ source venv/scripts/activate
(venv)
brian@Brians-Desktop MINGW64 /d/Projects/Python_Projects/udacity-projects/movie-trailer-project/favorite_movies/assets
$
```
Running pip install flask:
```
$ pip install flask
Collecting flask
  Using cached Flask-0.12.2-py2.py3-none-any.whl
Collecting Werkzeug>=0.7 (from flask)
  Using cached Werkzeug-0.12.2-py2.py3-none-any.whl
Collecting Jinja2>=2.4 (from flask)
  Using cached Jinja2-2.9.6-py2.py3-none-any.whl
Collecting click>=2.0 (from flask)
  Using cached click-6.7-py2.py3-none-any.whl
Collecting itsdangerous>=0.21 (from flask)
Collecting MarkupSafe>=0.23 (from Jinja2>=2.4->flask)
Installing collected packages: Werkzeug, MarkupSafe, Jinja2, click, itsdangerous, flask
Successfully installed Jinja2-2.9.6 MarkupSafe-1.0 Werkzeug-0.12.2 click-6.7 flask-0.12.2 itsdangerous-0.24
```
Running pip install sqlalchemy:
```
$ pip install sqlalchemy
Collecting sqlalchemy
Installing collected packages: sqlalchemy
Successfully installed sqlalchemy-1.1.13
```
Running the application:
```
$ python app.py
```
## Built With

* [Python](https://www.python.org/doc/) - The code used
* [Flask](http://flask.pocoo.org/docs/0.12/) - The Framework used
* [Sqlalchemy](http://docs.sqlalchemy.org/en/latest/) - ORM used

## Contributing

Please read [credits.html](http://localhost:5000/credits) for credit to the resources I used to finish this project and that helped me through some of the points I got stuck at.

## Authors

* **Brian Dennis** - *Initial work* - [Brian-Dennis](https://github.com/Brian-Dennis)

## License

This project is licensed under the MIT License

## Acknowledgments

* Hat tip to Udacity and anyone else's code that was used
* Inspiration
* etc
