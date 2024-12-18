## key points
- always think of BS whenever the time complexity needed is O(logn)
- whenever you know the range for your answer
- also applicable to almost sorted arrays
- BS on answers is finding the answer in the specific range of answer
## 1. Binary Search
- TC - O($\log_2 n$)
- always used where the array is sorted
```python
## Iterative Code

def BinarySearch(nums,target):
  n= len(nums)
  low = 0
  high = n-1
  while low <= high:
    mid = low + ((high-low)//2)
    if nums[mid] == target:
      return mid
    elif nums[mid] < target:
      low = mid+1
    else:
      high = mid-1
  return -1

nums = [2,3,4,5,6,7,8,9,56]
target = 56
output = BinarySearch(nums,target)
print(f"your target element {target} is at index:",output)
```

## 1.1 Recursive Code of Binary Search

```python
def RecursiveBinarySearch(nums, low, high, target):
  if low <= high:
    mid = (low + high) // 2
    if nums[mid] == target:
      return mid  
    elif nums[mid] < target:
      return RecursiveBinarySearch(nums, mid + 1, high, target)  
    else:
      return RecursiveBinarySearch(nums, low, mid - 1, target)
  return -1
  
nums = [2, 3, 4, 5, 6, 7, 8, 9, 56]
target = 8
low = 0
high = len(nums) - 1
output = RecursiveBinarySearch(nums, low, high, target)
if output != -1:
    print(f"Your target element {target} is at index: {output}")
else:
    print(f"Your target element {target} is not in the list.")
```

## 2. Lower Bound

```python
def Lowerbound(nums,x,n):
  low = 0
  high = n-1
  ans = n
  while low <= high:
    mid = (low+high)//2
    if nums[mid] >= x:
      ans = mid
      high = mid -1
    else :
      low = mid+1
  return ans
  
nums = [2, 3, 7, 8, 8, 8, 9, 10, 56]
x = 8
n = len(nums)
output = Lowerbound(nums,x,n)
print(f"Your lowerbound for the el {x} is at index: {output} --> {nums[output]} ")
```

## 3. Upper Bound
```python
def upperbound(nums,x,n):
  low = 0
  high = n-1
  ans = n
  while low <= high:
    mid = (low+high)//2
    if nums[mid] > x:
      ans = mid
      high = mid -1
    else :
      low = mid+1
  return ans
  
nums = [2, 3, 4, 5, 6, 7, 8, 8, 8, 9, 56]
x = 8
n = len(nums)
output = upperbound(nums,x,n)
print(f"Your upperbound for the el {x} is at index:",output)
```
## 3.5. Pivot Element using Binary Search
```python
def search(nums):
    n = len(nums)
    low = 0
    high = n - 1
    if nums[low] < nums[high]:
        return 0    # Pivot is the first element
        
    while low <= high:
        mid = (low + high) // 2
        if mid < n - 1 and nums[mid] > nums[mid + 1]:
            return mid + 1  # Pivot found
        elif mid > 0 and nums[mid] < nums[mid - 1]:
            return mid  # Pivot found
            
        # Adjust the search range
        if nums[mid] >= nums[low]:
            low = mid + 1
        else:
            high = mid - 1
    return 0
  
nums = [6, 7, 8, 1, 2, 3, 4, 5]  
pivot = search(nums)
print(f"The pivot is at index: {pivot}")
```
## 4. Find First and Last element in sorted Array
```python
# lower bound
def Lowerbound(nums,target,n):
  low = 0
  high = n-1
  ans = n
  while low <= high:
    mid = (low+high)//2
    if nums[mid] >= target:
      ans = mid
      high = mid -1
    else :
      low = mid+1
  return ans

# upperbound
def upperbound(nums,target,n):
  low = 0
  high = n-1
  ans = n
  while low <= high:
    mid = (low+high)//2
    if nums[mid] > target:
      ans = mid
      high = mid -1
    else :
      low = mid+1
  return ans
  
def searchRange(nums, target):
  lb = Lowerbound(nums,target,n)
  if (lb == n or nums[lb]!= target):
    return [-1,-1]
  else:
    return [lb,upperbound(nums,target,n)]
nums = [5,7,7,8,8,10]
target = 8
n = len(nums)
output = searchRange(nums,target)
print(output)
```

