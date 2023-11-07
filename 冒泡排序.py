def bubbleSort(a):
    """
    The function implements the bubble sort algorithm to sort a given list in descending order.
    
    :param a: The parameter "a"# The ` ` in the code is used to print the current state of the list after each iteration of the outer loop in the bubble sort algorithm. It helps visualize the sorting process and see how the elements are being swapped and rearranged.
     in the bubbleSort function is a list of numbers that you want to sort in descending order
    """
    n = len(a)
    for i in range(n-1, -1, -1):
        for j in range(0, i):
            if a[j] < a[j+1]:
                a[j],a[j+1] =a[j+1], a[j]
        print(a)
list = [3,2,1,4,5,0]
bubbleSort(list)
