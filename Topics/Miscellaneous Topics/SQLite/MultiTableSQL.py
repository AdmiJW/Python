import sqlite3
import lxml.etree as ET
from typing import Dict

SIGNIFICANT_INFO = ['Name', 'Artist', 'Album', 'Genre', 'Total Time', 'Track Count', 'Rating']

#   Will check for the tags that will contain significant info. It it was found, then in the next iteration
#   (which will be the value of the info) will get added into the dictionary
def extractInfo(track: ET._Element) -> Dict:
    result = dict()
    attrib = None
    for child in track:
        if child.text in SIGNIFICANT_INFO:
            attrib = child.text
        elif attrib is not None:
            result[attrib] = child.text
            attrib = None

    print(result)
    return result

# REMEMBER ALWAYS GET ARTIST ID FIRST!!!
def getIdOrCreate(key: str, type: str, artistId: int = None ) -> int:
    #   Try to check if it already exists in the respective table
    cursor.execute('SELECT id FROM {} WHERE {} = ?'.format(type, 'title' if type=='Album' else 'name'), (key,) )
    result = cursor.fetchone()

    if result is None:
        #   Album is special as it has an additional artist_id field and title field
        if type == 'Album' and artistId is not None:
            cursor.execute('INSERT INTO Album (artist_id, title) VALUES (?, ?)', ( artistId, key) )
        else:
            cursor.execute('INSERT INTO {} (name) VALUES (?)'.format(type), (key,) )
        #   Now that we have inserted the new value, use recursion to return the ID
        return getIdOrCreate(key, type)
    else:
        #   The value is present. Just return the ID of the item retrieved
        return result[0]



connect = sqlite3.connect('Resources/tracks.sqlite')
cursor = connect.cursor()

cursor.execute('DROP TABLE IF EXISTS Artist')
cursor.execute('DROP TABLE IF EXISTS Album')
cursor.execute('DROP TABLE IF EXISTS Track')
cursor.execute('DROP TABLE IF EXISTS Genre')

#   Using SQLite we really can't execute multiple statements in one go
cursor.execute('''
    CREATE TABLE Track (
        'id' INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        'title' TEXT UNIQUE,
        'album_id' INTEGER,
        'genre_id' INTEGER,
        'len' INTEGER,
        'rating' INTEGER,
        'count' INTEGER
    );
''')
cursor.execute('''
    CREATE TABLE Album (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id INTEGER,
        title TEXT UNIQUE
    );
''')
cursor.execute('''
    CREATE TABLE Genre (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );
''')
cursor.execute('''
    CREATE TABLE Artist (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );
''')

connect.commit()

file = open('Resources/Library.xml', 'r')
xmlFile = ET.parse( file )
trackDir = xmlFile.xpath('./dict/dict')
tracks = trackDir[0].xpath('./dict')


for track in tracks:
    infoList = extractInfo(track)
    #   Invalid track: No Title, Artist or Album
    if ( not "Name" in infoList or not "Artist" in infoList or not "Album" in infoList): continue

    title = infoList["Name"]
    len = infoList["Total Time"] if "Total Time" in infoList else None
    rating = infoList["Rating"] if "Rating" in infoList else None
    count = infoList["Track Count"] if 'Track Count' in infoList else None

    artistID = getIdOrCreate( infoList['Artist'], 'Artist')
    albumID = getIdOrCreate( infoList['Album'], 'Album', artistId=artistID )
    genreID = getIdOrCreate( infoList['Genre'], 'Genre' ) if "Genre" in infoList else None

    cursor.execute('INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count) VALUES (?,?,?,?,?,?)',
                   (title, albumID, genreID, len, rating, count) )
connect.commit()