## 5. Number of Occurences
```python
def Lowerbound(arr,target,n):
    low = 0
    high = n-1
    ans = n
    while low <= high:
        mid = (low+high)//2
        if arr[mid] >= target:
            ans = mid
            high = mid -1
        else :
            low = mid+1
    return ans
    
# upperbound
def upperbound(arr,target,n):
    low = 0
    high = n-1
    ans = n
    while low <= high:
        mid = (low+high)//2
        if arr[mid] > target:
            ans = mid
            high = mid -1
        else :
            low = mid+1
    return ans
    
class Solution:
    def countFreq(self, arr, target):
        #code here
        n = len(arr)
        lb = Lowerbound(arr,target,n)
        if (lb == n or arr[lb]!= target):
            return 0
        else:
            return upperbound(arr,target,n)-lb
```

## 6. Search in Rotated array
```python
def search(nums,target):
  n = len(nums)
  low = 0
  high = n -1
  while low <= high:
    mid = (low+high)//2
    if nums[mid] == target:
      return mid
    if nums[low] <= nums[mid]:
      if (nums[low] <= target and target <= nums[mid]):
        high = mid-1
      else:
        low = mid+1
    else:
      if nums[mid] <= target and target <= nums[high]:
        low = mid+1
      else:
        high = mid - 1
  return -1
```

## 7. Search In Sorted Array Part2 - repeated elements

```python
def search(nums,target):
  n = len(nums)
  low = 0
  high = n -1
  while low <= high:
    mid = (low+high)//2
    if nums[mid] == target:
      return True
      
    if nums[low] == nums[mid] and nums[mid] == nums[high]:
      low+=1
      high -=1
      continue
      
    # left sorted
    if nums[low] <= nums[mid]:
      if (nums[low] <= target and target <= nums[mid]):
        high = mid-1
      else:
        low = mid+1
        
    # right Sorted  
    else:
      if nums[mid] <= target and target <= nums[high]:
        low = mid+1
      else:
        high = mid - 1
  return False
```

## 8.  Single Element in a Sorted Array (540)

- You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
- Return the single element that appears only once.
- Your solution must run in O(log n) time and O(1) space.
`Example 1`:
- Input: nums = [1,1,2,3,3,4,4,8,8]
- Output: 2
`Example 2`:
- Input: nums = [3,3,7,7,10,11,11]
- Output: 10
```python
def SearchSingleElement(nums):
  n = len(nums)
  if n == 1:
      return nums[0]
  if nums[0] != nums[1]:
      return nums[0]
  if nums[n - 1] != nums[n - 2]:
      return nums[n - 1]
  low = 0
  high = n - 1
  while low <= high:
      mid = (low + high) // 2
      if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
          return nums[mid]
      if (mid % 2 == 1 and nums[mid] == nums[mid - 1]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1]):
          low = mid + 1
      else:
          high = mid - 1
  return -1
```

## 9. Find Peak Element(162)
- A peak element is an element that is strictly greater than its neighbors.
- Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
- You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
- You must write an algorithm that runs in O(log n) time.
`Example 1`:
- Input: nums = [1,2,3,1]
- Output: 2
- Explanation: 3 is a peak element and your function should return the index number 2.
`Example 2`:
- Input: nums = [1,2,1,3,5,6,4]
- Output: 5
- Explanation: Your function can return either index number 1 where the peak element is 2, or index number - where the peak element is 6.
```python
def FindPeakElement(nums):
  n = len(nums)
  if n == 1:
      return 0
  if nums[0] > nums[1]:
      return 0
  if nums[n - 1] > nums[n - 2]:
      return n - 1
  low = 1
  high = n - 2
  while low <= high:
      mid = (low + high) // 2
      if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
          return mid
      if nums[mid] < nums[mid + 1]:
          low = mid + 1
      else:
          high = mid - 1
  return -1
```

## 10. Find SquareRoot of N
```python
def SqaureRoot(n):
  ans = 0
  low = 0
  high = n//2
  while (low <= high):
    mid = (low+high)//2
    if mid * mid > n:
      high = mid -1
    else:
      ans = mid
      low = mid + 1
  return ans
SqaureRoot(5)
```

## 11. Find the nth root of m
```python
class Solution:
	def nthRoot(self, n: int, m: int) -> int:
		# Code here
		low = 1
        high = m
        while low <= high:
            mid = (low + high) // 2
            power = mid ** n
            if power == m:
                return mid  
            elif power < m:
                low = mid + 1 
            else:
                high = mid - 1  
        return -1 
```

