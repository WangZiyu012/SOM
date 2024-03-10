import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from minisom import MiniSom
from pylab import bone, pcolor, colorbar, plot, show

dataset = pd.read_csv('neuropil_synapse_table.csv')

X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, -1].values

# scaling

from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range=(0,1))

# fit sc var. to x s.t. sc gets all the info from x to apply normalization

X = sc.fit_transform(X)

# train SOM using MiniSOM module to train

som = MiniSom(x=150,y=150,input_len=320, sigma= 1.5, learning_rate= 0.5)

# initialize the initial weight of the SOM

som.random_weights_init(X)

# training process

som.train_random(data=X, num_iteration=500)

# visualization
# 1. put different winning nodes on the map, by adding the MID on the neurons (color)
bone()
pcolor(som.distance_map().T)
show()