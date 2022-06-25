from imports import *
from Utils import *
from loadData import *
import tensorflow as tf
import time
from tensorflow.keras.models import load_model


data = Standardization(makeTestData(150,100))

print(data.shape)


model = load_model('../Models/Model.h5')
predictions = model.predict(data[0,None])
print(predictions[0])

toc = time.time()
result = model.predict(data[1,None])
tic = time.time()

print("prediction time : ", tic-toc)