## 12. Koko Eating Bananas ( 875 )
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.
`Example` 1:
- Input: piles = [3,6,7,11], h = 8
- Output: 4
`Example` 2:
- Input: piles = [30,11,23,4,20], h = 5
- Output: 30
`Example` 3:
- Input: piles = [30,11,23,4,20], h = 6
- Output: 23
```python
import math
def totalTime(nums,k):
  n = len(nums)
  hours = 0
  for num in nums:
    hours += math.ceil(num/k)
  return hours

def minEatingSpeed(nums,h):
  low = 1
  high = max(nums)
  ans = high
  while (low<=high):
    mid = (low+high)//2
    totalhours = totalTime(nums,mid)
    if totalhours <=h:
      ans = mid
      high = mid -1
    else:
      low = mid +1
  return ans
```
## 13. Minimum Number of Days to Make `m` Bouquets (1482 )
You are given an integer array `bloomDay`, an integer `m`, and an integer `k`.
You want to make `m` bouquets. To make a bouquet, you need to use `k` adjacent flowers from the garden.
The garden consists of `n` flowers, the \(i^{th}\) flower will bloom in the `bloomDay[i]` and then can be used in exactly one bouquet.
Return the minimum number of days you need to wait to be able to make `m` bouquets from the garden. If it is impossible to make `m` bouquets, return `-1`.

---
### Example 1
**Input**:
bloomDay = [1,10,3,10,2], m = 3, k = 1
**Output**: 3
**Explanation**:
Let us see what happened in the first three days. `x` means flower bloomed and `_` means flower did not bloom in the garden.
- We need 3 bouquets each should contain 1 flower.
- After day 1: `[x, _, _, _, _]` → we can only make one bouquet.
- After day 2: `[x, _, _, _, x]` → we can only make two bouquets.
- After day 3: `[x, _, x, _, x]` → we can make 3 bouquets.
The answer is **3**.  
---
### Example 2
**Input**: bloomDay = [1,10,3,10,2], m = 3, k = 2
**Output**: -1
**Explanation**:
We need 3 bouquets each having 2 flowers, which means we need 6 flowers. The garden only has 5 flowers, so it is impossible to get the needed bouquets. We return `-1`.

---
### Example 3

**Input**: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
**Output**: 12
**Explanation**:
We need 2 bouquets each should have 3 flowers.  
Here is the garden after the 7th and 12th days:
- After day 7: `[x, x, x, x, _, x, x]` → We can make one bouquet of the first three flowers that bloomed. We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent.
- After day 12: `[x, x, x, x, x, x, x]` → We can make two bouquets in different ways.
The answer is **12**.)
```python
from typing import List
def minDays( bloomDay, m, k):
    if m * k > len(bloomDay):
        return -1
    def canMakeBouquets(day):
        bouquets = 0
        flowers = 0
        for bloom in bloomDay:
            if bloom <= day:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0
        return bouquets >= m
        
    low, high = min(bloomDay), max(bloomDay)
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if canMakeBouquets(mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    return result
```
## 14. Find the Smallest Divisor Given a Threshold
Given an array of integers `nums` and an integer `threshold`, we will choose a positive integer divisor, divide all the array by it, and sum the division's result. Find the smallest divisor such that the result mentioned above is less than or equal to `threshold`.
Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: \( \lceil 7/3 \rceil = 3 \) and \( \lceil 10/2 \rceil = 5 \)).
The test cases are generated so that there will be an answer.
### Example 1
**Input**: nums = [1,2,5,9], threshold = 6  
**Output**: 5  
**Explanation**: We can get a sum to 17 (1+2+5+9) if the divisor is 1. If the divisor is 4, we can get a sum of 7 (1+1+2+3), and if the divisor is 5, the sum will be 5 (1+1+1+2).  
### Example 2
**Input**: nums = [44,22,33,11,1], threshold = 5  
**Output**: 44
```python
import math
def smallestDivisor( nums, threshold):
  def calculateSum(nums, divisor):
    sum_ = 0
    for number in nums:
      sum_ += math.ceil(number / divisor)
    return sum_
  
  low = 1
  high = max(nums)
  k = high
  
  while low <= high:
    mid = (low + high) // 2
    if calculateSum(nums, mid) <= threshold:
      k = mid  # Update the smallest valid divisor
      high = mid - 1
    else:
      low = mid + 1
  return k
```

