#Task 1
import time

def newlist(n):
    squares = []

    for num in range(n+1):
        squares.append(num**2)

    return squares

t1_start_time = time.time()
print(newlist(30))
t1_end_time = time.time()

t1_time = t1_end_time - t1_start_time
print('Time taken to create the list: ', t1_time) # Time complexity is O(n) since the longer the list is the more time it takes


#Task 2
test = newlist(10)
def reverse_sublist(list, i, j):
    sublist = list[i:j]

    sublist.sort(reverse=True)

    list[i:j] = sublist

    return list

t2_start_time = time.time()
print(reverse_sublist(test, 4, 50))
t2_end_time = time.time()

t2_time = t2_end_time - t2_start_time
print('Time taken to reverse the sublist: ', t2_time) # Time complexity is O(n log n) since I use sort


#Task 3
merge1 = [16, 25, 36, 49, 64, 81, 100, 0, 1, 4, 9]
merge2 = [0, 1, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 4, 9, 16, 25, 36, 49, 64, 841, 900]
def merge_sorted(l1, l2):
    l1.sort()
    l2.sort()

    merged = l1+l2

    return merged

t3_start_time = time.time()
print(merge_sorted(merge1, merge2))
t3_end_time = time.time()

t3_time = t3_end_time - t3_start_time
print('Time taken to sort and merge lists: ', t3_time) # Time complexity is O(n log n) since I use sort