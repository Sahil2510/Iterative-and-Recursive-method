import random
import time
import psutil
import matplotlib.pyplot as plt
import sys
import os
sys.setrecursionlimit(10000000)


def mem():
    print(psutil.virtual_memory())
    x=psutil.Process(os.getpid())
    mem=x.memory_full_info()[0]/float(2**20)
    return mem

def mergeSort(array):
    c = 1
    while c < len(array) - 1:
        left = 0
        while left < len(array) - 1:
            mid = min((left + c - 1), (len(array) - 1))
            right = ((2 * c + left - 1, len(array) - 1)[2 * c + left - 1 > len(array) - 1])
            merge(array, left, mid, right)
            left = left + c * 2
        c = 2 * c
def merge(array, left, middle, right):
    n1 = middle - left + 1
    n2 = right - middle
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = array[left + i]
    for i in range(0, n2):
        R[i] = array[middle + i + 1]
    i, j, k = 0, 0, left
    while i < n1 and j < n2:
        if L[i] > R[j]:
            array[k] = R[j]
            j += 1
        else:
            array[k] = L[i]
            i += 1
        k += 1
    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1

def partition(arr, l, h):
    i = (l - 1)
    x = arr[h]
    for j in range(l, h):
        if arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return (i + 1)

def quickSortIterative(arr, l, h):
    size = h - l + 1
    stack = [0] * (size)
    top = -1
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
    while top >= 0:
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
        p = partition(arr, l, h)
        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h

def merge_sort(arr):
    n=len(arr)
    if n>1:
        mid=n//2
        L=arr[:mid]
        R=arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i,j,k=0,0,0
        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            arr[k]=R[j]
            j+=1
            k+=1

def pivot(arr, low, high):
    i=low-1
    pivot=arr[high]
    for j in range(low,high):
        if arr[j]<pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

def quick_sort(arr,low,high):
    if low<high:
        pi=pivot(arr, low, high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)



#Taking random numbers from random library'''

n = int(input("Enter number : "))
print("Before anything: ",mem())
ar = random.sample(range(0, n), n)
start = time.time()
merge_sort(ar)
end = time.time()
print("\nAfter merge rec: ", mem())
print("Runtime of the merge sort rec is ",end-start)
ar = random.sample(range(0, n), n)
start = time.time()
quick_sort(ar,0,n-1)
end = time.time()
print("\nAfter quick rec: ", mem())
print("Runtime of the quick sort rec is ",end-start)
arr = random.sample(range(0, n), n)
start = time.time()
quickSortIterative(arr,0,n-1)
end = time.time()
print("\nAfter quick iter: ", mem())
print("Runtime of the quick sort iter is ",end-start)
arr = random.sample(range(0, n), n)
start = time.time()
mergeSort(arr)
end = time.time()
print("\nAfter merge iter: ", mem())
print("Runtime of the merge sort iter is ",end-start)

list_n = [10,100,1000,100000]
list_mergei = []
list_quicki = []
list_merger = []
list_quickr = []
for array_size in list_n:
    arr = random.sample(range(0, array_size), array_size)
    start = time.time()
    quick_sort(arr, 0, array_size - 1)
    end = time.time()
    q = end - start
    list_quickr.append(q)
    arr = random.sample(range(0, array_size), array_size)
    start = time.time()
    merge_sort(arr)
    end = time.time()
    m = end - start
    list_merger.append(m)
    arr = random.sample(range(0, array_size), array_size)
    start = time.time()
    quickSortIterative(arr, 0, array_size - 1)
    end = time.time()
    q = end - start
    list_quicki.append(q)
    arr = random.sample(range(0, array_size), array_size)
    start = time.time()
    mergeSort(arr)
    end = time.time()
    m = end - start
    list_mergei.append(m)
print("\nMerger Recursive",list_merger)
print("\nQuick  Recursive",list_quickr)
print("\nMerge Itteration",list_mergei)
print("\nQuick Itteration",list_quicki)
plt.plot(list_n,list_merger)
plt.plot(list_n,list_quickr)
plt.plot(list_n,list_mergei)
plt.plot(list_n,list_quicki)
plt.legend(['merge rec','quick rec','merge iter','quick iter'],bbox_to_anchor=(1.1,1.15),ncol=5)
plt.show()