## 15.  ( 1011 ) Capacity To Ship Packages Within D Days

A conveyor belt has packages that must be shipped from one port to another within `days` days.  
The `i`th package on the conveyor belt has a weight of `weights[i]`. Each day, we load the ship with packages on the conveyor belt (in the order given by `weights`). We may not load more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within `days` days.
### Example 1
**Input**:  
```
weights = [1,2,3,4,5,6,7,8,9,10], days = 5
```
**Output**:  15
**Explanation**:  
A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:  
1st day: 1, 2, 3, 4, 5  
2nd day: 6, 7  
3rd day: 8  
4th day: 9  
5th day: 10
Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

---
### Example 2
**Input**:  
```
weights = [3,2,2,4,1,4], days = 3
```

**Output**:  6
**Explanation**:  
A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:  
1st day: 3, 2  
2nd day: 2, 4  
3rd day: 1, 4

```python
from typing import List
class Solution:
  def shipWithinDays(self, weights: List[int], days: int) -> int:
    # Function to calculate the number of days needed for a given capacity
    # logic which is little bit difficult
    def calculateDays(weights, capacity):
      requiredDays = 1
      load = 0
      for weight in weights:
        if load + weight > capacity:
            requiredDays += 1
            load = weight
        else:
            load += weight
      return requiredDays
     # binary Search
    low = max(weights)
    high = sum(weights)
    ans = high
  
    while low <= high:
      mid = (low + high) // 2
      if calculateDays(weights, mid) <= days:
        ans = mid  
        high = mid - 1  
      else:
        low = mid + 1  
    return ans
```

## 16. Kth missing positive number

**Example 1:**
**Input:** arr = [2,3,4,7,11], k = 5
**Output:** 9
**Explanation:** The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
**Example 2:**
**Input:** arr = [1,2,3,4], k = 2
**Output:** 6
**Explanation:** The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
```python
# brute force that came to my mind
def findkthPositive(arr,k):
  missingArray = []
  for i in range(k+ len(arr)+1):
    if i not in arr:
      missingArray.append(i)
  return missingArray[k]
```

```python
# Brute force with time complexity as O(n)
def findkthPositive(arr,k):
  for i in range(len(arr)):
    if arr[i] <= k:
      k+=1
    else:
      break
  return k
```

```python
def findKthPositive(arr,k):
  n = len(arr)
  # binary Search Solution
  low = 0
  high = n-1
  while (low <= high):
    mid = (low + high)//2
    missing = (arr[mid] - (mid+1))
    if missing < k :
      low = mid +1
    else:
      high = mid -1
    # more = k - missing
    # missing = arr[high] - (high+1)
  return high + 1 + k # or low +k
```
# Binary search on Answers Type-2 Finding min(max) or max(min)
## 17. Aggressive Cows min dist between two cows should be maximum
```python
# linear Search TC - O(max-min)*O(n) + Nlogn == O(n^2) approx
def canWePlaceCows(arr,dist,cows):
  countCows = 1
  last = arr[0]
  for num in arr:
    if num - last >= dist:
      countCows+=1
      last = num
    if countCows >= cows:
      return True
    else:
      False

def CowsDistance(arr,cows):
  n = len(arr)
  arr = sorted(arr)
  for i in range(max(arr)-min(arr)):
    if canWePlaceCows(arr,i,cows) == True:
      continue
    else:
      return i -1
arr = [0,3,4,7,10]
cows = 4
CowsDistance(arr,cows)
```

`1`  `2`  `3`  4  5  6  7  8  9  10
- so here upto 3 is possible and uske bad it is not possible so we can use BS where a part of range is possible and a part of range is not possible
#### Bs TC - O(N * logN) + O(log base2 N) * logN
#### SC - O(1)
```python
def canWePlaceCows(arr,dist,cows):
  countCows = 1
  last = arr[0]
  for num in arr:
    if num - last >= dist:
      countCows+=1
      last = num
    if countCows >= cows:
      return True
    else:
      False
  
def CowsDistance(arr,cows):
  n = len(arr)
  arr = sorted(arr)
  low = 1
  high = max(arr)
  # ans = -1
  while (low <= high):
    mid = (low+high)//2
    if canWePlaceCows(arr,mid,cows) == True:
      # ans = mid
      low = mid+1
    else:
      high = mid -1
  return high
# ans ko store karne ki koi jarurat nahi hai ...opposite polarity
# low was on possible index and high was on not possible answer so after BS due to reverse polarity the high will end up at possible and low will end up at impossible
arr = [0,3,4,7,10]
cows = 4
CowsDistance(arr,cows)
```

