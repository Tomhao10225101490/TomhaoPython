def countingSort(a):
    cntlen = max(a) + 1
    cnt  = [0] * cntlen #建立len为cntlen的都为0的数组
    for i in a:
        cnt[i] += 1
    n = 0
    for i in range(0, cntlen):
        while cnt[i] > 0:
            a[n] = i
            n += 1
            cnt[i] -= 1
test = [4,3,1,5,2]
print(test)
countingSort(test)
print(test)
