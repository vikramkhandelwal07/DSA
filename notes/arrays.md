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



## 10. Longest subArray with sum k (+ve ,-ve)

- two problems one array having positive negatives both so this is the best solution...
- this is the best approach for array having positive negatives both using dictionary we go ahead and check whether the sum - k exist in dict and
- if yes the rem is  the length of subarray
- and if not then we add that sum in dict for checking it further when we move more ahead
```python
from typing import List
def longestSubArray(nums,k):
  n = len(nums)
  preSummap = {}
  sum_ = 0
  maxi = 0  
  for i in range(n):
    sum_ += nums[i]
    if sum_ == k :
      maxi = max(maxi, i+1)
    rem = sum_ - k
    
    if rem in preSummap:
      length = i - preSummap[rem]
      maxi = max(maxi , length)

    if rem not in preSummap:
      preSummap[sum_] = i
  return maxi
  
nums = [2, 3, 5, 1, 9]
k = 10
length = longestSubArray(nums, k)
print(f"The length of the longest subarray is: {length}")
```
## 11. Longest subArray with sum k (only +ve )
best solution for the array having only positives is 

- now for best in case of positive and zero hum kya karenge ki hum left se right jayenge and then we will check at each i is the sum is greater than k
- if yes than hum left se ek ek trim karenge ....so it is like pehle aage jao and piche ka kat do aur barabar kardo sum ke ...
- go ahead trim from the left , go ahead trim from the left
- we will be using two pointer

```python
# TC - O(2N) because andar wala while loop har bar pura nahi chal raha hai ...thoda hi chalta hai like one or two places in each pass and overall you can assume it to be moving N times at worst case
# SC - O(1)
def longestSubArray(nums , k):
  left = 0
  right = 0
  n= len(nums)
  Sum = nums[0]
  maxLength = 0
  
  while right < n:
    while (left <= right and Sum > k):
      Sum -= nums[left]
      left +=1
    if Sum == k:
      maxLength = max(maxLength,right-left+1)
    right +=1
    if (right < n) :
      Sum += nums[right]
  return maxLength

arr = [10, 5, 2, 7, 1, 9]
k = 15
result = longestSubArray(arr, k)
print(result)
```

## 12. Two Sum

#### brute force
- simple ek element lo aur sabke sath + karke dekho jo match karta hai wo answer
- TC - O(N^2)
```python
def twoSum(nums,target):
  n = len(nums)
  for i in range(n):
    for j in range(i+1,n):
      if nums[i] + nums[j] == target:
        return [i,j]
        
nums = [2,7,11,15]
target = 9
result = twoSum(nums, target)
print(result)
```
#### better ya best
- hi hai ye bss with dict hai and agar without dictionary bola toh we can use below approach
```python
# TC - O(N)
# SC - O(N)
def twoSum(nums, target):
        hashMap = {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in hashMap:
                return [hashMap[complement], i]
            hashMap[num] = i
        return []
        
nums = [2,7,11,15]
target = 9
result = twoSum(nums, target)
print(result)
```

#### best ya better hi hai isme just without using dict hai

- using two pointers first sort the array and then using two pointer you can calculate the sum
```python
# TC - O(N)
# SC - O(1)
def twoSum(nums, target):
  nums = sorted(nums)
  left = 0
  right = len(nums)-1
  for i in range(len(nums)):
    if nums[left] + nums[right] == target:
      return [left, right]
    elif nums[left] + nums[right] < target:
      left+=1
    else:
      right-=1
nums = [2,7,11,15]
target = 9
result = twoSum(nums, target)
print(result)
```

## 13. Sort array of 0/1/2 or sort colors

#### Brute
- merge sort
```python
def sortColoursMerge(nums, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    # Merge the two halves
    while left <= mid and right <= high:
        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left += 1
        else:
            temp.append(nums[right])
            right += 1
    # Copy remaining elements of the left half, if any
    while left <= mid:
        temp.append(nums[left])
        left += 1 
   # Copy remaining elements of the right half, if any
    while right <= high:
        temp.append(nums[right])
        right += 1
    # Copy sorted elements back into the original array
    for i in range(len(temp)):
        nums[low + i] = temp[i]
        
def MergeSort(nums, low, high):
    if low < high:
        mid = (low + high) // 2
        MergeSort(nums, low, mid)
        MergeSort(nums, mid + 1, high)
        sortColoursMerge(nums, low, mid, high)
    return nums
    
nums = [2, 0, 2, 1, 1, 0]
low = 0
high = len(nums) - 1
result = MergeSort(nums, low, high)
print("After sorting:", result)
```

#### better
- since i know array only has 0 1 and 2 so i will traverse the loop once and then create 3 variable cnt1 cnt2 and cnt3 and then overwrite the original array
```python
# TC - O(2N)
# SC - O(1)
def SortColors(nums):
  cnt1 = 0
  cnt2 = 0
  cnt0 = 0
  for i in range(len(nums)):
    if nums[i] == 0 :
      cnt0 +=1
    elif nums[i] == 1:
      cnt1 +=1
    else:
      cnt2 +=1
      
  for i in range(cnt0):
    nums[i] = 0
  for i in range(cnt0,cnt0+cnt1):
    nums[i] = 1
  for i in range(cnt0+cnt1, cnt0+cnt1+cnt2):
    nums[i] = 2
  return nums

nums = [2, 0, 2, 1, 1, 0]
result = SortColors(nums)
print("After sorting:", result)
```

