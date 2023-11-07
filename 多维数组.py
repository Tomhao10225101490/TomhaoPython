import numpy as np
def fun(arr):
    shape = arr.shape
    flattened =  arr.flatten()
    np.random.shuffle(flattened)
    ans = flattened.reshape(shape)
    return ans
a = np.arange(1,10).reshape(3, 3)
print(fun(a))