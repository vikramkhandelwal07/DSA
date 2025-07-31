## Question 1: Largest Element in an Array

### Problem Statement
Given an array of integers, find the **largest element** in the array.

---

### Approach

**English:**  
We iterate through the array and keep track of the largest element found so far.  
- Initialize `largest` with the first element of the array.  
- For each element `num` in the array:  
  - If `num > largest`, update `largest = num`.  
- After processing all elements, `largest` will hold the maximum value.

**Hinglish:**  
Hum array ko iterate karke ab tak ka sabse bada element track karte hain.  
- Pehle `largest` ko first element se initialize karte hain.  
- Array ke har `num` element ke liye:  
  - Agar `num > largest`, to `largest = num` kar dete hain.  
- Poore array ke baad `largest` me maximum value hoti hai.

---

### Example

**Input:**  
`numbers = [1, 2, 3, 4, 7, 9, 1]`  
**Output:**  
`9`

---

### Code
```python
def largestElement(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

numbers = [1, 2, 3, 4, 7, 9, 1]
x = largestElement(numbers)
print(x)  # Output: 9
```

---

## Question 2: Second Largest Element in an Array

### Problem Statement
Given an array of integers, find the **second largest element** in the array.

---

### Approach

**English:**  
We iterate through the array and keep track of the largest and second largest elements:  
- Initialize `largest` as the first element, and `secondLargest` as `-1`.  
- For each element in the array:  
  - If the current element is greater than `largest`,  
    then update `secondLargest = largest` and `largest = current element`.  
  - Else if the current element is between `largest` and `secondLargest`,  
    update `secondLargest = current element`.  
- Finally, `secondLargest` will hold the required value.  

**Hinglish:**  
Hum array me iterate karke `largest` aur `secondLargest` ko track karte hain:  
- Pehle `largest` ko pehle element se aur `secondLargest` ko `-1` se initialize karte hain.  
- Har element ke liye:  
  - Agar element `largest` se bada hai, to `secondLargest = largest` aur `largest = element`.  
  - Ya agar element `largest` se chhota lekin `secondLargest` se bada hai, to `secondLargest = element`.  
- Loop ke baad `secondLargest` answer hoga.

---

### Example

**Input:**  
`nums = [1, 9, 2, 8, 4, 7]`  
**Output:**  
`8`

---

### Code
```python
def Print2Largest(nums):
    largest = nums[0]
    secondLargest = -1
    for i in range(len(nums)):
        if nums[i] > largest:
            secondLargest = largest
            largest = nums[i]
        elif nums[i] > secondLargest and nums[i] < largest:
            secondLargest = nums[i]
    return secondLargest

nums = [1, 9, 2, 8, 4, 7]
x = Print2Largest(nums)
print(x)  # Output: 8
```

---

## Question 3: Rotate Array by `k` Steps (Left Rotation)

### Problem Statement
Given an array of integers, rotate the array to the left by `k` steps.

---

### Brute Force Approach

**English:**  
- Store the first `k` elements in a temporary array.  
- Shift the remaining `n-k` elements of the original array to the left by `k` places.  
- Copy the stored `k` elements back to the end of the array.

**Hinglish:**  
- Pehle `k` elements ko ek `temp` array me store karlo.  
- Bache hue elements ko `k` jagah left shift kardo.  
- Fir `temp` ke elements ko last me copy kardo.

---

### Code
```python
arr = [1, 2, 3, 4, 5, 6, 7]
d = 3
n = len(arr)

temp = arr[0:d]
for i in range(d, n):
    arr[i-d] = arr[i]

j = 0
for i in range(n-d, n):
    arr[i] = temp[j]
    j += 1

print(arr)  # Output: [4, 5, 6, 7, 1, 2, 3]
```

---

### Better Approach

**English:**  
Same logic as brute force but instead of creating a separate variable `j`, we calculate the index directly using `i - (n-d)`.

**Hinglish:**  
Brute force jaisa hi hai lekin ek extra variable `j` lene ki jagah index calculate kar lete hain: `i - (n-d)`.

---

### Code
```python
arr = [1, 2, 3, 4, 5, 6, 7]
d = 3
n = len(arr)

temp = arr[0:d]
for i in range(d, n):
    arr[i-d] = arr[i]

for i in range(n-d, n):
    arr[i] = temp[i-(n-d)]

print(arr)  # Output: [4, 5, 6, 7, 1, 2, 3]
```

---

### Best Approach (Reversal Algorithm)

**English:**  
We use **reversal algorithm**.  
- Reverse the entire array.  
- Reverse the first `k` elements.  
- Reverse the remaining `n-k` elements.

**Hinglish:**  
Hum **reversal algorithm** use karte hain:  
- Poora array reverse kardo.  
- Pehle `k` elements ko reverse kardo.  
- Fir bache hue `n-k` elements ko reverse kardo.

---

### Code
```python
from typing import List

def rotateArray(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    k %= n
    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])
    return nums

print(rotateArray([1, 2, 3, 4, 5, 6, 7], 3))  # Output: [4, 5, 6, 7, 1, 2, 3]
```

---

## Question 4: Move Zeroes to End

### Problem Statement
Given an array, move all the `0`s to the end of the array while maintaining the relative order of the non-zero elements.  
Do this **in-place** without making a copy of the array.

---

### Approach

**English:**  
We use a **two-pointer technique**.  
- One pointer `j` is used to mark the position of the first zero in the array.  
- Iterate through the array with another pointer `i`, starting just after `j`.  
- Whenever we find a non-zero element at `i`, swap it with the zero at `j`, and increment `j`.  
- Continue until the end of the array.  

**Hinglish:**  
Hum **two-pointer approach** use karte hain.  
- Ek pointer `j` ko pehli `0` ke position par set karte hain.  
- Fir ek aur pointer `i` se array ko traverse karte hain.  
- Jab bhi `i` par non-zero mile, to usko `j` par rakhe `0` se swap karte hain aur `j++` kar dete hain.  
- Ye tab tak karte hain jab tak array khatam na ho jaye.

---

### Example

**Input:**  
`nums = [1, 0, 1, 0, 3, 12]`  
**Output:**  
`[1, 1, 3, 12, 0, 0]`

---

### Code
```python
def moveZeroes(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    j = -1
    for i in range(len(nums)):
        if nums[i] == 0:
            j = i
            break
    for i in range(j+1, len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
    return nums

nums = [1, 0, 1, 0, 3, 12]
res = moveZeroes(nums)
print(res)  # Output: [1, 1, 3, 12, 0, 0]
```

