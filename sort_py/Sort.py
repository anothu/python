import random
def bubble(a):
    n = len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    print(a)

def selection(a):
    n = len(a)
    for i in range(n-1):
        min = a[i]
        index = i
        for j in range(i+1,n):
            if a[j] < min:
                min = a[j]
                index = j
        a[i],a[index] = a[index],a[i]
    print(a)

def insert(a):
    n = len(a)
    for i in range(1,n):
        temp = a[i]
        for j in range(i-1,-1,-1):
            if temp < a[j]:
                a[j+1],a[j] = a[j],temp
            else:
                break
    print(a)

def shell(a):
    n = len(a)
    gap = n//2
    while gap > 0:
        for i in range(gap,n):
            temp = a[i]
            for j in range(i-gap,-1,-gap):
                if temp < a[j]:
                    a[j+gap],a[j] = a[j],temp
        gap //= 2

def combine(a,low,high,mid):
    temp = [None] * (high - low + 1)
    i = low
    j = mid + 1
    k = 0
    while i<=mid and j<=high:
        if a[i]<a[j]:
            temp[k] = a[i]
            k += 1
            i += 1
        else:
            temp[k] = a[j]
            k += 1
            j += 1
    while i <= mid:
        temp[k] = a[i]
        k += 1
        i += 1
    while j <=high:
        temp[k] = a[j]
        k += 1
        j += 1
    for i in range(len(temp)):
        a[i+low] = temp[i]
def merge(a,low,high):
    if(low<high):
        mid = (low + high)//2
        merge(a,low,mid)
        merge(a,mid+1,high)
        combine(a,low,high,mid)

def quick(a,left,right):
    i = left
    j = right
    index = a[left]
    while i<j :
        while i<j and a[j]>=index:
            j -= 1
        if i<j:
            a[i] = a[j]
            i += 1
        while i<j and a[i]<index:
            i += 1
        if i<j:
            a[j] = a[i]
            j -= 1
    a[i] = index
    return i
def quickSort(a,l,r):
    if l<r:
        i = quick(a,l,r)
        quickSort(a,l,i-1)
        quickSort(a,i+1,r)

def bulidMaxHeap(a,len):
    for i in range(len//2-1,-1,-1):
        if (a[i] < a[2 * i + 1] and (2 * i + 1) < len):
            temp = a[i]
            a[i] = a[2 * i+1]
            a[2 * i+1] = temp

        if (((2 * (2 * i + 1) + 1) < len and a[2 * i + 1] < a[2 * (2 * i + 1) + 1]) or (
                (2 * (2 * i + 1) + 2) < len and a[2 * i + 1] < a[2 * (2 * i + 1) + 2])) :
            bulidMaxHeap(a, len)


        if ((2 * i + 2) < len and a[i] < a[2 * i + 2]):
            temp = a[i];
            a[i] = a[2 * i+2];
            a[2 * i+2] = temp;

        if (((2 * (2 * i + 2) + 1) < len and a[2 * i + 2] < a[2 * (2 * i + 2) + 1]) or (
                (2 * (2 * i + 2) + 2) < len and a[2 * i + 1] < a[2 * (2 * i + 2) + 2])):
            bulidMaxHeap(a, len)

#begin
arr = [random.randint(0,99) for i in range(10)]
print(arr)
bulidMaxHeap(arr,len(arr))
print(arr)