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

## left rotate the array by 1 place

ek for loop mai starting from 1 arr ka 0 elemnt ko temp mai store kardiya and then har 
arr[i-1] ko arr[i] ka value dediya and last mai last element ko temp dediya and then return

```python
def rotateArray(arr):
    temp = arr[0]
    for i in range(1,len(arr)):
        arr[i-1] =  arr[i]
        
    arr[len(arr)-1] = temp
    
    return arr

```


## Left rotate array by d places


```python
def rotateArray(arr, n, d):
    # To handle cases where d is greater than n
    d = d % n
    # Slice and concatenate the array
    return arr[d:] + arr[:d]
```
##### brute Force
```python
arr = [1, 2, 3, 4, 5, 6, 7]
d = 3
n= len(arr)
temp = arr[0:d]
print(temp)
for i in range(d,n):
  arr[i-d] = arr[i]
# idhar ek naya variable j lelenge 
j = 0
for i in range(n-d,n):
  arr[i] = temp[j]
  j +=1

print(arr) 
``` 
##### better
```python
arr = [1, 2, 3, 4, 5, 6, 7]
d = 3
n= len(arr)
temp = arr[0:d]
print(temp)
for i in range(d,n):
  arr[i-d] = arr[i]

for i in range(n-d,n):
  arr[i] = temp[i-(n-d)]
  # temp[i-(n-d)] : reason bcoz we are standing at n-d and if we substract n-d we get 0 ,1 2 
  # so humko ek naya variable nhi lena padega
  j +=1
print(arr) 
```
##### best
1stly array ko reverse kardiya and then array ke starting elements upto k using slicing nums[:k] ko reverse karke usme hi store kardiya using reversed and then same with [k:] k se last tak and return original array
```python
def rotateArray(nums: List[int], n: int ,k: int ) :
  
  n = len(nums)
  k %= n
  nums.reverse()
  nums[:k] = reversed(nums[:k])
  nums[k:] = reversed(nums[k:])
  
  return nums
```