---

## Question 5: Missing Number in Range [0…n]

### Problem Statement
You’re given an array `nums` of length `n`, containing unique numbers from the range `0` to `n` (inclusive), with exactly one number missing.  
Find the missing number.

---

### Approach 1 — Brute Force

**Idea:**  
For every number `i` from `0` to `n`, check if `i` is **not in** `nums`. Return that number.

- **Time Complexity:** O(n²)  
- **Space Complexity:** O(1)

---

### Code
```python
def missingNumber(nums):
    n = len(nums)
    for i in range(n+1):
        if i not in nums:
            return i

nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
ans = missingNumber(nums)
print(ans)  # Output: 8
```

---

### Approach 2 — Optimal (Sum Formula)

**Idea:**  
We know the sum of first `n` natural numbers:  
\[
\text{Sum} = \frac{n(n+1)}{2}
\]  
Subtract the sum of elements of `nums` from it. The difference is the missing number.

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)

---

### Code
```python
def missingNumber(nums):
    n = len(nums)
    total = (n * (n+1)) // 2
    return total - sum(nums)

nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
ans = missingNumber(nums)
print(ans)  # Output: 8
```

---

## Question 6: Maximum Consecutive 1’s

### Problem Statement
Given a binary array `nums`, find the maximum number of consecutive `1`s.

---

### Approach 1 — Using Auxiliary List

**Idea:**  
Traverse `nums`, count consecutive `1`s and append counts to a list `arr`. At the end, return `max(arr)`.

- **Time Complexity:** O(n)  
- **Space Complexity:** O(n)

---

### Code
```python
def consecutiveOnes(nums):
    arr = []
    count = 0
    for num in nums:
        if num == 1:
            count += 1
        else:
            arr.append(count)
            count = 0
    arr.append(count)
    return max(arr)

nums = [1, 1, 0, 1, 1, 1]
print(consecutiveOnes(nums))  # Output: 3
```

---

### Approach 2 — Optimal

**Idea:**  
Instead of maintaining a list, keep a `maxi` variable to store the maximum count found so far while traversing.

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)

---

### Code
```python
def consecutiveOnes(nums):
    maxi = 0
    count = 0
    for num in nums:
        if num == 1:
            count += 1
            maxi = max(maxi, count)
        else:
            count = 0
    return maxi

nums = [1, 1, 0, 1, 1, 1, 0]
print(consecutiveOnes(nums))  # Output: 3
```
---


## Question 7: Single Number (XOR)

### Problem Statement
Given an integer array `nums` where every element appears **twice except for one**, find that single one.

---

### Approach — XOR  
**Idea:**  
- XOR of a number with itself is `0` → `a ^ a = 0`  
- XOR of a number with `0` is the number itself → `a ^ 0 = a`  
- So, XOR all elements. The duplicates cancel out and leave the unique number.

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(1)`

---

### Code
```python
def singleNumber(nums: List[int]) -> int:
    xor1 = 0
    for num in nums:
        xor1 ^= num
    return xor1

nums = [2, 3, 4, 5, 4, 3, 5]
result = singleNumber(nums)
print(result)  # Output: 2
```

---

## Question 8: Longest Subarray with Sum K

### Problem Statement
Given an array of integers and a target sum `k`, find the **length of the longest subarray** whose sum is equal to `k`.

---

### Approach

**English:**  
We want to find the subarray (continuous part of the array) that adds up to `k` and has the **maximum length**.

We solve it in two ways:
- **Brute Force**: Check all subarrays and their sums.
- **Optimal (Sliding Window)**: Use two pointers (`left`, `right`) to manage a window that adjusts based on the sum.

**Hinglish:**  
Humein ek aise subarray ki length chahiye jo `k` ke barabar ho aur sabse lamba ho.  
Do tarike se solve karte hain:
- **Brute Force**: Har subarray ka sum check karte hain.
- **Optimal (Sliding Window)**: Ek window maintain karte hain aur sum ke hisaab se `left` aur `right` pointers move karte hain.

---

### Example

**Input:**  
`arr = [10, 5, 2, 7, 1, 9]`  
`k = 15`

**Output:**  
`4`  

**Explanation:**  
`[5, 2, 7, 1]` is the longest subarray with sum 15.

---

### 🔹 Brute Force Approach

#### Code
```python
def longestSubArray(nums, k):
    n = len(nums)
    length = 0
    for i in range(n):
        for j in range(i, n):
            s = 0
            for x in range(i, j + 1):
                s += nums[x]
            if s == k:
                length = max(length, j - i + 1)
    return length
```

**Time Complexity:** `O(n³)` — Three nested loops  
**Space Complexity:** `O(1)` — No extra space used

---

### 🔹 Optimal Approach (Sliding Window)

#### Code
```python
def longestSubarray3(nums, k):
    left = 0
    right = 0
    n = len(nums)
    Sum = nums[0]
    maxLength = 0

    while right < n:
        while left <= right and Sum > k:
            Sum -= nums[left]
            left += 1

        if Sum == k:
            maxLength = max(maxLength, right - left + 1)

        right += 1
        if right < n:
            Sum += nums[right]

    return maxLength
```

**Time Complexity:** `O(n)` — Each element is visited at most twice  
**Space Complexity:** `O(1)` — No extra space used

---


## Question 9: Two Sum

### Problem Statement
Given an array of integers `nums` and an integer `target`, return the indices of the **two numbers** such that they add up to `target`.  
You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

---

### Approach

**English:**  
We need to find two numbers in the array whose sum is equal to the given target.  
We can solve this problem using:
- **Brute Force**: Try every pair.
- **Better**: Use a HashMap to store seen elements and their indices.
- **Optimal**: Sort and use two pointers (if index tracking not required).

**Hinglish:**  
Humein array ke do elements dhoondhne hain jinka sum target ke barabar ho.  
Teen tarike se solve kar sakte hain:
- **Brute Force**: Har possible pair try karo.
- **Better**: Ek hashmap rakho jisme dekha ki kaunsa number pehle aaya tha.
- **Optimal**: Array ko sort karke two pointer se answer dhoondho (agar index chahiye nahi to).

---

### Example  
**Input:**  
`nums = [2, 7, 11, 15]`  
`target = 9`  

**Output:**  
`[0, 1]`  
**Explanation:** `nums[0] + nums[1] = 2 + 7 = 9`

---

### Brute Force Approach

#### Code
```python
def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
```

#### Time Complexity  
O(n²) — All pairs are checked.

#### Space Complexity  
O(1) — No extra space used.

---

### Better Approach (Using Hash Map)

#### Code
```python
def twoSum(nums, target):
    hashMap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashMap:
            return [hashMap[complement], i]
        hashMap[num] = i