## 18. Book Allocation Problem
#### Problem statement

Send feedback

Given an array _**‘arr’**_ of integer numbers, ‘arr[i]’ represents the number of pages in the ‘i-th’ book.
There are _**‘m’**_ number of students, and the task is to allocate all the books to the students.
Allocate books in such a way that:
```
1. Each student gets at least one book.
2. Each book should be allocated to only one student.
3. Book allocation should be in a contiguous manner.
```
You have to allocate the book to ‘m’ students such that the maximum number of pages assigned to a student is minimum.
If the allocation of books is not possible, return -1.
**Example:**

```
Input: ‘n’ = 4 ‘m’ = 2 
‘arr’ = [12, 34, 67, 90]

Output: 113

Explanation: All possible ways to allocate the ‘4’ books to '2' students are:

12 | 34, 67, 90 - the sum of all the pages of books allocated to student 1 is ‘12’, and student two is ‘34+ 67+ 90 = 191’, so the maximum is ‘max(12, 191)= 191’.

12, 34 | 67, 90 - the sum of all the pages of books allocated to student 1 is ‘12+ 34 = 46’, and student two is ‘67+ 90 = 157’, so the maximum is ‘max(46, 157)= 157’.

12, 34, 67 | 90 - the sum of all the pages of books allocated to student 1 is ‘12+ 34 +67 = 113’, and student two is ‘90’, so the maximum is ‘max(113, 90)= 113’.

We are getting the minimum in the last case.

Hence answer is ‘113’.
```
#### brute Force

```python
def countStudents(arr, pages):
    n = len(arr)  
    students = 1
    pagesStudent = 0
    for i in range(n):
        if pagesStudent + arr[i] <= pages:
            pagesStudent += arr[i]
        else:
            students += 1
            pagesStudent = arr[i]
    return students
    
def findPages(arr, n, m):
    if m > n:
        return -1
        
    low = max(arr)
    high = sum(arr)
    for pages in range(low, high + 1):
        if countStudents(arr, pages) == m:
            return pages
    return low
  
arr = [25, 46, 28, 49, 24]
n = 5
m = 4
ans = findPages(arr, n, m)
print("The answer is:", ans)
```

#### optimal
```python
def countStudents(arr, pages):
    n = len(arr)  
    students = 1
    pagesStudent = 0
    for i in range(n):
        if pagesStudent + arr[i] <= pages:
            pagesStudent += arr[i]
        else:
            students += 1
            pagesStudent = arr[i]
    return students
  
def findPages(arr, n, m):
    if m > n:
        return -1
  
    low = max(arr)
    high = sum(arr)
    while low <= high:
        mid = (low + high) // 2
        students = countStudents(arr, mid)
        if students > m:
            low = mid + 1
        else:
            high = mid - 1
    return low
  
arr = [25, 46, 28, 49, 24]
n = 5
m = 4
ans = findPages(arr, n, m)
print("The answer is:", ans)
```

## 19. Distance between two gas Stations
```python
```
## 20. Split Array Largest sum / Painter's Partition
Given an integer array `nums` and an integer `k`, split `nums` into `k` non-empty subarrays such that the largest sum of any subarray is **minimized**.
Return _the minimized largest sum of the split_.
A **subarray** is a contiguous part of the array.
**Example 1:**

**Input:** nums = [7,2,5,10,8], k = 2
**Output:** 18
**Explanation:** There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.

**Example 2:**

**Input:** nums = [1,2,3,4,5], k = 2
**Output:** 9
**Explanation:** There are four ways to split nums into two subarrays.
The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.

