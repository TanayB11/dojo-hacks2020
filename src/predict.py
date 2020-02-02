import json, pickle, cv2
import numpy as np
from tensorflow.python.keras.models import model_from_json

# These two are for preprocessing inputs to the model
def extract_data_predict(path):
    data = []
    image = cv2.imread(path)
    image = cv2.resize(image, (32, 32))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    data.append(image)
    data = np.array(data)
    return (data.reshape(1, 32, 32, 1))

def normalize_predict(arr):
	norm = arr.astype('float32')
	norm = norm / 255.0
	return norm

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
test_img = 'test-imgs/test1.png' #TODO: Change to image
sample = normalize_predict(extract_data_predict(test_img))
sample = model.predict(sample)

# Print all predictions and probabiliites
with open('../logs/predictions.txt', 'w') as f:
    for i in range(len(sample[0])):
        pred = str(i) + ' ' + char_dict.get(i) + ' ' + str(sample[0][i]) + '\n'
        f.write(pred)
        print(pred)

# Final prediction
maxindex = sample.argmax() # Index of largest item
print('Prediction: ', maxindex, char_dict.get(maxindex), ' ', sample[0][maxindex])