```

#### Time Complexity  
O(n) — One pass through the array.

#### Space Complexity  
O(n) — Extra space for hashmap.

---

### Optimal Approach (Two Pointers – Only if sorted and index not required)

#### Code
```python
def twoSum(nums, target):
    nums = sorted(nums)
    left = 0
    right = len(nums) - 1
    while left < right:
        currentSum = nums[left] + nums[right]
        if currentSum == target:
            return [left, right]
        elif currentSum < target:
            left += 1
        else:
            right -= 1
```

**Note:** This approach works only if original indices are not needed (or if indices are tracked before sorting).

#### Time Complexity  
O(n log n) — Due to sorting

#### Space Complexity  
O(1) — No extra space used (excluding sort)

---

## Question 10: Sort Colors (Dutch National Flag Problem)

### Problem Statement  
Given an array `nums` with `n` objects colored red (0), white (1), or blue (2), sort them **in-place** so that objects of the same color are adjacent, with the colors in the order **0, 1, 2**.

---

### Approach

**English:**  
We need to sort an array that only contains 0s, 1s, and 2s.  
There are two main approaches:
- **Counting Method**: Count occurrences of 0, 1, and 2 and then overwrite the array.
- **Dutch National Flag Algorithm**: Use three pointers (`low`, `mid`, `high`) and swap elements accordingly.

**Hinglish:**  
Array me sirf 0, 1 aur 2 hote hain. Inhe ascending order me inplace sort karna hai.  
Do tarike se kar sakte hain:
- **Counting Method**: 0, 1, 2 kitni baar aaye woh count karo, fir array overwrite karo.
- **Dutch Flag Algorithm**: Teen pointer `low`, `mid`, `high` se inplace swap karke sort karte hain.

---

### Example  
**Input:**  
`nums = [2, 0, 2, 1, 1, 0]`  

**Output:**  
`[0, 0, 1, 1, 2, 2]`

---

### Brute Force (Counting Sort Style)

#### Code
```python
def SortColors(nums):
    cnt1 = 0
    cnt2 = 0
    cnt0 = 0 
    for i in range(len(nums)):
        if nums[i] == 0:
            cnt0 += 1
        elif nums[i] == 1:
            cnt1 += 1
        else:
            cnt2 += 1

    for i in range(cnt0):
        nums[i] = 0
    for i in range(cnt0, cnt0 + cnt1):
        nums[i] = 1
    for i in range(cnt0 + cnt1, cnt0 + cnt1 + cnt2):
        nums[i] = 2

    return nums

# Example
nums = [2, 0, 2, 1, 1, 0]
result = SortColors(nums)
print("After sorting:", result)
```

#### Time Complexity  
O(2N) — One pass to count, one to overwrite

#### Space Complexity  
O(1) — No extra space used

---

### Optimal Approach (Dutch National Flag Algorithm)

#### Code
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

# Example
arr = [0, 2, 1, 2, 0, 1]
result = sortArray(arr)
print("After sorting:", result)
```

#### Time Complexity  
O(N) — Single pass through array

#### Space Complexity  
O(1) — In-place sorting, no extra space

---


## Question 11. Majority Element

### ❓ Problem Statement  
Given an array `nums` of size `n`, find the **majority element** — the element that appears more than `n // 2` times.  
You may assume that the majority element always exists in the array.

---

### ✅ Approach

**English:**  
We want to find the element that appears **more than half the times** in the array.  
We use the **Boyer-Moore Voting Algorithm**, which works in two steps:
1. First pass to **find a candidate**.
2. Second pass to **verify** if it is truly the majority.

**Hinglish:**  
Humein woh element dhoondhna hai jo array me `n//2` se zyada baar aaya ho.  
Iske liye Boyer-Moore algorithm use karte hain:
1. Pehle ek **candidate** find karte hain.
2. Fir check karte hain ki woh actual majority hai ya nahi.

---

### 💡 Example  
**Input:**  
`nums = [2, 2, 1, 1, 1, 2, 2]`  
**Output:**  
`2`  
Explanation: `2` appears 4 times in a list of size 7.

---

### 🔹 Boyer-Moore Voting Algorithm (with explicit verification)

```python
def majorityElement(nums):
    element = nums[0]
    count = 0
    n = len(nums)

    for i in range(n):
        if count == 0:
            count = 1
            element = nums[i]
        elif nums[i] == element:
            count += 1
        else:
            count -= 1

    count1 = 0
    for i in range(n):
        if nums[i] == element:
            count1 += 1

    if count1 > n // 2:
        return element
```

**Time Complexity:** O(N)  
**Space Complexity:** O(1)

---

### 🔹 Optimized Boyer-Moore (Pythonic count)

```python
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
```

**Time Complexity:** O(N)  
**Space Complexity:** O(1)

---

## Question 12. Maximum Subarray Sum (Kadane’s Algorithm)

### ❓ Problem Statement  
Given an integer array `nums`, find the **contiguous subarray** (containing at least one number) which has the **largest sum**, and return its sum.

---

### ✅ Approach

**English:**  
We want to find a subarray (continuous elements) that gives the **maximum sum**.  
There are 3 common approaches:
- **Brute Force**: Try all possible subarrays and calculate their sums.
- **Better**: Improve by removing the innermost loop and maintaining a running sum.
- **Optimal (Kadane’s Algorithm)**: Traverse once while tracking current and max sum.

**Hinglish:**  
Humein ek subarray (lagataar elements) chahiye jiska sum sabse zyada ho.  
3 approaches use karte hain:
- **Brute Force**: Sabhi subarrays ka sum calculate karte hain.
- **Better**: Ek level optimize karke inner loop hatate hain.
- **Optimal (Kadane)**: Ek pass me answer milta hai.

---

### 💡 Example  
**Input:**  
`nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`  
**Output:**  
`6`  
Explanation: `[4, -1, 2, 1]` has the maximum sum = 6.

---

### 🔹 Brute Force Approach

