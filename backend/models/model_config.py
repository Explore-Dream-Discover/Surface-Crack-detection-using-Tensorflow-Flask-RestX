from logging import exception
from keras.models import load_model
import os

model_path = 'backend/models/Surface_detection_cnn.h5'

def model_loading():
    calling_cnn = load_model(model_path)
    print("Model Loaded")
    return calling_cnn


print(model_loading)    




