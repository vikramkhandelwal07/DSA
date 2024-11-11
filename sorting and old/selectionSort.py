#  function defination
#  time complexity is O(n^2)


def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1 , n):
            if arr[j] < arr[min_idx]:
                arr[j] , arr[min_idx] = arr[min_idx] , arr[j]
    return arr
    
# driver code 

arr = [70, 20 ,50 , 30, 90, 5, 15]
result = selectionSort(arr)
print("your array after selection sort is :", result)