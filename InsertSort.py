def insertSort(a):
    n = len(a)
    for i in range(1,n):
        x = a[i]
        j = i - 1
        while j >= 0:
            if x <= a[j]:
                a[j+1] = a[j]
                j -= 1
            else:
                break
        a[j+1] = x
        print(a)
list = [3,2,1,5,4]
print(list)
insertSort(list)
print(list)