```python
def maxSubArray(nums):
    n = len(nums)
    maxi = -10**5
    for i in range(n):
        for j in range(i, n):
            sum_ = 0
            for k in range(i, j + 1):
                sum_ += nums[k]
            maxi = max(maxi, sum_)  
    return maxi

# Example
nums = [-2,1,-3,4,-1,2,1,-5,4]
print("Sum of maximum subarray:", maxSubArray(nums))
```

**Time Complexity:** O(n³)  
**Space Complexity:** O(1)

---

### 🔹 Better Approach (Remove inner loop)

```python
def maxSubArray(nums):
    n = len(nums)
    maxi = -10**5
    for i in range(n):
        sum_ = 0
        for j in range(i, n):
            sum_ += nums[j]
            maxi = max(maxi, sum_)  
    return maxi

# Example
nums = [-2,1,-3,4,-1,2,1,-5,4]
print("Sum of maximum subarray:", maxSubArray(nums))
```

**Time Complexity:** O(n²)  
**Space Complexity:** O(1)

---

### 🔹 Optimal Approach (Kadane's Algorithm)

```python
import sys
def maxSubArray(nums):
    maxi = -sys.maxsize - 1
    sum_ = 0
    for i in range(len(nums)):
        sum_ += nums[i]
        if sum_ > maxi:
            maxi = sum_
        if sum_ < 0:
            sum_ = 0
    return maxi

# Example
nums = [-2,1,-3,4,-1,2,1,-5,4]
print("Sum of maximum subarray:", maxSubArray(nums))
```

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

---

### 🔹 Kadane's Algorithm with Subarray Print

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

# Example
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Sum of maximum subarray:", maxSubArray(nums))
```

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

---


## Question 13: Best Time to Buy and Sell Stock

### Problem Statement  
You are given an array `prices` where `prices[i]` is the price of a stock on the `i`-th day.  
You want to **buy one stock** on one day and **sell it on another day in the future** to earn the **maximum profit**.  
Return the **maximum profit** you can achieve from this transaction.  
If you cannot achieve any profit, return `0`.

---

### Approach

**English:**  
Keep track of the **minimum price** so far. For each price:
- Update `min_price` if the current price is lower.
- Calculate `price - min_price` and update `max_profit` if it's higher than before.

**Hinglish:**  
Minimum price track karte jao. Har din ka price ke saath:
- Agar naya price kam hai to `min_price` update karo.
- Fir `price - min_price` ka profit calculate karo aur `max_profit` update karo.

---

### Code (Optimal Approach — Single Pass)
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

# Example
prices = [7, 1, 5, 3, 6, 4]
output = maxProfit(prices)
print("Profit of Rs:", output)
```

### Time and Space Complexity  
- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)

---

## Question 14: Rearrange Array Elements by Sign

### Problem Statement  
Given an array `nums` consisting of **equal number of positive and negative integers** or **more of one type**, rearrange the elements so that:
- Elements at **even indices** are **positive**
- Elements at **odd indices** are **negative**
- Extra elements (if present) go at the end

---

### Approach 1: Optimal (Using Two Pointers)

**English:**  
Use two pointers:  
- `posIndx` for even indices  
- `negIndx` for odd indices  
Fill accordingly.

**Hinglish:**  
- `posIndx` pe positive numbers daalo  
- `negIndx` pe negative numbers daalo  
- Dono ko +2 se update karo

```python
def rearrangeArray(nums):
    n = len(nums)
    answer = [0]*n
    posIndx = 0
    negIndx = 1
    for i in range(n):
        if nums[i] < 0:
            answer[negIndx] = nums[i]
            negIndx += 2
        else:
            answer[posIndx] = nums[i]
            posIndx += 2
    return answer

nums = [3, 1, -2, -5, 2, -4]
output = rearrangeArray(nums)
print(output)
```

---

### Approach 2: Brute Force

**English:**  
- Split array into `positive[]` and `negative[]`.
- Alternate merge them.
- Add leftovers at the end if any.

**Hinglish:**  
- Positive aur negative numbers ko alag list me store karo.
- Fir alternate jagah par fill karo.

```python
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
            nums[2*i + 1] = negative[i]
        index = len(negative)*2
        for i in range(len(negative), len(positive)):
            nums[index] = positive[i]
            index += 1
    else:
        for i in range(len(positive)):
            nums[2*i] = positive[i]
            nums[2*i + 1] = negative[i]
        index = len(positive)*2
        for i in range(len(positive), len(negative)):
            nums[index] = negative[i]
            index += 1
            
    return nums

nums = [3, 1, -2, -5, 2, -4, -9, -9]
output = rearrangeArray(nums)
print(output)
```

---

### Time and Space Complexity

| Approach        | Time Complexity | Space Complexity |
|----------------|------------------|-------------------|
| Optimal         | O(N)             | O(N)              |
| Brute Force     | O(2N)            | O(N)              |

---

## Question 15: Next Permutation

### Problem Statement  
Given an array of integers `nums`, rearrange them into the **next lexicographically greater permutation**.  
If such arrangement is not possible, return the **lowest possible order** (sorted in ascending order).  
**Do it in-place**.

---

### Approach (Rightmost Breakpoint + Reverse Suffix)

```python
def nextPermutation(nums):
    n = len(nums)
    index = -1

    # Step 1: Find the break point
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            index = i
            break

    # If no break point, reverse the entire array
    if index == -1:
        nums.reverse()
        return

    # Step 2: Swap with next greater element from right
    for i in range(n - 1, index, -1):
        if nums[i] > nums[index]:
            nums[i], nums[index] = nums[index], nums[i]
            break

    # Step 3: Reverse suffix
    nums[index + 1:] = reversed(nums[index + 1:])
    return nums

nums = [1, 2, 3]
nextPermutation(nums)
print(nums)  # Output: [1, 3, 2]
```

### Time and Space Complexity  
- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)

---


## Question 16: Leaders in an Array

### 🔶 Problem Statement  
Given an array `nums[]` of size `n`, find all the **leaders** in the array.  
An element is a **leader** if it is **strictly greater than all elements to its right**.  
The rightmost element is always considered a leader.

---

### 🟡 Brute Force Approach (Nested Loops)

#### 💡 Intuition (English)  
- For every element, check all elements to its right.  
- If none are greater, it is a leader.

#### 💭 Hinglish  
- Har element ke liye uske right ke sabhi elements check karo.  
- Agar koi bhi usse bada nahi nikla to wo leader hai.

