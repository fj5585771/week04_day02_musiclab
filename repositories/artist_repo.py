from db.run_sql import run_sql
import repositories.artists_repository as artists_repository
from models.artists import Artists

# CREATE 
def save(artist):
    sql = "INSERT INTO artists (first_name, last_name) VALUES (%s, %s) RETURNING id"
    values = [artist.first_name, artist.last_name]
    results = run_sql(sql, values)
    id = results[0]["id"]
 # RESULTS WILL BE A LIST OF DICTIONARIES, WHERE EACH ITEM IN THE LIST CONTAINS INFO
    artist.id = id 
    return artist

# READ - select all
def select_all(artists):  
    artists = [] 

    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        artist = Artist(row['First_name'], row['last_name'], row['id'] )
        artists.append(artist)
    return artists
    
# READ 
def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"  
    values = [id] 
    result = run_sql(sql, values)[0]
    
    if result is not None:
        artist = Artist(result['first_name'], result['last_name'], result['id'] )
    return artist

# DELETE - all
def delete_all():
    sql = "DELETE FROM artists" 
    run_sql(sql)

# DELETE
def delete(id):
    sql = "DELETE FROM artists WHERE id = %s" 
    values = [id]
    run_sql(sql, values)

# UPDATE 
def update(artist):
    sql = "UPDATE artists SET (first_name, last_name) = (%s, %s) WHERE id = %s"
    values = [artist.first_name, artist.last_name, artist.id]
    run_sql(sql, values) 
    
def get_albums(artist):
    sql = "SELECT * FROM albums WHERE artists_id = %s"
    values = [artist.id]
    results = run_sql(sql, values)
    artists_albums = []

    for row_data in results:
        album = Album(
            row_data["title"], 
            artist, 
            row_data["year"],
            row_data["duration"]
            row_data["genre"],
            row_data["id"]
        )
        artists_albums.append(album)

    return artists_albums