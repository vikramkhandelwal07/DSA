  

# 1.  Set Matrix Zeroes
## 🧾 Problem Statement
Given an `n x m` matrix, if an element is `0`, set its entire row and column to `0`. Do it **in-place** (i.e., modify the input matrix without using extra space for another matrix).

---
## 📘 Description
You are given a 2D array of integers. Your task is to set the entire row and column to zero for any cell that has a zero in it.
- Modifications must be done **in-place**.
- Try to optimize for **space** as well as **time**.
---
##  Examples
### ✅ Example 1 (Easy)
**Input:**

```
matrix = [
  [1, 1, 1],
  [1, 0, 1],
  [1, 1, 1]
]
```
**Output:**
```
[
  [1, 0, 1],
  [0, 0, 0],
  [1, 0, 1]
]
```
---
### ✅ Example 2 (Hard)
**Input:**
```
matrix = [
  [0, 1, 2, 0],
  [3, 4, 5, 2],
  [1, 3, 1, 5]
]
```
**Output:**
```
[
  [0, 0, 0, 0],
  [0, 4, 5, 0],
  [0, 3, 1, 0]
]
```
---
## 🚀 Approaches
---
### 🔴 1. Brute Force (Using -1 Marker)
#### 💡 Logic:
Whenever we see a 0, mark its row and column using `-1` (a temporary marker). Then, in a second pass, convert all `-1`s to 0s.
#### 🕒 Time Complexity:
`O(n × m × (n + m))`  
For each zero, mark row & column.
#### 💾 Space Complexity:
`O(1)` (modifies in-place, but not reliable with `-1` if matrix contains negative values)
#### ⚠️ Drawback:
If `-1` is already a valid element in the matrix, it breaks.

---
### 🟡 2. Better Approach (Using Extra Arrays)
#### 💡 Logic:
Create two extra arrays `row[]` and `col[]` to track which rows and columns should be zeroed. Then traverse and apply zeros.
#### 🕒 Time Complexity:
`O(n × m)` — 2 passes over the matrix.
#### 💾 Space Complexity:
`O(n + m)` — Extra space for row and column markers.
#### ✅ Code:
```python
def zeroMatrix(matrix, n, m):
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
```

---
### 🟢 3. Optimal Approach (In-Place Marking with First Row & Col)

#### 💡 Logic:
Use the first row and column as markers instead of extra arrays. Also, track a `col0` flag to manage the first column separately.
#### 🕒 Time Complexity:
`O(n × m)`
#### 💾 Space Complexity:
`O(1)` — truly in-place
#### ✅ Code:
```python
def zeroMatrix(matrix, n, m):
    col0 = 1
    # Mark rows & columns
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                if j == 0:
                    col0 = 0
                else:
                    matrix[0][j] = 0
  
    # Update cells except first row & col
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
  
    # Zero the first row
    if matrix[0][0] == 0:
        for j in range(m):
            matrix[0][j] = 0
            
      # Zero the first column
    if col0 == 0:
        for i in range(n):
            matrix[i][0] = 0

    return matrix
```  
---
## ✅ Conclusion

| Approach      | Time Complexity    | Space Complexity   | In-Place? | Notes                         |
| ------------- | ------------------ | ------------------ | --------- | ----------------------------- |
| Brute Force   | O(n × m × (n + m)) | O(1)               | ✅         | Risky due to use of `-1`      |
| Better        | O(n × m)           | O(n + m)           | ❌         | Simple, but uses extra space  |
| Optimal       | O(n × m)           | O(1)               | ✅         | Best solution                 |

---
# 2.Pascal Triangle implementation

## 🧾 Problem Statement
Given an integer `n`, generate the nth row, a specific element at (r, c), or the complete Pascal's Triangle up to `n` rows. Pascal's Triangle is a triangular array of binomial coefficients.

---

## 📘 Description
Pascal's Triangle is constructed as follows:
- The triangle starts with a `1` at the top.
- Each number is the sum of the two numbers directly above it.
- The element at position `(r, c)` corresponds to the binomial coefficient `C(r-1, c-1)`.

There are three common variations of Pascal Triangle problems:
1. Get a specific element.
2. Get an entire row.
3. Generate the full triangle.

---

## 🧪 Examples

### Type 1: Element at (r, c)
**Input:** r = 5, c = 3  
**Output:** 6

### Type 2: nth Row
**Input:** n = 5  
**Output:** [1, 4, 6, 4, 1]

