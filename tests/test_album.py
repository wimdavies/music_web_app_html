from lib.album import Album

def test_album_constructs():
    album = Album(1, "Test Title", 1999, 2)
    album.id == 1
    album.title == "Test Title"
    album.release_year == 1999
    album.artist_id == 2

def test_album_validates():
    assert Album(1, None, 1999, 2).is_valid() == False
    assert Album(1, "", 1999, 2).is_valid() == False
    assert Album(1, "Test Title", None, 2).is_valid() == False
    assert Album(1, "Test Title", "", 2).is_valid() == False
    assert Album(1, "Test Title", 1999, None).is_valid() == False
    assert Album(1, "Test Title", 1999, "").is_valid() == False
    assert Album(1, "Test Title", 1999, 2).is_valid() == True

def test_album_generates_errors():
    assert Album(1, None, 1999, 2).generate_errors() == ["Title can't be blank"]
    assert Album(1, "Test Title", None, 2).generate_errors() == ["Release year can't be blank"]
    assert Album(1, "Test Title", 1999, None).generate_errors() == ["Artist ID can't be blank"]
    assert Album(1, None, None, None).generate_errors() == ["Title can't be blank", "Release year can't be blank", "Artist ID can't be blank"]
    assert Album(1, "Test Title", 1999, 2).generate_errors() == None
