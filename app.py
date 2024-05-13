import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/albums', methods=['POST'])
def post_albums():
    db_connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(db_connection)
    album = Album(
        None,
        request.form["title"],
        request.form["release_year"],
        request.form["artist_id"]
    )
    album_repository.create(album)
    return "Album added successfully"

@app.route('/albums', methods=['GET'])
def get_albums():
    db_connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(db_connection)
    albums = album_repository.all()
    return "\n".join([
        str(album) for album in albums
    ])

@app.route("/artists", methods=['GET'])
def get_artists():
    db_connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(db_connection)
    artists = artist_repository.all()
    return "\n".join([
        str(artist) for artist in artists
    ])

@app.route("/artists", methods=['POST'])
def post_artists():
    db_connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(db_connection)
    artist = Artist(
        None,
        request.form["name"],
        request.form["genre"],
    )
    artist_repository.create(artist)
    return "Artist added successfully"

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
