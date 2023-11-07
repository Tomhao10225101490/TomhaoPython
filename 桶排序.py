#先实现选择排序
def SelectSort(a):
    n = len(a)
    for i in range(0,n):
        min = i
        for j in range(i+1, n):
            if a[j] > a[min]:
                min = j
        a[min],a[i] = a[i], a[min]

def BucketSort(a):
    maxV = max(a)
    minV = min(a)
    BucketCount = 3
    Buckets = [[],[],[]]
    perBucket = (maxV - minV + BucketCount) // BucketCount

    for num in a:
        BucketIndex = (maxV - num) // perBucket
        Buckets[BucketIndex].append(num)

    for i in range(BucketCount):
        SelectSort(Buckets[i])

    idx = 0
    for i in range(BucketCount):
        for j in Buckets[i]:
            a[idx] = j
            idx += 1

test = [4,3,1,5,2]
print(test)
BucketSort(test)
print(test)



