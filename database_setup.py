import os
import re
import sys
import webbrowser
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


# MovieItem class for DB
class MovieItem(Base):
    __tablename__ = 'movie_item'
    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=False)
    synopsis = Column(String(250))
    poster_image_url = Column(String(250))
    youtube_trailer_url = Column(String(250))

engine = create_engine('sqlite:///favoriteMovies.db')
Base.metadata.create_all(engine)
