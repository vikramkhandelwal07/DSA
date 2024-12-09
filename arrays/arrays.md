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

## 5.Moves zero to end

two pointer type use kiya hai 0 ko j pr rkha hai and i ko numbers mai rakha hai...and then swap kiya hai..

```python
def moveZeroes(nums) -> None:
  """
  Do not return anything, modify nums in-place instead.
  """
  j=-1
  for i in range(len(nums)):
    if nums[i] == 0:
      j = i
      break
  i = j+1
  for i in range(j+1,len(nums)):
    if nums[i] != 0:
      # swap
      nums[i],nums[j] = nums[j],nums[i]
      j+=1
  return nums
nums = [1,0,1,0,3,12]
res = moveZeroes(nums)
print(res)
```


## 6. Union of array

simply using in and not in operator in python

```python
a= [14,1, 2, 3, 4, 5]
b = [1, 2, 3, 6, 7,4,4]
for i in b:
  if i not in a :
    a.append(i)
print(sorted(a))
```


## 7. Missing Number (268)

ye approach that came to my find was in for loop traverse and if that i is not in nums that the number 
```python
def missingNumbers(nums):
  n = len(nums)
  for i in range(n+1):
    if i not in nums:
      return i
nums = [9,6,4,2,3,5,7,0,1]
ans = missingNumbers(nums)
print(ans)
```

best or optimal approach is using `sum of n natural numbers - sum of array`

```python
def missingNumbers(nums):
  n = len(nums)
  sum_ = (n*(n+1))//2
  missing_sum = sum(nums)
  number = sum_ - missing_sum
  return number
  
nums = [9,6,4,2,3,5,7,0,1]
ans = missingNumbers(nums)
print(ans)
```


## 8. Max Consecutive Ones 485

this was the solution that came to my mind that we will take an empty arr and count variable , and traverse in the nums if we get one we update the count and if we get anything other than one we append the previous count value in the arr and reset count to 0 and in the end we return the max value from the array


```python
def consecutiveOnes(nums):
  arr = []
  count = 0
  n = len(nums)
  for i in range(n):
    if nums[i] == 1:
      count +=1
    elif nums[i] !=1:
      arr.append(count)  
      count = 0
    arr.append(count)  
  return max(arr)
nums =[1,1,0,1,1,1]
result = consecutiveOnes(nums)
print(result)
```
best approach instead of using arry we can keep a variable of maximum 
```python
def consecutiveOnes(nums):
  maxi = 0
  count = 0
  n = len(nums)
  for i in range(n):
    if nums[i] ==1:
      count+=1
      maxi = max(count , maxi)    
    else:
      count = 0
  return maxi
  
nums =[1,1,0,1,1,1,0]
result = consecutiveOnes(nums)
print(result)
```

## 9. Single Number 136

```python 
# TC - O(n)
# SC - O(1)
def singleNumber(nums):
        xor1 = 0
        for i in range(len(nums)):
            xor1 = xor1 ^ nums[i]
        return xor1
nums = [2,3,4,5,4,3,5]
result = singleNumber(nums)
print(result)
```
because a ^ a = 0 and a ^ 0 = a toh isme sab do bar hai toh xor karne pe it will be like 
2^ 3^ 4^ 5^ 4^ 3^ 5 so isme last mai sab zero ^ 2 hoga and usme it will return 2

