import numpy as np
import codecs, json, os

user = 'joeysapp'

# with open('data/lastfm/json/'+user+'.test.json', 'r') as f:
# 	data = json.load(f)
# 	for filename in os.listdir('data/embeddings/'):
# 		artist = filename[:-5]
# 		if 'json' not in filename:
# 			continue
# 		obj_text = codecs.open('data/embeddings/'+filename, 'r', encoding='utf-8').read()
# 		obj_json = json.loads(obj_text)
# 		for song in obj_json:
# 			for album in data[artist]['Albums']:
# 				# This is super gross but my data design wasn't 100%
# 				if song in data[artist]['Albums'][album]['Songs']:
# 					data[artist]['Albums'][album]['Songs'][song]['Embedding'] = obj_json[song]

# with open('data/lastfm/json/'+user+'.test.json', 'w') as f:
# 	json.dump(data, f, indent=2)


obj_text = codecs.open('data/lastfm/json/'+user+'.test.json', 'r', encoding='utf-8').read()
data = json.loads(obj_text)
for artist in data:
	artist_embedding = np.zeros(50)
	for album in data[artist]['Albums']:
		album_embedding = np.zeros(50);
		for song in data[artist]['Albums'][album]['Songs']:
			embedding = data[artist]['Albums'][album]['Songs'][song]['Embedding']
			if np.count_nonzero(embedding) > 0:
				album_embedding += np.array(embedding)
		if np.count_nonzero(album_embedding) > 0:
			data[artist]['Albums'][album]['Embedding'] = album_embedding.tolist()
		if np.count_nonzero(album_embedding) > 0:
			artist_embedding += album_embedding
	if np.count_nonzero(artist_embedding) > 0:
		data[artist]['Embedding'] = artist_embedding.tolist()

with open('data/lastfm/json/'+user+'.test_2.json', 'w') as f:
	json.dump(data, f, indent=2)
