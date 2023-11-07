import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
TRAIN_URL = 'http ://download.tensorflow.org/data/iris_training.csv'
train_path = tf.keras.utils.get_file('iris_training.csv',TRAIN_URL)
COLUMNS_NAMES =  ['SepalLength', 'SepalWidth', 'PetalLength','Petalwidth','Species']
df_iris = pd.read_csv(train_path,header = 0,names = COLUMNS_NAMES)

print(df_iris.head(3))
print(type(df_iris))
print('the dim of df_iris is',df_iris.ndim)
print('the shape of df_iris is',df_iris.shape)
print('the size of df_iris is',df_iris.size)
# print(df_iris.describe())

iris = np.array(df_iris)
# iris = df_iris.values
# iris = df_iris.as_matrix()#这个是旧版的pandas才有的，新版已经删除了，用values就OK
print('the type of df_iris is', type(df_iris))
print('the type of iris is', type(iris))
# print(iris[0:6])
print('================================')
# print(iris[:6,:4])

# plt.scatter(iris[:,2], iris[:,3],c = iris[:,4], cmap = 'brg',marker='*')
# plt.title("Anderson's Iris Data Set\n(Bule->Setosa | Red->Versicolor | Green->Virginica)")
# plt.xlabel(COLUMNS_NAMES[2])
# plt.ylabel(COLUMNS_NAMES[3])
# plt.show()
fig = plt.figure('Iris Data', figsize = (12,12))
fig.suptitle("Anderson's Iris Data Set\n(Bule->Setosa | Red->Versicolor | Green->Virginica)")
for i in range(4):
    for j in range(4):
        plt.subplot(4,4, i + 1 + 4*j)
        if(i == j):
            plt.text(0.3,0.5,COLUMNS_NAMES[j],fontsize = 15)
        else:
            plt.scatter(iris[:,i], iris[:,j], c= iris[:,4], cmap = 'brg',marker='*')
        if j==0:
            plt.title(COLUMNS_NAMES[i])
        if i==0:
            plt.ylabel(COLUMNS_NAMES[j])
plt.tight_layout(rect=[0,0,1,1])
plt.show()

