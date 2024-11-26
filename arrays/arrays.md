# Arrays

## largest element in array

- so very first we took a variable that stores the largest number and traversed in array using for loop and after placed a condition
- if arr[i] > largest : we updated the largest and in the end we return the largest.

```python
def LargestElememt(arr : list[int]) -> int:
    largest = arr[0]
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]
            
    return largest


# driver code

# driver code
arr = [2,3,45,90,200]
result = LargestElememt(arr)
print(result)

```

## secondLargest element in array

- so in this we created two variables largest and secondLargest and similar to above we traversed in for loop and

```
  if arr[i] is > largest 
  secondLargest = largest 
  largest = arr[i]
```

- pehle secondLargest ko change karna padega and then we will update the largest
- and hume ek aur elif lagana padega jisme we will check that if
 arr[i] < largest and arr[i] >secondLargest:
 secondLargest = arr[i]

```python
def print2largest(arr):
    largest = arr[0]
    secondLargest = -1
    for i in range(len(arr)):
        if arr[i] > largest:
            secondLargest = largest
            largest = arr[i]   
        elif (arr[i] < largest and arr[i] > secondLargest):
            secondLargest = arr[i]
        
        
    return secondLargest
    
```
