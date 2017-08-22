from flask import Flask, render_template, request, redirect, url_for
# Importing sqlalchemy for database sqlite
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, MovieItem, engine

app = Flask(__name__)

# Database name
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Routes in Templates directory
@app.route('/')
def index():
    items = session.query(MovieItem)
    return render_template('index.html', items=items)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/credits')
def credits():
    return render_template('credits.html')


@app.route('/add-movie', methods=['GET', 'POST'])
def add_movie():
    # if statement checking form status
    if request.method == 'POST':
        newMovie = MovieItem(
            title=request.form['movie_title'],
            synopsis=request.form['movie_storyline'],
            poster_image_url=request.form['poster_image'],
            youtube_trailer_url=request.form['trailer_youtube'])
        session.add(newMovie)
        session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('add-movie.html')


if __name__ == '__main__':
    app.run(debug=True)
