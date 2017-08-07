import numpy as np
import json, re, os, codecs

artist = "Pinegrove"

## Get in GloVe values
num_words = 400000

glove_index_dict = {}
glove_embedding_weights = np.empty((num_words, 50))

with open('data/glove.6B/glove.6B.50d.txt', 'r') as f:
	i = 0
	for line in f:
		if (num_words == i):
			break
		line = line.strip().split()
		word = line[0]
		glove_index_dict[word] = i
		glove_embedding_weights[i,:] = map(float, line[1:])
		i += 1


for filename in os.listdir('data/lyrics/'):
	embeddings = {}
	#print('data/lyrics/'+filename)
	if 'json' not in filename:
		continue
	with open('data/lyrics/'+filename) as f:
		data = json.load(f)
		for key in data:
			song_embedding = np.empty(50)
			print(song_embedding)
			if data[key] == None:
				continue

			for word in data[key].split():
				stripped_word = re.sub('([^\s\w]|_)+', '', word.lower())
				if stripped_word in glove_index_dict:
					song_embedding += glove_embedding_weights[glove_index_dict[stripped_word]]
			print(key)
			print(song_embedding.tolist())
			embeddings[key] = song_embedding.tolist()

	with codecs.open('data/embeddings/'+filename, 'w', encoding='utf-8') as f:
		json.dump(embeddings, f)



