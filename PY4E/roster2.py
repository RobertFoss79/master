import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'

# Read and parse the JSON file
str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:
    name = entry[0]
    title = entry[1]
    role = entry[2]

    print((name, title, role))

    # Insert or ignore new users
    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', (name,))
    cur.execute('SELECT id FROM User WHERE name = ? ', (name,))
    user_id = cur.fetchone()[0]

    # Insert or ignore new courses
    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', (title,))
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title,))
    course_id = cur.fetchone()[0]

    # Insert or replace member information including the role
    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
        (user_id, course_id, role))

    conn.commit()

# Run the provided SQL commands to verify the output
print("Running SQL queries...")

# Query to match the required output format
cur.execute('''
    SELECT User.name, Course.title, Member.role
    FROM User
    JOIN Member ON User.id = Member.user_id
    JOIN Course ON Member.course_id = Course.id
    ORDER BY User.name DESC, Course.title DESC, Member.role DESC
    LIMIT 2
''')
rows = cur.fetchall()
for row in rows:
    print('|'.join(map(str, row)))

# Query for checksum validation
cur.execute('''
    SELECT 'XYZZY' || hex(User.name || Course.title || Member.role) AS X
    FROM User
    JOIN Member ON User.id = Member.user_id
    JOIN Course ON Member.course_id = Course.id
    ORDER BY X
    LIMIT 1
''')
row = cur.fetchone()
print(row[0] if row else 'No result found')

cur.close()