### Type 3: Full Triangle with 4 rows
**Output:**
```
[
 [1],
 [1, 1],
 [1, 2, 1],
 [1, 3, 3, 1]
]
```

---

## ✅ Implementations

### 🔹 Type 1: Element at (r, c)
```python
def nCr(n, r):
    res = 1
    for i in range(r):
        res *= (n - i)
        res //= (i + 1)
    return res

def pascalTriangle(r, c):
    return nCr(r - 1, c - 1)

r = 5
c = 3
print(f"The element at position (r,c) is: {pascalTriangle(r, c)}")
```

🕒 **Time Complexity:** O(c)  
💾 **Space Complexity:** O(1)

---

### 🔹 Type 2: nth Row of Pascal's Triangle
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

🕒 **Time Complexity:** O(n)  
💾 **Space Complexity:** O(n)

---

### 🔹 Type 3: Complete Pascal's Triangle
```python
def generateRows(row):
    ans = 1
    ansRow = [1]
    for col in range(1, row):
        ans *= row - col
        ans //= col
        ansRow.append(ans)
    return ansRow

def pascalTriangle(numRows):
    ans = []
    for row in range(1, numRows + 1):
        ans.append(generateRows(row))
    return ans

print(pascalTriangle(5))
```

🕒 **Time Complexity:** O(n²)  
💾 **Space Complexity:** O(n²)

---

## 🔍 Explanations
- We use the combination formula `nCr = n! / (r!(n-r)!)` to compute values.
- Each row of Pascal's Triangle represents the coefficients of the binomial expansion.
- For memory efficiency, Type 1 and Type 2 are best.
- Type 3 is ideal when visualization of the whole triangle is needed.

---

Use the right type based on your need: element access, single row, or full triangle!

# 3.Next Permutation 

## 📋 Problem Statement
Given an array of integers `nums`, rearrange them to form the **next lexicographically greater permutation** of numbers. If no such permutation exists (i.e., the array is sorted in descending order), rearrange it as the **lowest possible order** (i.e., sorted in ascending order).

The replacement must be done **in-place**, using only constant extra memory.

---

## 📘 Description
This problem is a classic application of permutation logic, often used in combinatorics:
- We want to transform the current arrangement into the next one that would appear in sorted order.
- If we're at the last permutation, we cycle back to the first.

---

## 🧪 Examples

### Easy Example
**Input:** [1, 2, 3]  
**Output:** [1, 3, 2]

### Hard Example
**Input:** [2, 3, 6, 5, 4, 1]  
**Output:** [2, 4, 1, 3, 5, 6]

**Explanation:**
- Find the pivot index: 3 < 6 ✅ at index 1
- Swap with next bigger value from the end (4)
- Reverse the subarray after index 1

---

## ✅ Implementations

### 🔷 Brute Force (Generate All Permutations)
```python
from itertools import permutations

def brute_next_permutation(nums):
    all_perms = sorted(set(permutations(nums)))
    idx = all_perms.index(tuple(nums))
    return list(all_perms[0]) if idx == len(all_perms) - 1 else list(all_perms[idx + 1])

nums = [2, 3, 6, 5, 4, 1]
print(brute_next_permutation(nums))
```

⏱ **Time Complexity:** O(n!)  
📀 **Space Complexity:** O(n!)

---

### 🔹 Better (Using Python Library)
```python
import itertools

def better_next_permutation(nums):
    try:
        next_perm = next(itertools.islice(
            (p for p in sorted(set(itertools.permutations(nums))) if list(p) > nums),
            0, 1
        ))
        return list(next_perm)
    except StopIteration:
        return sorted(nums)

nums = [2, 3, 6, 5, 4, 1]
print(better_next_permutation(nums))
```

⏱ **Time Complexity:** O(n!) in worst case  
📀 **Space Complexity:** O(n!)

---

### 🔶 Optimal (In-place Rearrangement)
```python
def nextPermutation(nums):
    n = len(nums)
    index = -1
    
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            index = i
            break

    if index == -1:
        nums.reverse()
        return nums

    for i in range(n - 1, index, -1):
        if nums[i] > nums[index]:
            nums[i], nums[index] = nums[index], nums[i]  
            break

    nums[index + 1:] = reversed(nums[index + 1:])
    return nums

nums = [2, 3, 6, 5, 4, 1]
print(nextPermutation(nums))
```

🕐 **Time Complexity:** O(n)  
📀 **Space Complexity:** O(1)

---