#### Optimal - DUTCH NATIONAL FLAG ALGORITHM
This algorithm contains 3 pointers i.e. low, mid, and high, and 3 main rules.  The rules are the following:
- arr[0….low-1] contains 0. [Extreme left part]
- arr[low….mid-1] contains 1.
- arr[high+1….n-1] contains 2. [Extreme right part], n = size of the array
- ![[Pasted image 20241210120422.png]]
- First, we will run a loop that will continue until mid <= high.
- There can be three different values of mid pointer i.e. arr[mid]
- If arr[mid] == 0, we will swap arr[low] and arr[mid] and will increment both low and mid. Now the subarray from index 0 to (low-1) only contains 0.
- If arr[mid] == 1, we will just increment the mid pointer and then the index (mid-1) will point to 1 as it should according to the rules.
- If arr[mid] == 2, we will swap arr[mid] and arr[high] and will decrement high. Now the subarray from index high+1 to (n-1) only contains 2.
- In this step, we will do nothing to the mid-pointer as even after swapping, the subarray from mid to high(after decrementing high) might be unsorted. So, we will check the value of mid again in the next iteration.
- Finally, our array should be sorted.

```python
def sortArray(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
  
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr
n = 6
arr = [0, 2, 1, 2, 0, 1]
result = sortArray(arr)
print("After sorting:",arr)
```

## 14. Majority Element
  #### better solution
  -  Approach that came to my mind
```python
#Time Complexity: O(N)
#Space Complexity: O(N)
def majorityElement(nums):
  dict1 = {}
  n = len(nums)
  for num in nums:
    if num in dict1:
      dict1[num] +=1
    else:
      dict1[num] = 1
  max_key = max(dict1, key=dict1.get)  
  if (dict1[max_key]) > n//2:
    return max_key
nums = [2,2,1,1,1,2,2]
output = majorityElement(nums)
print(output)
```

#### Optimal Moore Voting Algorithm
- if someone is coming more than n//2 times it will not get cancelled by other elements
```python
def majorityElement(nums):
  element = nums[0]
  count = 0
  n = len(nums)
  
  for i in range(n):
    if count == 0 :
      count =1
      element = nums[i]
    elif nums[i] == element:
      count+=1
    else:
      count-=1
  
  count1 = 0
  for i in range(n):
    if nums[i] == element:
      count1+=1
  if count1 > n//2:
    return element
  
nums = [2,2,1,1,1,2,2]
output = majorityElement(nums)
print(output)
```

```python
# TC - O(N)
# SC - O(1)
def majorityElement(nums):
    element = None
    count = 0
    for num in nums:
        if count == 0:
            element = num
        count += 1 if num == element else -1
    if nums.count(element) > len(nums) // 2:
        return element
    return None  
  
nums = [2, 2, 1, 1, 1, 2, 2]
output = majorityElement(nums)
print(output)  # Output: 2
```

## 15. Kadane's Algorithm or SubArray with Max Sum

#### brute
```python
# TC - O(N^3)
# SC - O(1)
  
def maxSubArray(nums):
  n = len(nums)
  maxi = -10**5
  for i in range(n):
    for j in range(i,n):
      sum_ = 0
      for k in range(i,j+1):
        sum_ += nums[k]
      maxi = max(maxi, sum_)  
  return maxi
  
nums = [-2,1,-3,4,-1,2,1,-5,4]
output = maxSubArray(nums)
print("sum of maximum subarray:",output)

```

#### Better Approach
```python
# TC - O(N^2)
# SC - O(1)
  
def maxSubArray(nums):
  n = len(nums)
  maxi = -10**5
  for i in range(n):
    sum_ = 0
    for j in range(i,n):
      sum_ += nums[j]
      maxi = max(maxi, sum_)  
  return maxi
  
nums = [-2,1,-3,4,-1,2,1,-5,4]
output = maxSubArray(nums)
print("sum of maximum subarray:",output)
```

#### Optimal Kadane Algorithm
```python
# TC - O(N)
# SC - O(1)
import sys
def maxSubArray(nums):
  maxi = -sys.maxsize-1
  sum_ = 0
  for i in range(len(nums)):
    sum_ += nums[i]
    if sum_ > maxi:
      maxi = sum_
    if sum_ < 0:
      sum_ = 0
  if maxi < 0: maxi = 0
  return maxi
  
nums = [-2,1,-3,4,-1,2,1,-5,4]
output = maxSubArray(nums)
print("sum of maximum subarray:",output)
```