```python
from typing import List
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def calculateSum(nums, mid):
            subArray = 1
            numberSum = 0
            for num in nums:
                if numberSum + num <= mid:
                    numberSum += num
                else:
                    subArray += 1
                    numberSum = num
            return subArray
  
        low = max(nums)  
        high = sum(nums)  
  
        while low <= high:
            mid = (low + high) // 2
            if calculateSum(nums, mid) > k:
                low = mid + 1
            else:
                high = mid - 1
  
        return low
```
## 21. Median of two Sorted Array
#### Brute Force
`TC - O(n1+ n2)`
`SC - O(n1+n2)`
```python
from typing import List
class Solution:
  def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
      n1, n2 = len(nums1), len(nums2)
      nums = []
      i = 0
      j = 0
      while i < n1 and j < n2:
          if nums1[i] <= nums2[j]:
              nums.append(nums1[i])
              i += 1
          else:
              nums.append(nums2[j])
              j += 1
  
      while i < n1:
          nums.append(nums1[i])
          i += 1
  
      while j < n2:
          nums.append(nums2[j])
          j += 1
  
      n = n1 + n2
      if n % 2 == 1:  
          return nums[n // 2]
      else:
          return (nums[n // 2] + nums[n // 2 - 1]) / 2
```

#### Better 
```python  
def median(a, b):
    n1, n2 = len(a), len(b)
    n = n1 + n2  
    ind2 = n // 2
    ind1 = ind2 - 1
    cnt = 0
    ind1el, ind2el = -1, -1
  
    i, j = 0, 0
    while i < n1 and j < n2:
        if a[i] < b[j]:
            if cnt == ind1:
                ind1el = a[i]
            if cnt == ind2:
                ind2el = a[i]
            cnt += 1
            i += 1
        else:
            if cnt == ind1:
                ind1el = b[j]
            if cnt == ind2:
                ind2el = b[j]
            cnt += 1
            j += 1
  
    while i < n1:
        if cnt == ind1:
            ind1el = a[i]
        if cnt == ind2:
            ind2el = a[i]
        cnt += 1
        i += 1
    while j < n2:
        if cnt == ind1:
            ind1el = b[j]
        if cnt == ind2:
            ind2el = b[j]
        cnt += 1
        j += 1
  
    if n % 2 == 1:
        return float(ind2el)
  
    return float(ind1el + ind2el) / 2.0

  
a = [1, 4, 7, 10, 12]
b = [2, 3, 6, 15]
median(a,b)
print("The median of two sorted arrays is", "{:.1f}".format(median(a, b)))
```

#### Optimal
```python
def median(a, b):
    n1, n2 = len(a), len(b)
    if n1 > n2:
        return median(b, a)

    n = n1 + n2  # total length
    left = (n1 + n2 + 1) // 2  # length of left half
    # apply binary search:
    low, high = 0, n1
    while low <= high:
        mid1 = (low + high) // 2
        mid2 = left - mid1
        # calculate l1, l2, r1, and r2;
        l1, l2, r1, r2 = float('-inf'), float('-inf'), float('inf'), float('inf')
        if mid1 < n1:
            r1 = a[mid1]
        if mid2 < n2:
            r2 = b[mid2]
        if mid1 - 1 >= 0:
            l1 = a[mid1 - 1]
        if mid2 - 1 >= 0:
            l2 = b[mid2 - 1]
  
        if l1 <= r2 and l2 <= r1:
            if n % 2 == 1:
                return max(l1, l2)
            else:
                return (float(max(l1, l2)) + float(min(r1, r2))) / 2.0
  
        # eliminate the halves:
        elif l1 > r2:
            high = mid1 - 1
        else:
            low = mid1 + 1
    return 0  # dummy statemen  
a = [1, 4, 7, 10, 12]
b = [2, 3, 6, 15]
print("The median of two sorted arrays is {:.1f}".format(median(a, b)))
```

## 22. kth Element in Sorted Arrays 

```python
def kthElement(a, b, m, n, k):
    if m > n:
        return kthElement(b, a, n, m, k)
  
    left = k  # length of left half
  
    # apply binary search:
    low = max(0, k - n)
    high = min(k, m)
    while low <= high:
        mid1 = (low + high) // 2
        mid2 = left - mid1
        # calculate l1, l2, r1, and r2
        l1 = float('-inf')
        l2 = float('-inf')
        r1 = float('inf')
        r2 = float('inf')
        
        if mid1 < m:
            r1 = a[mid1]
        if mid2 < n:
            r2 = b[mid2]
        if mid1 - 1 >= 0:
            l1 = a[mid1 - 1]
        if mid2 - 1 >= 0:
            l2 = b[mid2 - 1]
        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)
  
        # eliminate the halves:
        elif l1 > r2:
            high = mid1 - 1
        else:
            low = mid1 + 1
  
    return 0  # dummy statement
a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
print("The k-th element of two sorted arrays is:", kthElement(a, b, len(a), len(b), 5))
```

