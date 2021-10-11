"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
7 October 2021
"""
#Of course I take every opportunity to rep my man Alec
#I made everything with proper capitalisation already out of respect for my man Alec.

def make_album(artist, title, tracks=0):
    album_dictionary = {
        'Artist': artist.title(),
        'Title': title.title(),
        }
    if tracks:
        album_dictionary['Tracks'] = tracks
    return album_dictionary

album = make_album('Alec Benjamin', "Together We'll Fall")
print(album)

album = make_album('Alec Benjamin', 'Older', tracks=4)
print(album)

album = make_album('Alec Benjamin', 'Medicine Man', tracks=0)
print(album)

album = make_album('Alec Benjamin', 'Anesthesia', tracks=2)
print(album)

"""
def make_album(artist, title):
    album_dictionary = {
        'Artist': artist.title(),
        'Title': title.title(),
        }
    return album_dictionary

album = make_album('Alec Benjamin', "Together We'll Fall") #dunno why the first L in ' we'll ' ends up capitalised.... very odd. When I delete the first L, it happens to the second L.
print(album)

album = make_album('Alec Benjamin', 'Older')
print(album)

album = make_album('Alec Benjamin', 'Medicine Man')
print(album)
"""
