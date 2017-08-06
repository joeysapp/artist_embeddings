import json, sys, os, time, random, urllib
from PyLyrics import *

# Usage:
# > python lyric_individual.py joeysapp "Kanye West"

user = str(sys.argv[1])
artist = urllib.quote_plus(str(sys.argv[2]))
fname = 'data/lyrics/'+artist+'.json'

if not os.path.isfile(fname):
	entry = { artist:artist }
	with open(fname, 'w') as f:
		json.dump(entry, f)
else:

	with open('data/lastfm/json/'+user+'.json', 'r') as f:
		user_data = json.load(f)
	entry = {}
	fails = 0
	with open(fname) as f:
		data = json.load(f)
	if artist not in user_data or artist not in data:
		print("Couldn't find that artist: "+artist)
		sys.exit()
	for album in user_data[artist]['Albums']:
		if (fails > 10):
			break
		for song in user_data[artist]['Albums'][album]['Songs']:
			if song in data or song in entry:
				continue
			try:
				#time.sleep(random.random()*1)
				entry[song] = PyLyrics.getLyrics(artist.replace('+', ' '), song.replace('+', ' '))
				print("O %-*s %s" % (20, artist, song))
				fails = 0
			except ValueError:
				entry[song] = None
				print("X %-*s %s" % (20, artist, song))
				fails += 1
	data.update(entry)
	with open(fname, 'w') as f:
		json.dump(data, f)
