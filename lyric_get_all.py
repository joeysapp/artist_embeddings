import json, sys, os, time, random, urllib
from PyLyrics import *

# Usage:
# > python lyric_get_all.py joeysapp n_plays

user = str(sys.argv[1])

with open('data/lastfm/json/'+user+'.json', 'r') as f:
	user_data = json.load(f)

for artist in user_data:
	fname = 'data/lyrics/'+artist+'.json'
	if os.path.isfile(fname):
		print("D %-*s" % (20, artist))
		continue
	else:
		entry = {}
		fails = 0
		if user_data[artist]["Plays"] < int(sys.argv[2]) or artist == 'C418':
			print("- %-*s" % (20, artist))
			continue
		for album in user_data[artist]['Albums']:
			if (fails > 10):
				print("Failed too much!")
				break
			for song in user_data[artist]['Albums'][album]['Songs']:
				try:
					#time.sleep(random.random()*1)
					entry[song] = PyLyrics.getLyrics(artist.replace('+', ' '), song.replace('+', ' '))
					print("O %-*s %s" % (20, artist, song))
					fails = 0
				except ValueError:
					entry[song] = None
					print("X %-*s %s" % (20, artist, song))
					fails += 1
		with open(fname, 'w') as f:
			json.dump(entry, f)