## 🔍 Explanation (Step-by-Step)
1. Traverse from right to left to find the first index `i` where `nums[i] < nums[i + 1]`. This is called the **breakpoint**.
2. If no such index is found, the array is in descending order. Simply reverse it to get the smallest permutation.
3. Otherwise, find the **smallest number greater than `nums[i]`** to its right, then swap them.
4. Finally, reverse the subarray from `i+1` to end to get the next permutation.

---

This approach is efficient, elegant, and commonly used in interview and competitive programming scenarios.

# 4.Kadane's Algorithm - Maximum Subarray Sum

## 📋 Problem Statement
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

---
##  Example
### Input:
```python
nums = [-2,1,-3,4,-1,2,1,-5,4]
```
### Output:
```
Sum of maximum subarray: 6
Subarray: [4, -1, 2, 1]
```

---
## ✅ Approaches
### 🟧 Brute Force
```python
# TC - O(N^3)
# SC - O(1)

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
```

---
### 🟧 Better
```python
# TC - O(N^2)
# SC - O(1)

def maxSubArray(nums):
    n = len(nums)
    maxi = -10**5
    for i in range(n):
        sum_ = 0
        for j in range(i, n):
            sum_ += nums[j]
            maxi = max(maxi, sum_)
    return maxi
```

---

### 🟩 Optimal (Kadane's Algorithm)
```python
# TC - O(N)
# SC - O(1)
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
    if maxi < 0:
        maxi = 0
    return maxi
```

#### 🔍 Explanation
1. `sum_` keeps a running total of the current subarray.
2. If it drops below 0, it's reset, as a negative sum won't help the upcoming subarray.
3. `maxi` stores the maximum seen so far.
4. In case all elements are negative, it returns 0.

---

## 🧩 Follow-Up: Print the Subarray with Maximum Sum
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

    print(f"The subarray is: {nums[ansStart:ansEnd + 1]}")
    return maxi

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
output = maxSubArray(nums)
print("Sum of maximum subarray:", output)
```

#### 🔍 Explanation
- `start` tracks the possible start index of a new subarray when the sum resets.
- `ansStart` and `ansEnd` are updated when a new `maxi` is found.
- The final subarray is sliced using these indices.

---

# 5. Sort Colors - Dutch National Flag Algorithm

## 📊 Problem Statement
Given an array `nums` with `n` objects colored red, white, or blue, sort them **in-place** so that objects of the same color are adjacent, with the colors in the order red (0), white (1), and blue (2).

You must solve this problem **without using the sort()** library function.

---
## 🧪 Example
### Input:
```python
nums = [2, 0, 2, 1, 1, 0]
```
### Output:
```
[0, 0, 1, 1, 2, 2]
```

---

## ✅ Optimal Approach (Dutch National Flag Algorithm)
```python
def sortColours(nums):
    n = len(nums)
    low = 0
    mid = 0
    high = n - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums
```

### 🔍 Explanation
- **`low`**: The region before this index contains all 0s.
- **`mid`**: Current element under consideration.
- **`high`**: The region after this contains all 2s.

### Steps:
1. If `nums[mid] == 0`, swap with `low`, move both `low` and `mid` forward.
2. If `nums[mid] == 1`, it's in place; move `mid` forward.
3. If `nums[mid] == 2`, swap with `high`, and move `high` backward (don’t increment mid!).

---

## 🕒 Time & Space Complexity
- **Time Complexity:** `O(N)`
- **Space Complexity:** `O(1)` (in-place)

---

This algorithm is optimal and widely used in problems involving categorization or partitioning. It’s a popular interview question asked by companies like **Google**, **Amazon**, and **Facebook**.


# 6. Best Time to Buy and Sell Stock

## 📋 Problem Statement
You are given an array `prices` where `prices[i]` is the price of a given stock on the `i-th` day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

---

## 🧪 Example
### Input:
```python
prices = [7,1,5,3,6,4]
```
### Output:
```
5
```
### Explanation:
Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.

---

## ✅ Optimal Approach
```python
def maxProfit(prices):
    minPrice = float('inf')
    maxProfit = 0

    for price in prices:
        if price < minPrice:
            minPrice = price
        elif price - minPrice > maxProfit:
            maxProfit = price - minPrice

    return maxProfit
```

---

## 🔍 Explanation
- We initialize `minPrice` to infinity and `maxProfit` to 0.
- For each price in the array:
  - If it's smaller than the current `minPrice`, we update `minPrice`.
  - Otherwise, we calculate the profit by subtracting `minPrice