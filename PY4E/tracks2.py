import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Create new tables with the updated schema
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Genre (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
);

CREATE TABLE Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

# Open the CSV file
handle = open('tracks.csv')

# Read and process each line from the CSV file
for line in handle:
    line = line.strip()
    pieces = line.split(',')
    if len(pieces) < 7: continue  # Assuming the genre is the 7th element

    name = pieces[0]
    artist = pieces[1]
    album = pieces[2]
    genre = pieces[3]
    count = pieces[4]
    rating = pieces[5]
    length = pieces[6]

    print(name, artist, album, genre, count, rating, length)

    # Insert or ignore artist
    cur.execute('''INSERT OR IGNORE INTO Artist (name) VALUES ( ? )''', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist,))
    artist_id = cur.fetchone()[0]

    # Insert or ignore genre
    cur.execute('''INSERT OR IGNORE INTO Genre (name) VALUES ( ? )''', (genre,))
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre,))
    genre_id = cur.fetchone()[0]

    # Insert or ignore album
    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) VALUES ( ?, ? )''', (album, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album,))
    album_id = cur.fetchone()[0]

    # Insert or replace track
    cur.execute('''INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count) 
                   VALUES ( ?, ?, ?, ?, ?, ? )''', (name, album_id, genre_id, length, rating, count))

    conn.commit()

handle.close()