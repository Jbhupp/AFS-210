from random import randint 
import time

def shuffleList(arr):
    n =len(arr)

    for i in range(n):
        # random index
        rand = randint(i, n -1)
        # switch elements
        arr[i], arr[rand] = arr[rand], arr[i]

    return arr
print("Before shuffle:")
print([7, 20, 26, 31, 40, 51, 55, 63, 74, 81])

start_time = time.time()
print("After shuffle:")
print(shuffleList([7, 20, 26, 31, 40, 51, 55, 63, 74, 81]))

end_time = time.time()
print(f"the end time is: {end_time-start_time}")

# I think the time complexity of this algorithm is O(1) since I am only iterating through the length of the list, 
# creating a random index, taking the current index and random index, swapping them around, and this process only completes once. 