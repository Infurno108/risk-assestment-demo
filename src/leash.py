import keras as kr
import numpy as np
import tensorflowjs as tfjs
# converts keras model to tensorflow.js
dog = kr.models.load_model('riskyBusiness.h5')
tfjs.converters.save_keras_model(dog, 'dog.json')
# bash