#### ✅ Code
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
print(output)  # Output: [17, 5, 2]
```

---

### ✅ Optimal Approach (Right to Left)

#### 💡 Intuition (English)  
- Start from the last element and keep track of the maximum seen so far.  
- If current element is greater than the max so far, it’s a leader.

#### 💭 Hinglish  
- Array ko reverse me traverse karo.  
- Har element ke liye check karo ki kya ye ab tak ka sabse bada hai.  
- Agar haan, to leader hai.

#### ✅ Code
```python
import sys

def leaders(nums): 
    n = len(nums)
    ans = []
    maxi = -sys.maxsize - 1
    for i in range(n-1, -1, -1):
        if nums[i] > maxi:
            ans.append(nums[i])
            maxi = nums[i]
    return ans

arr = [10, 22, 12, 3, 0, 6]
output = leaders(arr)
print(output)  # Output: [6, 12, 22]
```

---

### ⏱️ Time and Space Complexity

| Approach        | Time Complexity | Space Complexity |
|----------------|------------------|------------------|
| Brute Force     | O(N²)            | O(1)             |
| Optimal         | O(N)             | O(N)             |

---

## Question 17: Longest Consecutive Sequence

###  Problem Statement  
Given an **unsorted array of integers**, return the length of the **longest consecutive elements sequence**.  

> A consecutive sequence means numbers that follow each other with a difference of 1 (in any order).

 **Example**  
Input: `[100, 4, 200, 1, 3, 2, 2, 3, 3, 4]`  
Output: `4`  
Explanation: Longest consecutive sequence is `[1, 2, 3, 4]`

---

###  Optimal Approach (Using HashSet)

####  Intuition (English)  
- Use a set for O(1) lookup of elements.  
- For each number, check if it's the **start of a sequence** (i.e., `num - 1` is not present).  
- If it is, keep incrementing and counting until the next number is not found.

#### Hinglish  
- Sab numbers ko set me daal do (fast lookup ke liye).  
- Har number check karo kya wo sequence ka starting point hai (`num-1` set me nahi hona chahiye).  
- Agar haan, to `num+1`, `num+2`, ... check karte jao jab tak sequence chalti rahe.

---

#### Code
```python
def longestSuccessiveElements(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest = max(longest, current_streak)

    return longest

nums = [100, 4, 200, 1, 3, 2, 2, 3, 3, 4]
output = longestSuccessiveElements(nums)
print(output)  # Output: 4
```

---

###  Time and Space Complexity

| Metric            | Value |
|-------------------|--------|
| Time Complexity   | O(N)   |
| Space Complexity  | O(N)   |

>  **Note:** Brute force would be O(N²) by checking every possible sequence.  
> Using HashSet reduces it to linear time.

---

## Question 18: Set Matrix Zero

### Problem Statement  
Given an `n x m` matrix, if any element is 0, set its entire row and column to 0 in-place.

---

### Approach 1: Brute Force (Using -1 as Marker)  

**Time Complexity:** O(N × M × (N + M))  
**Space Complexity:** O(1) (Using in-place markers)

```python
def markRow(matrix, n, m, i):
    for j in range(m):
        if matrix[i][j] != 0:
            matrix[i][j] = -1

def markCol(matrix, n, m, j):
    for i in range(n):
        if matrix[i][j] != 0:
            matrix[i][j] = -1

def setZeros(matrix, n, m):
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                markRow(matrix, n, m, i)
                markCol(matrix, n, m, j)

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == -1:
                matrix[i][j] = 0
    return matrix

matrix = [[1,1,1],[1,0,1],[1,1,1]]
n = len(matrix)
m = len(matrix[0])
output = setZeros(matrix, n, m)
print(output)
```

---

### Approach 2: Better (Using Row and Column Arrays)  

**Time Complexity:** O(N × M)  
**Space Complexity:** O(N + M)

```python
def ZeroMatrix(matrix, n, m):
    row = [0] * n
    col = [0] * m
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                row[i] = 1
                col[j] = 1

    for i in range(n):
        for j in range(m):
            if row[i] or col[j]:
                matrix[i][j] = 0
    return matrix

matrix = [[0,1,2,0],[3,4,5,2],[1,3,0,5]]
n = len(matrix)
m = len(matrix[0])
output = ZeroMatrix(matrix, n, m)
print(output)
```

---

### Approach 3: Optimal (In-place Using First Row and Column)  

**Time Complexity:** O(N × M)  
**Space Complexity:** O(1)

```python
def zeroMatrix(matrix, n, m):
    col0 = 1

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                if j != 0:
                    matrix[0][j] = 0
                else:
                    col0 = 0

    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if matrix[0][0] == 0:
        for j in range(m):
            matrix[0][j] = 0
    if col0 == 0:
        for i in range(n):
            matrix[i][0] = 0

    return matrix

matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
n = len(matrix)
m = len(matrix[0])
ans = zeroMatrix(matrix, n, m)
print("The Final matrix is:")
for row in ans:
    for ele in row:
        print(ele, end=" ")
    print()
```

---

## Question 19: Rotate Image 90° Clockwise

### Problem Statement  
You are given an `n x n` 2D matrix representing an image. Rotate the image in-place **by 90 degrees clockwise**.

---

### Approach 1: Brute Force (Using Extra Matrix)  

**Time Complexity:** O(N²)  
**Space Complexity:** O(N²)

```python
def rotate(matrix):
    n = len(matrix)
    rotated = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            rotated[j][n-1-i] = matrix[i][j]
    
    for i in range(n):
        for j in range(n):
            matrix[i][j] = rotated[i][j]
    
    return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
output = rotate(matrix)
print(output)
```

---

### Approach 2: Optimal (Transpose + Reverse Rows)  

**Time Complexity:** O(N²)  
**Space Complexity:** O(1)

```python
def rotate(matrix):
    n = len(matrix)
    
    for i in range(n-1):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(n):
        matrix[i].reverse()
    
    return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
output = rotate(matrix)
print(output)
```

---

### Explanation

#### Step 1: Transpose the Matrix

Before Transpose:  
```
1 2 3  
4 5 6  
7 8 9
```

After Transpose:  
```
1 4 7  
2 5 8  
3 6 9
```

#### Step 2: Reverse Each Row  

Final Rotated Matrix:  
```
7 4 1  
8 5 2  
9 6 3
```

This rotates the matrix 90° clockwise **in-place** with no extra space.

---

## Question 20: Spiral Matrix Traversal

Given an `m x n` matrix, return all elements of the matrix in **spiral order**.

---

### Approach: Boundary Pointers (Optimal)

Use four pointers — `top`, `bottom`, `left`, `right` — to control the traversal of the matrix in layers (like peeling an onion).

- Traverse **left to right** (→) on the top row  
- Traverse **top to bottom** (↓) on the right column  
- Traverse **right to left** (←) on the bottom row  
- Traverse **bottom to top** (↑) on the left column  

Update the boundaries after each direction.

**Time Complexity:** O(m × n)  
**Space Complexity:** O(1) (excluding the output list)

---

### Code

```python
def spiralOrder(matrix):
    n = len(matrix)
    m = len(matrix[0])
    left, right, top, bottom = 0, m - 1, 0, n - 1
    answer = []
    
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            answer.append(matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            answer.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                answer.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                answer.append(matrix[i][left])
            left += 1

    return answer

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
output = spiralOrder(matrix)
print(output)
```

---

### Example

**Input:**
```python
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
```

**Output:**
```
[1, 2, 3, 6, 9, 8, 7, 4, 5]
```

---

### Notes

- Always check the boundary conditions (`top <= bottom` and `left <= right`) to avoid duplicate traversals.
- The loop stops when we’ve completely traversed the matrix from all four directions.

---

## Question 21: Count Subarrays with Sum = K

Given an array `nums` and an integer `k`, return the **total number of continuous subarrays** whose sum equals to `k`.

---

### Approach: Prefix Sum with Hash Map (Optimal)

Maintain a running prefix sum (`preSum`) and store its frequency in a hashmap. For every element:

- Compute `preSum += nums[i]`  
- Check if `preSum - k` exists in the map  
  - If yes, that means there exists a subarray ending at index `i` with sum = `k`  
- Update the hashmap with the current `preSum`

This avoids nested loops and ensures **O(n)** time.

---

### Code

```python
def noOfSubArray(nums, k):
    n = len(nums)
    dict1 = {0: 1}
    preSum = 0
    count = 0
    
    for i in range(n):
        preSum += nums[i]
        rem = preSum - k

        if rem in dict1:
            count += dict1[rem]
        
        if preSum in dict1:
            dict1[preSum] += 1
        else:
            dict1[preSum] = 1
            
    return count
```

---

### Time & Space Complexity

- **Time Complexity:** O(n)  
- **Space Complexity:** O(n)

---

### Example

**Input:**
```python
nums = [1, 2, 3]
k = 3
```

**Output:**
```
2
```

**Explanation:**  
The subarrays are: `[1, 2]` and `[3]`

---

### Notes

- The prefix sum technique is a powerful tool for range-based queries.
- The line `dict1 = {0: 1}` handles cases when a subarray starting from index 0 sums to `k`.
---


## Question 22: Pascal Triangle Variants

---

### Type 1: Element at Specific Position (r, c)

```python
def nCr(n, r):
    res = 1
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return res

def pascalTriangle(r, c):
    element = nCr(r - 1, c - 1)
    return element

r = 5  # row number
c = 3  # col number
element = pascalTriangle(r, c)
print(f"The element at position (r,c) is: {element}")
```

---

### Type 2: Return a Full Row of Pascal's Triangle (1-indexed)

```python
def nCr(n, r):
    res = 1
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return res

def pascalTriangle(n):
    ans = []
    for c in range(1, n + 1):
        ans.append(nCr(n - 1, c - 1))
    return ans

n = 5
print(pascalTriangle(n))
```

---

### Type 3: Generate a Row Using a Single Loop (Optimized)

```python
def pascalTriangle(n):
    ans = 1
    result = [1]

    for i in range(1, n):
        ans = ans * (n - i)
        ans = ans // i
        result.append(ans)

    return result

n = 14
print(pascalTriangle(n))
```

---

### Type 4: Full Pascal Triangle Till n Rows (1-indexed)

```python
from typing import *

def generateRow(row):
    ans = 1
    ansRow = [1]
    for col in range(1, row):
        ans *= (row - col)
        ans //= col
        ansRow.append(ans)
    return ansRow

def pascalTriangle(n: int) -> List[List[int]]:
    ans = []
    for row in range(1, n + 1):
        ans.append(generateRow(row))
    return ans

n = 5
ans = pascalTriangle(n)
for it in ans:
    for ele in it:
        print(ele, end=" ")
    print()
```

---

## Question 23: Majority Elements 2 (Appearing More Than ⌊n/3⌋ Times)

Given an integer array `nums`, return all elements that appear more than ⌊n/3⌋ times. You may return the answer in **any order**.

---

### Brute-force Approach

**Time Complexity:** O(n²)  
**Not efficient for large inputs**

```python
def majorityElement(nums):
    n = len(nums)
    result = []
    for i in range(n):
        count = 0
        for j in range(n):
            if nums[j] == nums[i]:
                count += 1
        if count > n // 3 and nums[i] not in result:
            result.append(nums[i])
    return result

# Example usage
nums = [3, 2, 3]
print(majorityElement(nums))  # Output: [3]
```

---

### Optimal Approach: Moore's Voting Algorithm Extension

**Time Complexity:** O(n)  
**Space Complexity:** O(1)  

There can be **at most 2 elements** that appear more than ⌊n/3⌋ times.

```python
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cnt1, cnt2 = 0, 0
        element1, element2 = None, None

        # First pass: Find potential candidates
        for num in nums:
            if element1 == num:
                cnt1 += 1
            elif element2 == num:
                cnt2 += 1
            elif cnt1 == 0:
                element1, cnt1 = num, 1
            elif cnt2 == 0:
                element2, cnt2 = num, 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        # Second pass: Verify the candidates
        cnt1, cnt2 = 0, 0
        for num in nums:
            if num == element1:
                cnt1 += 1
            elif num == element2:
                cnt2 += 1

        result = []
        if cnt1 > n // 3:
            result.append(element1)
        if cnt2 > n // 3:
            result.append(element2)

        return result

# Example usage
nums = [1, 1, 1, 3, 3, 2, 2, 2]
print(Solution().majorityElement(nums))  # Output: [1, 2]
```
---
### Tip
This algorithm generalizes for **majority element > n/k** — maintain at most (k - 1) potential candidates.

---

## Question 24: 3Sum – Find All Unique Triplets That Sum to Zero
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that:
- `i != j`, `i != k`, and `j != k`
- `nums[i] + nums[j] + nums[k] == 0`
Return the solution **without duplicates**.
---
### Approach 1: Brute-force with HashSet (Incorrect Implementation)
```python
def threeSum(nums):
    n = len(nums)
    res = set()
    
    for i in range(n):
        seen = set()
        for j in range(i + 1, n):
            complement = -(nums[i] + nums[j])
            if complement in seen:
                # Bug: 'complement' is a value, not an index
                triplet = tuple(sorted((nums[i], nums[j], complement)))
                res.add(triplet)
            else:
                seen.add(nums[j])
    
    return [list(triplet) for triplet in res]

arr = [-1, 0, 1, 2, -1, -4]
o = threeSum(arr)
print(o)  # Output may be incorrect due to logic error
```

**Note:**  

The first implementation has a logical mistake.  
In `nums[complement]`, `complement` is a **value**, not an index.  
To fix this, we can directly use `complement` in the triplet instead.

---
### Approach 2: Optimal – Sorting + Two Pointers
```python
def triplet(n, arr):
    if n < 3:
        return []

    ans = []
    arr.sort()
    
    for i in range(n):
        if i != 0 and arr[i] == arr[i - 1]:
            continue  # Skip duplicates for first number

        j, k = i + 1, n - 1
        while j < k:
            total_sum = arr[i] + arr[j] + arr[k]
            if total_sum < 0:
                j += 1
            elif total_sum > 0:
                k -= 1
            else:
                ans.append([arr[i], arr[j], arr[k]])
                j += 1
                k -= 1
                while j < k and arr[j] == arr[j - 1]:
                    j += 1
                while j < k and arr[k] == arr[k + 1]:
                    k -= 1

    return ans

arr = [-1, 0, 1, 2, -1, -4]
n = len(arr)
ans = triplet(n, arr)
print(ans)  # Output: [[-1, -1, 2], [-1, 0, 1]]
```
---

### Time & Space Complexity
| Approach                 | Time Complexity | Space Complexity           | Duplicates Handled |
|--------------------------|-----------------|----------------------------|---------------------|
| Brute (HashSet)          | O(n²)           | O(n)                       | ❌ No (also logic bug) |
| Optimal (Two Pointer)    | O(n²)           | O(1) (excluding output)    | ✅ Yes |
---
### Final Output
```python
[[-1, -1, 2], [-1, 0, 1]]
```

---

## Question 25: Maximum Product Subarray

Given an integer array `arr`, find the contiguous subarray within the array (containing at least one number) that has the **largest product** and return that product.

---

### Approach: Two-Pass Traversal (Prefix & Suffix Product)
We traverse the array from both directions to keep track of the prefix product and the suffix product.
- If any element is zero, we reset the corresponding product to 1.
- The answer is the maximum of the current prefix, suffix, or previously stored maximum.
This method efficiently handles zeros and negative numbers.

---

### Code

```python
def maxProductSubArray(arr):
    n = len(arr)  # Size of array
    pre, suff = 1, 1
    ans = float('-inf')
    
    for i in range(n):
        if pre == 0:
            pre = 1
        if suff == 0:
            suff = 1
        pre *= arr[i]
        suff *= arr[n - i - 1]
        ans = max(ans, max(pre, suff))
    
    return ans

# Example usage
arr = [1, 2, -3, 0, -4, -5]
print("The maximum product subarray is:", maxProductSubArray(arr))
```
---
### Time & Space Complexity
- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)
---
### Example
#### Input:
```python
arr = [1, 2, -3, 0, -4, -5]
```
#### Output:
```
20
```
#### Explanation:
The maximum product subarray is `[-4, -5]` with product `20`.

---

### Notes
- This approach avoids nested loops and handles edge cases with zero and negative numbers effectively.
- A classic trick: traversing both forward and backward helps catch the best subarray regardless of zero resets and sign flips.

---

## Question 26: Four Sum (Find Unique Quadruplets)

### Problem Statement
Given an array `nums` of `n` integers and an integer `target`, return all unique quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that:
```
0 <= a, b, c, d < n
a, b, c, and d are distinct
nums[a] + nums[b] + nums[c] + nums[d] == target
```

### Approach 1: Better (Using Hashing)
**Idea:** Fix two elements using nested loops, and for the remaining two, use hashing to check if the required fourth element exists.

**Code:**
```python
def fourSumBetter(nums, target):
    n = len(nums)
    ans = set()
    for i in range(n):
        for j in range(i + 1, n):
            hashSet = set()
            for k in range(j + 1, n):
                rem = target - (nums[i] + nums[j] + nums[k])
                if rem in hashSet:
                    temp = tuple(sorted([nums[i], nums[j], nums[k], rem]))
                    ans.add(temp)
                hashSet.add(nums[k])
    return [list(t) for t in ans]

nums = [1, 0, -1, 0, -2, 2]
target = 0
x = fourSumBetter(nums, target)
print("Better Approach Output:", x)
```

**Time Complexity:** O(n³)  
**Duplicates:** Handled via `set`

### Approach 2: Optimal (Two Pointers + Sorting)
**Idea:** Sort the array. Fix two pointers (`a`, `b`) and use two pointers (`c`, `d`) to find remaining numbers.

**Code:**
```python
def fourSumOptimal(nums, target):
    n = len(nums)
    nums.sort()
    if n < 4:
        return []
    ans = []
    for a in range(n):
        if a > 0 and nums[a] == nums[a - 1]:
            continue
        for b in range(a + 1, n):
            if b > a + 1 and nums[b] == nums[b - 1]:
                continue
            c = b + 1
            d = n - 1
            while c < d:
                totalSum = nums[a] + nums[b] + nums[c] + nums[d]
                if totalSum < target:
                    c += 1
                elif totalSum > target:
                    d -= 1
                else:
                    ans.append([nums[a], nums[b], nums[c], nums[d]])
                    c += 1
                    d -= 1
                    while c < d and nums[c] == nums[c - 1]:
                        c += 1
                    while c < d and nums[d] == nums[d + 1]:
                        d -= 1
    return ans

nums = [1, 0, -1, 0, -2, 2]
target = 0
x = fourSumOptimal(nums, target)
print("Optimal Approach Output:", x)
```

**Time Complexity:** O(n³)  
**Duplicates:** Handled via sorting and skips

### Output
```python
Better Approach Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
Optimal Approach Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
```

### Conclusion
- **Better Approach:** Simpler but slower, avoids duplicates via `set`
- **Optimal Approach:** Cleaner and faster due to sorting + pointer technique

---

## Question 27: Maximum Length Subarray with Sum = 0

### Problem Statement
Given an array `nums`, find the **maximum length** of a subarray with sum equal to 0.

### Approach: Prefix Sum with Hash Map
**Idea:**  
- Keep a running sum (`Sum`).  
- Store first occurrence of each sum in a map (`mpp`).  
- If sum is seen again, the subarray between those indices has sum 0.

**Code:**
```python
def maxSubArray(nums):
    n = len(nums)
    mpp = {} 
    maxlength = 0
    Sum = 0
    for i in range(n):
        Sum += nums[i]
        if Sum == 0:
            maxlength = i + 1
        elif Sum in mpp:
            maxlength = max(maxlength, i - mpp[Sum])
        else:
            mpp[Sum] = i
    return maxlength

nums = [1, 2, -2, 4, -4]
print(maxSubArray(nums))  # Output: 5
```

**Time Complexity:** O(n)  
**Space Complexity:** O(n)



## Question 28: Count Subarrays with XOR Equal to K

### Problem Statement
Given an array, count the number of subarrays whose XOR is equal to `k`.

### Approach: Prefix XOR with HashMap
We keep track of the prefix XOR in `xr`.  
For each index, we check if `xr ^ k` exists in the map.  
If it does, it means a subarray ending at the current index has XOR `k`.

### Code
```python
def xorSubArray(nums, k):
    n = len(nums)
    cnt = 0
    hashMap = {0: 1}
    xr = 0
    for i in range(n):
        xr = xr ^ nums[i]
        x = xr ^ k
        cnt += hashMap.get(x, 0)
        hashMap[xr] = hashMap.get(xr, 0) + 1
    return cnt

nums = [4, 2, 2, 4, 6]
print("The number of subarrays with XOR equal to 6 is:", xorSubArray(nums, k=6))
```

### Time and Space Complexity
- **Time Complexity:** O(n)  
- **Space Complexity:** O(n)

### Output
```
The number of subarrays with XOR equal to 6 is: 4
```

---

## Question 29: Find the Missing and Repeating Number in an Array

### Problem Statement
Given an array from `0` to `n-1` with one number missing and one number repeating, find both.

### Approach: Using Sum and Square Sum Formulas
1. Compute expected sum `Sn` and square sum `S2n`.  
2. Compute actual sum `S` and square sum `S2`.  
3. Use equations:
   - `S - Sn = x - y`
   - `S2 - S2n = x² - y² = (x - y)(x + y)`
4. Solve to find `x` (repeating) and `y` (missing)

### Code
```python
def findMissingAndRepeating(nums):
    n = len(nums)
    Sn = (n * (n - 1)) / 2
    S2n = (n * (n - 1) * (2 * n - 1)) / 6
    S = 0
    S2 = 0
    for num in nums:
        S += num
        S2 += num ** 2
    val1 = S - Sn
    val2 = S2 - S2n
    val2 = val2 / val1
    x = (val1 + val2) / 2
    y = x - val1
    return int(y), int(x)

nums = [0, 1, 2, 3, 3, 5]
print("Missing and Repeating Numbers:", findMissingAndRepeating(nums))
```

### Example
```python
Input: nums = [0, 1, 2, 3, 3, 5]
Output: (4, 3)
```
- Missing number = 4  
- Repeating number = 3

### Time and Space Complexity
- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)

---

## Question 30: Island Perimeter

### Problem Statement
Given a 2D grid of 0s (water) and 1s (land), return the perimeter of the island.  
There is exactly one island with no lakes, and each land cell is connected horizontally or vertically.

### Approach
1. Traverse each cell.  
2. For each land cell (`1`), add 4 to perimeter.  
3. Subtract 2 for each adjacent land above or to the left.  
4. This avoids double-counting edges.

### Code
```python
def islandPerimeterOptimised(grid):
    n = len(grid)
    m = len(grid[0])
    perimeter = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2
    return perimeter
```

### Example Usage
```python
grid = [
  [0, 1, 0, 0],
  [1, 1, 1, 0],
  [0, 1, 0, 0],
  [1, 1, 0, 0]
]
print(islandPerimeterOptimised(grid))
```

### Output
```
16
```

### Time and Space Complexity
- **Time Complexity:** O(n × m)  
- **Space Complexity:** O(1)

---


## Question 31: Check if Array is Monotonic
```python
def isMonotonic(nums):
    increasing = decreasing = True
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            decreasing = False
        elif nums[i] < nums[i - 1]:
            increasing = False
    return increasing or decreasing
```
**Example Usage:**
```python
print(isMonotonic([1, 2, 2, 3]))   # True
print(isMonotonic([6, 5, 4, 4]))   # True
print(isMonotonic([1, 3, 2]))      # False
```
**Time:** O(n) **Space:** O(1)

---

## Question 32: Find All K-Distant Indices in an Array
```python
def findKDistantIndices(nums, key, k):
    ans = set()
    n = len(nums)
    for i in range(n):
        if nums[i] == key:
            for j in range(max(0, i - k), min(n, i + k + 1)):
                ans.add(j)
    return sorted(ans)
```
**Example Usage:**
```python
nums = [3, 4, 9, 1, 3, 9, 5]
key = 9
k = 1
print(findKDistantIndices(nums, key, k))  # [1, 2, 3, 4, 5, 6]
```
**Time:** O(n·k) **Space:** O(n)

---

## Question 33: Merge Sorted Array
```python
def merge(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
    return nums1
```
**Example Usage:**
```python
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
x = merge(nums1, m, nums2, n)
print(x)  # [1, 2, 2, 3, 5, 6]
```
**Time:** O(m+n) **Space:** O(1)

---

## Question 34: Number of Ways to Split Array

```python
def waysToSplitArray(nums):
    totalSplits = 0
    n = len(nums)
    lsum = 0
    rsum = sum(nums)
    for i in range(n - 1):
        lsum += nums[i]
        rsum -= nums[i]
        if lsum >= rsum:
            totalSplits += 1
    return totalSplits
```
**Example Usage:**
```python
nums = [10, 4, -8, 7]
print(waysToSplitArray(nums))  # 2
```
**Time:** O(n) **Space:** O(1)
