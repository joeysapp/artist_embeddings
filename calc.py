import numpy as np
import json, sys, urllib

with open('data/lastfm/json/joeysapp.embeds.json', 'r') as f:
	data = json.load(f)

#artist_nice = str(sys.argv[1])
#artist = urllib.quote_plus(str(sys.argv[1]))
#artist_embed = np.array(data[artist]['Embedding'])

print('1. Artist input')
selected_artist_1 = ""
selected_album_1 = ""
selected_song_1 = ""
selected_artist_2 = ""
selected_album_2 = ""
selected_song_2 = ""
user_input = 0
while user_input != 'q' and user_input != 'quit':
	user_input = input('> ')
	if (user_input == 1):
		artists = []
		i = 0
		for artist in data:
			if data[artist]['Embedding'] != None:
				artists.append(artist)
				print(str(i) + ' ' + artist)
				i += 1
		selected_artist_1 = artists[input('> # of artist: ')]
		if selected_artist_1 in data:
			print('[ '+selected_artist_1+' ]')
			print('1. Artist Embedding')
			print('2. Album -> Song embedding')
			user_input = input('> ')
			if user_input == 1:
				print("Setting embedding 1 to "+selected_artist_1)
				embedding_1 = data[selected_artist_1]['Embedding']
				user_input = 'q'
				continue
			elif user_input == 2:
				print('[ '+selected_artist_1+' ]')
				albums = []
				i = 0
				for album in data[selected_artist_1]['Albums']:
					if data[selected_artist_1]['Albums'][album]['Embedding'] != None:
						albums.append(album)
						print(str(i) + ' ' + album)
						i += 1
				selected_album_1 = albums[input('> # of album: ')]
				print('1. Album embedding')
				print('2. Song embedding')
				user_input = input('> ')
				if user_input == 1:
					print("Setting embedding 1 to "+selected_album_1)
					embedding_1 = data[selected_artist_1]['Albums'][selected_album_1]['Embedding']
					user_input = 'q'
					continue
				elif user_input == 2:
					print('[ '+selected_artist_1 +' - ' + selected_album_1+' ]')
					songs = []
					i = 0
					for song in data[selected_artist_1]['Albums'][selected_album_1]['Songs']:
						if data[selected_artist_1]['Albums'][selected_album_1]['Songs'][song]['Embedding'] != None:
							songs.append(song)
							print(str(i) + ' ' + selected_album_1 + ' - ' +song)
							i += 1
						else:
							continue

					selected_song_1 = songs[input('> # of song: ')]
					embedding_1 = data[selected_artist_1]['Albums'][selected_album_1]['Songs'][selected_song_1]['Embedding']
					user_input = 'q'
					continue

user_input = 0
embedding_1 = np.array(embedding_1)
print('1. Find most similar and disimilar items')
print('2. Compare items')
user_input = input('> ')
if user_input == 1:
	maximum = -9999999
	max_name = ""
	minimum = 9999999
	min_name = ""
	if selected_song_1 != "":
		for artist in data:
			for album in data[artist]['Albums']:
				for song in data[artist]['Albums'][album]['Songs']:
					if data[artist]['Albums'][album]['Songs'][song]['Embedding'] != None:
						embedding_2 = np.array(data[artist]['Albums'][album]['Songs'][song]['Embedding'])
						if song == selected_song_1:
							continue
						dist = np.linalg.norm(embedding_1-embedding_2);
						if dist > maximum:
							maximum = dist
							max_name = str(artist)+" - "+str(album)+" - "+str(song)
							print('far: ', dist, max_name)
						if dist < minimum:
							minimum = dist
							min_name = str(artist)+" - "+str(album)+" - "+str(song)
							print('near: ', dist, min_name)
		print("The least similar to ["+
				urllib.unquote_plus(selected_artist_1)+" - "+
				urllib.unquote_plus(selected_album_1)+" - "+
				urllib.unquote_plus(selected_song_1)+"] is"),
		print('['+urllib.unquote_plus(max_name)+']')
		print("The most similar to ["+
				urllib.unquote_plus(selected_artist_1)+" - "+
				urllib.unquote_plus(selected_album_1)+" - "+
				urllib.unquote_plus(selected_song_1)+"] is"),
		print('['+urllib.unquote_plus(min_name)+']')
	elif selected_album_1 != "":
		for artist in data:
			for album in data[artist]['Albums']:
				if data[artist]['Albums'][album]['Embedding'] != None:
					embedding_2 = np.array(data[artist]['Albums'][album]['Embedding'])
					if album == selected_album_1:
						continue
					dist = np.linalg.norm(embedding_1-embedding_2);
					if dist > maximum:
						maximum = dist
						max_name = str(artist)+" - "+str(album)
						print('far: ', dist, max_name)
					if dist < minimum:
						minimum = dist
						min_name = str(artist)+" - "+str(album)
						print('near: ', dist, min_name)
		print("The least similar to ["+
				urllib.unquote_plus(selected_artist_1)+" - "+
				urllib.unquote_plus(selected_album_1)+"] is"),
		print('['+urllib.unquote_plus(max_name)+']')
		print("The most similar to ["+
				urllib.unquote_plus(selected_artist_1)+" - "+
				urllib.unquote_plus(selected_album_1)+"] is"),
		print('['+urllib.unquote_plus(min_name)+']')
	else:
		for artist in data:
			if data[artist]['Embedding'] != None:
				embedding_2 = np.array(data[artist]['Embedding'])
				if artist == selected_artist_1:
					continue
				dist = np.linalg.norm(embedding_1-embedding_2);
				if dist > maximum:
					maximum = dist
					max_name = str(artist)
					print('far: ', dist, max_name)
				if dist < minimum:
					minimum = dist
					min_name = str(artist)
					print('near: ', dist, min_name)
		print("The least similar to ["+
				urllib.unquote_plus(selected_artist_1)+"] is"),
		print('['+urllib.unquote_plus(max_name)+']')
		print("The most similar to ["+
				urllib.unquote_plus(selected_artist_1)+"] is"),
		print('['+urllib.unquote_plus(min_name)+']')
