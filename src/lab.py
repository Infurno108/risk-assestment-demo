import numpy as np
import keras as kr

wackyZacky = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

zackyWacky = np.array([[0], [1], [1], [0]])


xorNetwork = kr.models.Sequential()
xorNetwork.add(kr.layers.Dense(16, input_dim=2, activation='relu'))
# 16 here sets up the assumption that there are 16 neurons in the hidden layer
xorNetwork.add(kr.layers.Dense(1))
# 1 here is just the ouput layers size, the input is just assumed to be the hidden layer @ 16

xorNetwork.compile(loss='mean_squared_error',
                   optimizer='adam',
                   metrics=['binary_accuracy'])


xorNetwork.fit(wackyZacky, zackyWacky, epochs=1000, verbose=100)

print(xorNetwork.predict(wackyZacky))
