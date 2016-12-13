

import tensorflow as tf
import numpy as np

import matplotlib.pyplot as plt
#%matplotlib inline

mnist = tf.contrib.learn.datasets.load_dataset('mnist')

train_data = mnist.train.images
train_label = np.asarray(mnist.train.labels, dtype = np.int32)

test_data = mnist.test.images
test_label = np.asarray(mnist.train.labels, dtype = np.int32)

max_example = 500

train_data = train_data[:max_example]
train_label = train_label[:max_example]

#Disaply a MNIST image
def displayImage(i):
    img = test_data[i]
    plt.title('Example: %d ,Label: %d' % (i, test_label[i]))
    plt.imshow(img.reshape((28, 28)), cmap = plt.cm.gray_r)

displayImage(1)