## 23. Row with maximum 1's
#### brute
```python
def rowWithMax1s( arr):
  maxi = max(arr)
  n = len(arr)
  for i in range(n):
    if arr[i] == maxi:
      return i
arr = [[0,1,1,1], [0,0,1,1], [1,1,1,1], [0,0,0,0]]
rowWithMax1s(arr)
```

#### Optimal
```python  
def lowerBound(arr, n, x):
    low = 0
    high = n - 1
    ans = n
    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] >= x:
            ans = mid
            # look for smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right
    return ans
  
def rowWithMax1s(matrix, n, m):
    cnt_max = 0
    index = -1
  
    # traverse the rows:
    for i in range(n):
        # get the number of 1's:
        cnt_ones = m - lowerBound(matrix[i], m, 1)
        if cnt_ones > cnt_max:
            cnt_max = cnt_ones
            index = i
    return index
  
matrix = [[1, 1, 1], [0, 0, 1], [0, 0, 0]]
n = 3
m = 3
print("The row with maximum no. of 1's is:", rowWithMax1s(matrix, n, m))
```

## 24.  Find Peak Element

```python
from typing import List
def findMaxIndex(mat, n, m, col):
  maxValue = -1
  index = -1
  for i in range(n):
    if mat[i][col] > maxValue:
      maxValue = mat[i][col]
      index = i
  return index
  
def findPeakGrid(mat):
  n = len(mat)
  m = len(mat[0])
  low = 0
  high = m - 1
  while low <= high:
    mid = (low + high) // 2
    maxRowIndex = findMaxIndex(mat, n, m, mid)  
    
    left = mat[maxRowIndex][mid - 1] if mid > 0 else -1
    right = mat[maxRowIndex][mid + 1] if mid < m - 1 else -1

    if mat[maxRowIndex][mid] > left and mat[maxRowIndex][mid] > right:
        return [maxRowIndex, mid]
        
    elif mat[maxRowIndex][mid] < left:  
        high = mid - 1
        
    else:  
       low = mid + 1 
  return [-1, -1]
```

## 25 . Find Median of Matrix
TC - O(log(10^9)) X O(M(logN))

```python
def upperBound(arr, x, n):
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] > x:
            ans = mid
            # look for a smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right
    return ans

def countSmallEqual(matrix, m, n, x):
    cnt = 0
    for i in range(m):
        cnt += upperBound(matrix[i], x, n)
    return cnt
def median(matrix, m, n):
    low = float('inf')
    high = float('-inf')
    # point low and high to the right elements
    for i in range(m):
        low = min(low, matrix[i][0])
        high = max(high, matrix[i][n - 1])
    req = (n * m) // 2
    
    while low <= high:
        mid = (low + high) // 2
        smallEqual = countSmallEqual(matrix, m, n, mid)
        
        if smallEqual <= req:
            low = mid + 1
        else:
            high = mid - 1
    return low

  

if __name__ == "__main__":

    matrix = [

        [1, 2, 3, 4, 5],

        [8, 9, 11, 12, 13],

        [21, 23, 25, 27, 29]

    ]

    m = len(matrix)

    n = len(matrix[0])

    ans = median(matrix, m, n)

    print("The median element is:", ans)
```

## 26. Search In a 2D matrix
#### Brute TC - O(N) + O(logm)
```python
def searchMatrix(matrix,target):
  low = 0
  m = len(matrix[0])
  n = len(matrix)
  high = n*m - 1

  while (low <= high):
    mid = (low + high)//2
    row = mid // m
    col = mid % m
    if matrix[row][col] == target:
      return True
    elif matrix[row][col] < target:
      low = mid + 1
    else:
      high = mid - 1
  return False
```

#### Better TC - O(m+n)
```python
def searchElement(matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    row = 0
    col = m - 1
    # Traverse the matrix from (0, m-1):
    while row < n and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1
    return False

matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
result = searchElement(matrix, 8)
print(result)
```

