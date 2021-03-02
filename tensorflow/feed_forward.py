import sys
import tensorflow as tf
import pandas as pd
import numpy as np
from tensorflow.keras import models, layers

# Generate data randomly
# Generated data is already normalized with mean=0 and standard deviation is 1
x_train = np.random.normal(loc = 0,scale=1.0, size = (10000,200))
y_train = np.random.choice(np.arange(2),size = (10000))
print(x_train.shape)
print(y_train.shape)



def make_model():

	model = Sequential()
	model.add(layers.Dense(x_train.shape[]))

# visualize data



	