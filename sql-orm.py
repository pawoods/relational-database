from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" db
db = create_engine("postgresql:///chinook")
base = declarative_base()


# creates a class-based model for the "Artist" table
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


# creates a class-based model for the "Album" table
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


# creates a class-based model for the "Track" table
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the db using declarative_base subclass
base.metadata.create_all(db)


# query 1 - select all records from "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep=" | ")

# query 2 - select only the "Name" records from "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.Name)

# query 3 - select only "Queen" from "Artist" table
# artist = session.query(Artist).filter_by(Name="Queen").first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# query 4 - select only "ArtistId" #84 from "Artist" table
# artist = session.query(Artist).filter_by(ArtistId=84).first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# query 5 - select only albums from "Album" table with "ArtistId" #84
# albums = session.query(Album).filter_by(ArtistId=84)
# for album in albums:
#     print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")

# query 6 - select only tracks from "Tracks" table with composer "Foo Fighters"
tracks = session.query(Track).filter_by(Composer="Foo Fighters")
for track in tracks:
    print(track.TrackId, track.Name, track.AlbumId, track.Composer, sep=" | ")
