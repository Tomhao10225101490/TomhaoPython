import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
boston_housing = tf.keras.datasets.boston_housing

(train_x, train_y),(test_x,test_y) = boston_housing.load_data(test_split=0.0)

titles = ['CRIM','ZN','INDUS','CHAS','NOX',"RM,'AGE",
          'DIS','RAD','TAX','PTRATIO','B-1000','LSTAT','MEDV']

# print("training set:", len(train_x))
# print("testing set:", len(test_x))
# print("Dim of train_y",train_y.ndim)
# print("Dim of train_y",train_y.shape)
# print(train_x[0:5])
# print(train_x[:,5])

#房价和房间数量的关系
# plt.figure(figsize = (5,5))
# plt.scatter(train_x[:,5],train_y)
# plt.xlabel("RM")
# plt.ylabel("Price($1000's)")
# plt.title("5. RM-Price")
# plt.show()

plt.figure(figsize = (8,8))
for i in range(13):
    plt.subplot(4,4,(i+1))
    plt.scatter(train_x[:,i], train_y)
    plt.xlabel(titles[i])
    plt.ylabel("price($1000's)")
    plt.title(str(i+1)+'.'+titles[i] + '-Price')

plt.tight_layout()
plt.suptitle("各个属性与房价的关系",x=0.5, y=1.02, fontsize=20)
plt.show()