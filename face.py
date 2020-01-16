import face_recognition
import os
import numpy as np
from PIL import Image, ImageDraw
from IPython.display import display

print("gg")
def loadfaces(path) : 
# directory = 'faces'
	known_face_encodings = []
	known_face_names = []
	for filename in os.listdir(path):
		if filename.endswith(".jpg"):
			Image = face_recognition.load_image_file(path + filename)
			known_face_encodings.append(face_recognition.face_encodings(Image)[0])
			known_face_names.append(filename)
			continue
		else:
			continue
	return known_face_encodings,known_face_names

directory = 'faces1/'

known_face_encodings,known_face_names = loadfaces(directory)
path = "faces/"
for filename in os.listdir(path):
	if filename.endswith(".jpg"):
		Image = face_recognition.load_image_file(path + filename)
		face_encoding = face_recognition.face_encodings(Image)[0]
		matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
		face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
		best_match_index = np.argmin(face_distances)
		print(best_match_index)
		if matches[best_match_index]:
			name = known_face_names[best_match_index]
			print(name)
			continue
	else:
		continue
