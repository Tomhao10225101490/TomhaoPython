def selectSort( _list):
    n = len(_list)
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if _list[j] < _list[min]:
                min = j
        _list[min],_list[i]  = _list[i],_list[min]
        print(_list)

a = [9,11,13,4,6,5,7,12,1]
selectSort(a)