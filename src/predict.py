import json, pickle, cv2
import numpy as np
from tensorflow.python.keras.models import model_from_json

drawing=False
mode=True
# These two are for preprocessing inputs to the model
def extract_data_predict(path):
    data = []
    im = cv2.imread(path)
    im = cv2.resize(im, (32, 32))
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    data.append(im)
    data = np.array(data)
    return (data.reshape(1, 32, 32, 1))

def normalize_predict(arr):
	norm = arr.astype('float32')
	norm = norm / 255.0
	return norm

def prediction():
    # Load the model and weights
    with open('../model/model.json', 'r') as f:
        model = f.read()
        model = model_from_json(model)
    model.load_weights('../model/weights.h5')
    model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


    # Allows predictions to be mapped to classes and characters
    with open('char_dict', 'rb') as f:
        char_dict = pickle.load(f)
    char_dict = dict([(value, key) for key, value in char_dict.items()])

    # Use the model to predict an image
    test_img = 'image.png' #TODO: Change to image
    sample = normalize_predict(extract_data_predict(test_img))
    sample = model.predict(sample)

    # Final prediction
    maxindex = sample.argmax() # Index of largest item
    return char_dict.get(maxindex)
