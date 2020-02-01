import os, h5py
import numpy as np
import cv2

def extract_data(path):
    labels = []
    data = []
    numOfItems = 0
    for i, label in enumerate(sorted(os.listdir(path))):
        if (label != '.DS_Store'):
            for j, filename in enumerate(os.listdir(os.path.join(path, label))):
                image = cv2.imread(os.path.join(path, label, filename))
                image = cv2.resize(image, (64, 64))
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                data.append(image)
                labels.append(i-1)
                numOfItems += 1
    data = np.array(data)
    return (data.reshape(numOfItems, 32, 32, 1), np.array(labels))

def normalize(trainX, testX):
	train_norm = trainX.astype('float32') / 255.0
	test_norm = testX.astype('float32') / 255.0
	return train_norm, test_norm

train_path = '../data/train'
test_path = '../data/test'
print('Extracting Train...')
(trainX, trainY) = extract_data(train_path)
print('Extracting Test...')
(testX, testY) = extract_data(test_path)
print('Normalizing...')
trainX, testX = normalize(trainX, testX)
print('Saving...')

print(trainX.shape, testX.shape, trainY.shape, testY.shape)

# Save preprocessed data
with h5py.File('../data/compressed/trainX.h5', 'w') as f:
   f.create_dataset('trainX', data=trainX, compression='gzip', compression_opts=6)
with h5py.File('../data/compressed/testX.h5', 'w') as f:
   f.create_dataset('testX', data=testX, compression='gzip', compression_opts=6)
with h5py.File('../data/compressed/trainY.h5', 'w') as f:
   f.create_dataset('trainY', data=trainY, compression='gzip', compression_opts=6)
with h5py.File('../data/compressed/testY.h5', 'w') as f:
   f.create_dataset('testY', data=testY, compression='gzip', compression_opts=6)
