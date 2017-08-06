import json, csv, re, sys

user = str(sys.argv[1])
obj = { }

artist_count = 0
album_count = 0
track_count = 0
listen_count = 0

with open('data/lastfm/csv/'+user+'.csv') as f:
	for row in csv.reader(f):

		artist = re.sub('([^\s\w]|_)+', '', row[0])
		album = re.sub('([^\s\w]|_)+', '', row[1])
		track = re.sub('([^\s\w]|_)+', '', row[2])
		
		if artist == "":
			continue
		if artist not in obj:
			obj[artist] = { "Albums": {}, "Embedding": None, "Plays":0 }
			artist_count += 1
		if album not in obj[artist]["Albums"]:
			obj[artist]["Albums"][album] = { "Songs": {}, "Embedding": None, "Plays": 0 }
			album_count += 1
		if track not in obj[artist]["Albums"][album]["Songs"]:
			obj[artist]["Albums"][album]["Songs"][track] = { "Lyrics": None, "Embedding": None, "Plays":1 }
			obj[artist]["Albums"][album]["Plays"] += 1
			obj[artist]["Plays"] += 1
			track_count += 1
			listen_count += 1
		else:
			obj[artist]["Albums"][album]["Songs"][track]["Plays"] += 1
			obj[artist]["Albums"][album]["Plays"] += 1
			obj[artist]["Plays"] += 1
			listen_count += 1


with open('data/lastfm/json/'+user+'.min.json', 'w') as f:
	json.dump(obj, f)

with open('data/lastfm/json/'+user+'.json', 'w') as f:
	json.dump(obj, f, indent=4)

print("> User: "+user+"\n\tArtists: "+str(artist_count)+"\n\tAlbums: "+str(album_count)+"\n\tPlays: "+str(listen_count))
