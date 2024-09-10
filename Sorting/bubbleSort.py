#  function defination
#  time complexity is O(n^2)


def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
      for j in range(0 , n-i-1):
          if arr[j] > arr[j+1]:
            arr[j] , arr[j+1] = arr[j+1] , arr[j]
    return arr



#  driver code

arr = [70, 20, 50, 30, 90, 5, 15]
result = bubbleSort(arr)
print("your array after bubble sort is :", result)
print()