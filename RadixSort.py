def RadixSort(a):
    """
    The RadixSort function implements the radix sort algorithm to sort a list of integers in ascending order.
    
    :param a: The parameter "a" in the RadixSort function is a list of integers that you want to sort using the radix sort algorithm
    """
    base = 1
    maxlen = max(a)
    while base <= maxlen:
        buckets = []
        for i in range(10):
            buckets.append([])
        for num in a:
            index = (num // base) % 10
            buckets[index].append(num)
        l = 0
        for i in range(10):
            for j in buckets[i]:
                a[l] = j
                l += 1
        print(a)
        base *= 10
test = [10,4,3,7,5,9,1,2]
print(test)
RadixSort(test)
print(test)