follow up question also print the subarrays with maximum sum
```python
import sys
def maxSubArray(nums):
    maxi = -sys.maxsize - 1
    sum_ = 0
    start = 0
    ansStart, ansEnd = 0, 0
  
    for i in range(len(nums)):
        if sum_ == 0:
            start = i
        sum_ += nums[i]
        if sum_ > maxi:
            maxi = sum_
            ansStart = start
            ansEnd = i
        if sum_ < 0:
            sum_ = 0
  
    if maxi < 0:
        return 0
  
    print(f"The subarray is: {nums[ansStart:ansEnd+1]}")
    return maxi
  
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
output = maxSubArray(nums)
print("Sum of maximum subarray:", output)
```

## 16. Best time to Buy and Sell stocks

```python
def maxProfit(prices):
  min_price = float('inf')
  max_profit = 0
  
  for price in prices:
    if price < min_price:
      min_price = price
    elif price - min_price > max_profit:
      max_profit = price - min_price
  
  return max_profit
prices = [7,1,5,3,6,4]
output = maxProfit(prices)
print("profit of rs:",output)
```

## 17. rearrange the elements in the array
- brute force
```python
# TC - O(N+ N/2)
# SC - O(N)
def rearrangeArray(nums):
  n = len(nums)
  positive = []
  negative = []
  for num in nums:
    if num >= 0:
      positive.append(num)
    else:
      negative.append(num)
      
  for i in range(n//2):
    nums[2*i] = positive[i]
    nums[2*i +1 ] = negative[i]
  return nums
  
nums = [3,1,-2,-5,2,-4]
output = rearrangeArray(nums)
print(output)
```

#### Optimal
```python
# TC - O(N)
# SC - O(N)
def rearrangeArray(nums):
  n = len(nums)
  answer = [0]*n
  posIndx = 0
  negIndx = 1
  for i in range(n):
    if nums[i] < 0:
      answer[negIndx] = nums[i]
      negIndx +=2
    else:
      answer[posIndx] = nums[i]
      posIndx +=2
  return answer
nums = [3,1,-2,-5,2,-4]
output = rearrangeArray(nums)
print(output)
```

##### variety 2 : pos and neg are not equal
- isme brute force pe hi waps jana hai ....kyuki iska aur koi aacha solution nahi hai
```python
# TC - O(2n)
# SC - O(N)
def rearrangeArray(nums):
  n = len(nums)
  positive = []
  negative = []
  
  for i in range(n):
    if nums[i] >= 0:
      positive.append(nums[i])
    else:
      negative.append(nums[i])
      
  if len(positive) > len(negative):
    for i in range(len(negative)):
      nums[2*i] = positive[i]
      nums[2*i +1 ] = negative[i]
    index = len(negative)*2
    for i in range(len(negative),len(positive)):
      nums[index] = positive[i]
      index+=1
      
  else:
    for i in range(len(positive)):
      nums[2*i] = positive[i]
      nums[2*i +1 ] = negative[i]
    index = len(positive)*2
    for i in range(len(positive),len(negative)):
      nums[index] = negative[i]
      index+=1


  return nums
nums = [3,1,-2,-5,2,-4,-9,-9]
output = rearrangeArray(nums)
print(output)
```
## 18. Next Permutation

#### Brute
- generate all the permutatuion using recursion in sorted manner
- find the permutation next to the given permuatation
- TC - N! * N
- these cannot be practically possilbe because for an array size of 15 there are 10^12 combinations so these will take very long time
- just tell this to interviewer and skip on to better
#### Better
- can use inbuilt libraries like itertools and can use inbuilt function of this library
#### Best
- 1. longer prefix match same as og dictionary and find the breakpoint where arr[i] < arr[i+1]
- 2. take number which is just greater than that number : smallest big number
- 3. try to place the remaining in sorted in ascending order
```python
def nextPermutation(nums):
  """
  Do not return anything, modify nums in-place instead.
  """
  n = len(nums)
  index = -1
  for i in range(n - 2, -1, -1):
    if nums[i] < nums[i + 1]:
      index = i
      break
  if index == -1:
    nums.reverse()
    return
  for i in range(n - 1, index, -1):
    if nums[i] > nums[index]:
      nums[i], nums[index] = nums[index], nums[i]  
      break 
  nums[index + 1:] = reversed(nums[index + 1:])
  return nums
  
nums = [1,2,3]
output = nextPermutation(nums)
print(output)
```

## 19. Leaders in array
everything on the right should be smaller than the leader
#### Brute

```python
def leaders(nums):
  ans = []
  n = len(nums)
  for i in range(n):
    leader = True
    for j in range(i+1, n):
      if nums[j] > nums[i]:
        leader = False
        break
    if leader:
      ans.append(nums[i])
  return ans
  
nums = [16, 17, 4, 3, 5, 2]
output = leaders(nums)
print(output)
```
#### Optimal
- backtracking of array piche se aayenge and then check karenge uske right mai ki usse koi bada hai kya
```python
import sys
def leaders(nums):
    ans = []
    n = len(nums)
    maxi = -sys.maxsize - 1
    for i in range(n - 1, -1, -1):
      if nums[i] > maxi:
        ans.append(nums[i])
        maxi = nums[i]
    return ans
nums = [16, 17, 4, 3, 5, 2]
output = leaders(nums)
print(output)
```

