import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_train) = mnist.load_data()

plt.imshow(x_train[6942])
plt.show()

