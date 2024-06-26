from playwright.sync_api import Page, expect

# Tests for your routes go here

def test_get_albums(page, db_connection, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    expect(page.locator('article').first).to_contain_text("Title: Doolittle")
    expect(page.locator('article').last).to_contain_text("Released: 1973")

def test_get_albums_links_to_albums_id(page, db_connection, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.get_by_text("Doolittle").click()
    expect(page.locator('h3')).to_contain_text("Doolittle")
    expect(page.locator('p').first).to_contain_text("1989")
    expect(page.locator('p').last).to_contain_text("Pixies")

def test_get_artists(page, db_connection, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    expect(page.locator('article').first).to_contain_text("Name: Pixies")
    expect(page.locator('article').last).to_contain_text("Genre: Jazz")

def test_get_artists_links_to_artists_id(page, db_connection, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.get_by_text("Pixies").click()
    expect(page.locator('h3')).to_contain_text("Pixies")
    expect(page.locator('p')).to_contain_text("Rock")

def test_create_book(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.get_by_text("Add new album").click()

    page.fill("input[name='title']", "Midnights")
    page.fill("input[name='release_year']", "2022")
    page.fill("input[name='artist_id']", "3")

    page.click("text=Create new album")

    expect(page.locator("h3")).to_contain_text("Midnights")
    expect(page.locator('p').first).to_contain_text("2022")
    expect(page.locator('p').last).to_contain_text("Taylor Swift")

def test_validate_book(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums/new")
    page.click("text=Create new album")
    expect(page.get_by_test_id("errors")).to_contain_text("can't be blank")

# def test_post_albums_success(db_connection, web_client):
#     db_connection.seed("seeds/music_library.sql")
#     post_response = web_client.post("/albums", data={
#         "title": "Midnights",
#         "release_year": "2022",
#         "artist_id": "3"
#     })
#     assert post_response.status_code == 200
#     assert post_response.data.decode("utf-8") == "Album added successfully"

#     get_response = web_client.get("/albums")
#     last_album = get_response.data.decode("utf-8").split("\n")[-1]
#     assert last_album == "Album(13, Midnights, 2022, 3)"

# def test_post_albums_with_invalid_params(db_connection, web_client):
#     db_connection.seed("seeds/music_library.sql")
#     post_response = web_client.post("/albums")
#     assert post_response.status_code == 400

#     get_response = web_client.get("/albums")
#     last_album = get_response.data.decode("utf-8").split("\n")[-1]
#     assert last_album == "Album(12, Ring Ring, 1973, 2)"

# def test_get_artists(db_connection, web_client):
#     db_connection.seed("seeds/music_library.sql")
#     response = web_client.get("/artists")
#     assert response.status_code == 200
#     assert response.data.decode("utf-8") == "\n".join([
#         "Artist(1, Pixies, Rock)",
#         "Artist(2, ABBA, Pop)",
#         "Artist(3, Taylor Swift, Pop)",
#         "Artist(4, Nina Simone, Jazz)"
#     ])

# def test_post_artists_success(db_connection, web_client):
#     db_connection.seed("seeds/music_library.sql")
#     post_response = web_client.post("/artists", data={
#         "name": "Outkast",
#         "genre": "Hip hop",
#     })
#     assert post_response.status_code == 200
#     assert post_response.data.decode("utf-8") == "Artist added successfully"

#     get_response = web_client.get("/artists")
#     last_album = get_response.data.decode("utf-8").split("\n")[-1]
#     assert last_album == "Artist(5, Outkast, Hip hop)"

# def test_post_artists_with_invalid_params(db_connection, web_client):
#     db_connection.seed("seeds/music_library.sql")
#     post_response = web_client.post("/artists")
#     assert post_response.status_code == 400

#     get_response = web_client.get("/artists")
#     last_album = get_response.data.decode("utf-8").split("\n")[-1]
#     assert last_album == "Artist(4, Nina Simone, Jazz)"
