import time
import random

def quick_sort(a_list, start, end):
    if start >= end:
        return

    pivot = partitionStart(a_list, start, end)
    quick_sort(a_list, start, pivot-1)
    quick_sort(a_list, pivot+1, end)
        

def partitionStart(a_list, start, end):
    return partition(a_list, start, end)

def partition(a_list, start, end):
    pivot = a_list[start]
    
    low = start + 1
    high = end

    while True:
        while low <= high and a_list[high] >= pivot:
            high = high - 1

        while low <= high and a_list[low] <= pivot:
            low = low + 1

        if low <= high:
            a_list[low], a_list[high] = a_list[high], a_list[low]
            
        else:
            
            break

    a_list[start], a_list[high] = a_list[high], a_list[start]

    return high


print("Quick Sort:")

myList = [x for x in range(1000)]
random.shuffle(myList)


start_time = time.time()
quick_sort(myList,0,len(myList)-1)
end_time = time.time()

print(f"The execution time is: {end_time-start_time}")

def quickSort2(sequence):
    length = len(sequence)
    if length <=1:
        return sequence
    else:
        pivot = sequence.pop()
        # print(pivot, "line 81")
    
    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quickSort2(items_lower) + [pivot] + quickSort2(items_greater)


start_time = time.time()
sequence = [x for x in range(1000)]
random.shuffle(sequence)

quickSort2(sequence)
end_time = time.time()
print(f"The execution time is: {end_time-start_time}")

def qsort(a, low, hi):
    if(low >= hi):
        return
    p = a[(low + hi) // 2]       
    i = low - 1
    j = hi + 1
    while(1):
        while(1):              
            i += 1
            if(a[i] >= p):
                break
        while(1):               
            j -= 1
            if(a[j] <= p):
                break
        if(i >= j):
            break
        a[i],a[j] = a[j],a[i]
    qsort(a, low, j)
    qsort(a, j+1, hi)
    return(qsort)
    


start_time = time.time()
a = [x for x in range(1000)]
random.shuffle(a)

qsort(a, 0, len(a)-1)
end_time = time.time()
# print(a)
print(f"The execution time is: {end_time-start_time}")


def randQuickSort(list):
    def sorting(first, l, r):
        if r <= l:
            return
        pivot_index = random.randint(l,r)

        first[l], first[pivot_index]= first[pivot_index], first[l]

        i = l
        for j in range(l+1, r+1):
            if first[j]< first[l]:
                i +=1
                first[i], first[j] = first[j], first[i]

        first[i], first[l] = first[l], first[i]

        sorting(first, l, i-i)
        sorting(first, i+1, r)
    if list is None or len(list) < 2 :
        return
    sorting(list, 0, len(list)-1)


start_time = time.time()
list = [x for x in range(1000)]
random.shuffle(list)

randQuickSort(list)
end_time = time.time()

print(f"The execution time is: {end_time-start_time}")