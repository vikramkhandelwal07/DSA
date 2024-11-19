# Sorting

## Selection Sort

### select the minimum

swap at index 0 & minimum among [0,n-1]
swap at index 1 & minimum among [1,n-1]
swap at index 2 & minimum among [2,n-1]
ye jayega n-2 tak kyuki last elements is always Sorted.
isme chota dhundte hai then usko swap kardete hai and ek loop kel bad ek element swap ho jata hai ...
not so effcient in real life

```python
#  time complexity is O(n^2)
def selectionSort(arr):
  n = len(arr)
  for i in range(n):
    mini = i
    for j in range(i+1,n):
      if arr[j] < arr[mini]:
        arr[j], arr[mini] = arr[mini],arr[j]
  return arr

arr = [76,23,199,3,98,65,32,11,2]
output = selectionSort(arr)
print(output)
```

## Bubble Sort

- pushes the maximum to last by adjacent swaps

```python
# time complexity O(n^2)-for worst and avg
# for best - O(n)
# 
def BubbleSort(arr):
  n = len(arr)
  for i in range(n):
    didSwap = 0
    for j in range(n,i,-1):
      if arr[j] < arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        didSwap = 1
    
    if didSwap == 0:
      break
  return arr

# some improvement in algo
arr = [76,23,199,3,3,98,98,65,32,11,2]
output = selectionSort(arr)
print(output)
```

## Insertion Sort

- takes an element and place it in it's correct order.

```python
# time complexity O(n^2)
# best case O(n )
def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):  # Start from 1 since the first element is already considered sorted
        key = arr[i]
        j = i - 1
        while j >=0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Driver code
arr = [76,23,199,3,3,98,98,65,32,11,2]
result = insertionSort(arr)
print("Your array after insertion sort is:", result)
   
```

## mergeSort

- Divide and merge
- time complexity O(N*logN)

```python


def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1

    # Merge two halves into the temp array
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    # Copy remaining elements of left half, if any
    while left <= mid:
        temp.append(arr[left])
        left += 1

    # Copy remaining elements of right half, if any
    while right <= high:
        temp.append(arr[right])
        right += 1

    # Copy the sorted temp array back to the original array
    for i in range(len(temp)):
        arr[low + i] = temp[i]


def mergeSort(arr, low, high):
    if low < high:  # Base case: when low is not less than high, return
        mid = (low + high) // 2
        mergeSort(arr, low, mid)
        mergeSort(arr, mid + 1, high)
        merge(arr, low, mid, high)
    return arr


# Example usage
arr = [76, 23, 199, 3, 3, 98, 98, 65, 32, 11, 2]
low = 0
high = len(arr) - 1
result = mergeSort(arr, low, high)
print("Your array after mergesort is:", result)
```

## QuicKSort

```python


```