elif user_input == 2:
	while user_input != 'q' and user_input != 'quit':
		user_input = input('> ')
		if (user_input == 1):
			artists = []
			i = 0
			for artist in data:
				artists.append(artist)
				print(str(i) + ' ' + artist)
				i += 1
			selected_artist_2 = artists[input('> # of artist: ')]
			if selected_artist_2 in data:
				print('[ '+selected_artist_2+' ]')
				print('1. Artist Embedding')
				print('2. Album -> Song embedding')
				user_input = input('> ')
				if user_input == 1:
					print("Setting embedding 1 to "+selected_artist_2)
					embedding_2 = data[selected_artist_2]['Embedding']
					user_input = 'q'
					continue
				elif user_input == 2:
					print('[ '+selected_artist_2+' ]')
					albums = []
					i = 0
					for album in data[selected_artist_2]['Albums']:
						albums.append(album)
						print(str(i) + ' ' + album)
						i += 1
					selected_album_2 = albums[input('> # of album: ')]
					print('1. Album embedding')
					print('2. Song embedding')
					user_input = input('> ')
					if user_input == 1:
						print("Setting embedding 1 to "+selected_album_2)
						embedding_2 = data[selected_artist_2]['Albums'][selected_album_2]['Embedding']
						user_input = 'q'
						continue
					elif user_input == 2:
						print('[ '+selected_artist_2 +' - ' + selected_album_2+' ]')
						songs = []
						i = 0
						for song in data[selected_artist_2]['Albums'][selected_album_2]['Songs']:
							if 'Embedding' in data[selected_artist_2]['Albums'][selected_album_2]['Songs'][song]:
								songs.append(song)
								print(str(i) + ' ' + selected_album_2 + ' - ' +song)
								i += 1
						selected_song_2 = songs[input('> # of song: ')]
						embedding_2 = data[selected_artist_2]['Albums'][selected_album_2]['Songs'][selected_song_2]['Embedding']
						user_input = 'q'
						continue

print('Artist 1 : '+selected_artist_1)
if selected_album_1 != "":
	print('Album 1 : '+selected_album_1)
if selected_song_1 != "":
	print('Song 1 : '+selected_song_1)

print('Artist 2 : '+selected_artist_2)
if selected_album_2 != "":
	print('Album 2 : '+selected_album_2)
if selected_song_2 != "":
	print('Song 2 : '+selected_song_2)


#for album in data[artist]['Albums']:
#	print(album)


# closest = 9999999
# farthest = -99999999

# for artist in data:
# 	compare_embed = np.array(data[artist]['Embedding'])
# 	if np.count_nonzero(compare_embed) == 0:
# 		continue
# 	dist = np.linalg.norm(artist_embed-compare_embed)
# 	if (dist > farthest and artist != "Kanye+West" and artist != "Jon+Hopkins"):
# 		farthest = dist
# 		farthest_artist = artist
# 	if (dist < closest and dist > 0):
# 		print(artist)
# 		closest = dist
# 		closest_artist = artist

# print("The closest artist to "+artist_nice+" is "+str(closest_artist))
# print("The farthest artist to "+artist_nice+" is "+str(farthest_artist))


# a = np.array(kanye['Embedding'])
# b = np.array(chance['Embedding'])

# dist = np.linalg.norm(a-b)

# print(dist)