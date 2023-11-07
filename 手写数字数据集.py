import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
mnist = tf.keras.datasets.mnist
(train_x, train_y),(test_x, test_y) = mnist.load_data()
print("Training set",len(train_x))
print("Testing set",len(test_x))
print("Train_x: ",train_x.shape, train_x.dtype)
print("Train_y: ",train_y.shape, train_y.dtype)

for i in range(8):
    num = np.random.randint(1,60000)

    plt.subplot(2,4,i+1)
    plt.axis('off')
    plt.imshow(train_x[num], cmap = 'gray')
    plt.title(train_y[num])
plt.show()

