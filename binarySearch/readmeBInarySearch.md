  

# 1. Binary Search — Iterative Approach

## 📝 Problem Statement
Given a sorted array `nums` and a target value `target`, return the **index of `target`** if it exists in the array. Otherwise, return `-1`.
---
##  Approach 
Hum **binary search** algorithm use karte hain.  
Do pointers lete hain: `low` aur `high`.  
Har step pe:
- Agar `nums[mid] == target` hai, to `mid` return karo.
- Agar `nums[mid] < target`, to `low = mid+1` kar do.
- Agar `nums[mid] > target`, to `high = mid-1` kar do.
Jab tak `low > high` nahi ho jata, tab tak repeat karte hain. Agar nahi mila, to `-1` return karte hain.
---
##  Patterns / Concepts
✅ Binary Search  
✅ Two Pointer Technique  
✅ Divide and Conquer  

---
## Time Complexity
**O(log n)** — because we halve the search space at each step.  
**O(1)** — since we use only a few extra variables. 

---

## Example
**Input:**  
`nums = [2,3,4,5,6,7,8,9,56]`, `target = 56`
**Output:**  
`your target element 56 is at index: 8`
---

## 🚧 Edge Cases
✅ **Edge Case 1:**  
**Input:** `nums = []`, `target = 5`  
**Output:** `-1` (array is empty)

✅ **Edge Case 2:**  
**Input:** `nums = [1]`, `target = 1`  
**Output:** `0` (single element found)
---  
```python

# Function to perform binary search iteratively

def BinarySearch(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    # Loop until low and high cross
    while low <= high:
        mid = low + ((high - low) // 2)  # Calculate middle index safely
        if nums[mid] == target:
            return mid  # Target found at mid
        elif nums[mid] < target:
            low = mid + 1  # Search right half
        else:
            high = mid - 1  # Search left half  
    return -1  # Target not found

# Example usage
nums = [2, 3, 4, 5, 6, 7, 8, 9, 56]
target = 56
output = BinarySearch(nums, target)
print(f"your target element {target} is at index:", output)

```

# 2. Lower Bound — Iterative Binary Search

## Problem Statement
Given a sorted array `nums` and a target value `x`, return the **index of the first element in `nums` which is greater than or equal to `x`** (the lower bound).  
If all elements are smaller than `x`, return `n` (size of array).

## Approach 
### English
We use a modified **binary search**.  
We maintain two pointers: `low` and `high`, and initialize `ans = n`.  
At each step:  
- If `nums[mid] >= x`, this could be our answer, so we update `ans = mid` and move `high = mid - 1`.
- Else, move `low = mid + 1`.

Loop until `low > high`. `ans` will be the index of lower bound.

### Hinglish
Hum modified **binary search** use karte hain.  
Do pointers lete hain: `low` aur `high`, aur ek `ans = n` initialize karte hain.  
Har step pe:  
- Agar `nums[mid] >= x` ho, to ye ek potential answer ho sakta hai, to `ans = mid` aur `high = mid -1` kar dete hain.
- Nahi to `low = mid+1` kar dete hain.

Jab tak `low > high` nahi ho jata, tab tak loop chalta hai. Final `ans` lower bound ka index hoga.

## Patterns / Concepts
Binary Search  
Lower Bound in Sorted Array  
Divide and Conquer

## Time Complexity
**O(log n)** — because we halve the search space at each step.

## Space Complexity
**O(1)** — since we use only a few extra variables.

## Example
**Input:**  
`nums = [2, 3, 7, 8, 8, 8, 9, 10, 56]`, `x = 8`

**Output:**  
`Your lowerbound for the el 8 is at index: 3 --> 8`

## Edge Cases
**Edge Case 1:**  
**Input:** `nums = []`, `x = 5`  
**Output:** `0` (array is empty, conventionally returns size `0`)  

**Edge Case 2:**  
**Input:** `nums = [1, 2, 3]`, `x = 10`  
**Output:** `3` (all elements are smaller than `x`, so returns `n`)  

## Code with Comments
```python
def Lowerbound(nums, x, n):
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

nums = [2, 3, 7, 8, 8, 8, 9, 10, 56]
x = 8
n = len(nums)
output = Lowerbound(nums, x, n)
print(f"Your lowerbound for the el {x} is at index: {output} --> {nums[output]} ")

```

# 3. Upper Bound — Iterative Binary Search

## Problem Statement
Given a sorted array `nums` and a target value `x`, return the **index of the first element in `nums` which is strictly greater than `x`** (the upper bound).  
If no such element exists, return `n` (size of array).

## Approach
### English
We use a modified **binary search**.  
We maintain two pointers: `low` and `high`, and initialize `ans = n`.  
At each step:  
- If `nums[mid] > x`, this could be our answer, so we update `ans = mid` and move `high = mid - 1`.
- Else, move `low = mid + 1`.

Loop until `low > high`. `ans` will be the index of upper bound.

### Hinglish
Hum modified **binary search** use karte hain.  
Do pointers lete hain: `low` aur `high`, aur ek `ans = n` initialize karte hain.  
Har step pe:  
- Agar `nums[mid] > x` ho, to ye ek potential answer ho sakta hai, to `ans = mid` aur `high = mid -1` kar dete hain.
- Nahi to `low = mid+1` kar dete hain.

Jab tak `low > high` nahi ho jata, tab tak loop chalta hai. Final `ans` upper bound ka index hoga.

## Patterns / Concepts
Binary Search  
Upper Bound in Sorted Array  
Divide and Conquer

## Time Complexity
**O(log n)** — because we halve the search space at each step.

## Space Complexity
**O(1)** — since we use only a few extra variables.

## Example
**Input:**  
`nums = [2, 3, 4, 5, 6, 7, 8, 8, 8, 9, 56]`, `x = 8`

**Output:**  
`Your upperbound for the el 8 is at index: 9`

## Edge Cases
**Edge Case 1:**  
**Input:** `nums = []`, `x = 5`  
**Output:** `0` (array is empty, conventionally returns size `0`)  

**Edge Case 2:**  
**Input:** `nums = [1, 2, 3]`, `x = 10`  
**Output:** `3` (all elements are smaller than or equal to `x`, so returns `n`)  

## Code with Comments
```python
def upperbound(nums, x, n):
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] > x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

nums = [2, 3, 4, 5, 6, 7, 8, 8, 8, 9, 56]
x = 8
n = len(nums)
output = upperbound(nums, x, n)
print(f"Your upperbound for the el {x} is at index:", output)
```

# 4. Find Pivot in Rotated Sorted Array — Iterative Binary Search

## Problem Statement
Given a **rotated sorted array** `nums`, find the **index of the smallest element (pivot)** where the rotation happens.  
If the array is not rotated, return `0`.

## Approach / तरीका (English + Hinglish)
### English
We use a modified **binary search** to locate the pivot point (smallest element).  
We maintain two pointers: `low` and `high`.  
- If `nums[low] < nums[high]`, the array is already sorted and pivot is at index `0`.  
- Otherwise, we keep checking `mid`:
  - If `nums[mid] > nums[mid+1]`, then `mid+1` is pivot.
  - If `nums[mid] < nums[mid-1]`, then `mid` is pivot.
- If `nums[mid] >= nums[low]`, move `low = mid+1`.
- Else move `high = mid-1`.

Loop until `low > high`. If not found explicitly, pivot is at `0`.

### Hinglish
Hum modified **binary search** use karte hain pivot point (smallest element) dhoondhne ke liye.  
Do pointers lete hain: `low` aur `high`.  
- Agar `nums[low] < nums[high]`, matlab array already sorted hai aur pivot `0` hai.  
- Nahi to, `mid` check karte hain:
  - Agar `nums[mid] > nums[mid+1]`, to `mid+1` pivot hai.
  - Agar `nums[mid] < nums[mid-1]`, to `mid` pivot hai.
- Agar `nums[mid] >= nums[low]`, to `low = mid+1`.
- Nahi to `high = mid-1`.

Agar loop ke baad bhi nahi mila, to pivot `0` hai.

## Patterns / Concepts
Binary Search  
Find Minimum in Rotated Sorted Array  
Divide and Conquer

## Time Complexity
**O(log n)** — because we halve the search space at each step.

## Space Complexity
**O(1)** — since we use only a few extra variables.

## Example
**Input:**  
`nums = [6, 7, 8, 1, 2, 3, 4, 5]`

**Output:**  
`The pivot is at index: 3`

## Edge Cases
**Edge Case 1:**  
**Input:** `nums = [1, 2, 3, 4, 5]`  
**Output:** `0` (array is already sorted)

**Edge Case 2:**  
**Input:** `nums = [2, 1]`  
**Output:** `1` (pivot at last index)

## Code with Comments
```python
def search(nums):
    n = len(nums)
    low = 0
    high = n - 1

    # If array is already sorted
    if nums[low] < nums[high]:
        return 0

    while low <= high:
        mid = (low + high) // 2

        # Check if mid is pivot
        if mid < n - 1 and nums[mid] > nums[mid + 1]:
            return mid + 1
        elif mid > 0 and nums[mid] < nums[mid - 1]:
            return mid

        # Decide which half to search
        if nums[mid] >= nums[low]:
            low = mid + 1
        else:
            high = mid - 1

    return 0  # Pivot not found explicitly, default to 0

nums = [6, 7, 8, 1, 2, 3, 4, 5]
pivot = search(nums)
print(f"The pivot is at index: {pivot}")
```

# 5. Find Floor and Ceil of a Number in a Sorted Array — Iterative Binary Search

## Problem Statement
Given a **sorted array** `arr` of size `n` and a number `x`, find:
- **Floor:** the largest number in `arr` ≤ `x`
- **Ceil:** the smallest number in `arr` ≥ `x`  
If floor or ceil does not exist, return `-1` for that.

## Approach / तरीका (English + Hinglish)
### English
We use two separate binary searches:
- `findFloor`: keep track of the largest `arr[mid] ≤ x` seen so far. Move `low = mid+1` if `arr[mid] ≤ x`.
- `findCeil`: keep track of the smallest `arr[mid] ≥ x` seen so far. Move `high = mid-1` if `arr[mid] ≥ x`.

Return both values as a pair.

### Hinglish
Hum do alag **binary search** chalate hain:
- `findFloor`: ab tak jo sabse bada element `≤ x` mila usse track karte hain. Agar `arr[mid] ≤ x`, to `low = mid+1`.
- `findCeil`: ab tak jo sabse chhota element `≥ x` mila usse track karte hain. Agar `arr[mid] ≥ x`, to `high = mid-1`.

Finally `floor` aur `ceil` pair me return karte hain.

## Patterns / Concepts
Binary Search  
Floor and Ceil in Sorted Array  
Search Space Reduction

## Time Complexity
**O(log n)** — two binary searches, each logarithmic.

## Space Complexity
**O(1)** — no extra space.

## Example
**Input:**  
`arr = [3, 4, 4, 7, 8, 10]`, `x = 5`

**Output:**  
`The floor and ceil are: 4 7`

## Edge Cases
**Edge Case 1:**  
**Input:** `arr = [1, 2, 3]`, `x = 0`  
**Output:** `The floor and ceil are: -1 1` (no floor)

**Edge Case 2:**  
**Input:** `arr = [5, 6, 7]`, `x = 10`  
**Output:** `The floor and ceil are: 7 -1` (no ceil)

## Code with Comments
```python
def findFloor(arr, n, x):
    low = 0
    high = n - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        # possible floor
        if arr[mid] <= x:
            ans = arr[mid]
            low = mid + 1  # look further right
        else:
            high = mid - 1  # look left

    return ans

def findCeil(arr, n, x):
    low = 0
    high = n - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        # possible ceil
        if arr[mid] >= x:
            ans = arr[mid]
            high = mid - 1  # look further left
        else:
            low = mid + 1  # look right

    return ans

def getFloorAndCeil(arr, n, x):
    f = findFloor(arr, n, x)
    c = findCeil(arr, n, x)
    return (f, c)

arr = [3, 4, 4, 7, 8, 10]
n = 6
x = 5
ans = getFloorAndCeil(arr, n, x)
print("The floor and ceil are:", ans[0], ans[1])
```


# 6. Search in Rotated Sorted Array — Iterative Binary Search

## Problem Statement
Given a **rotated sorted array** `nums` and a `target`, return the **index of the target** if it exists in the array.  
If the target is not found, return `-1`.

## Approach / तरीका (English + Hinglish)
### English
We use a modified **binary search**.  
At each step:
- If `nums[mid] == target`, return `mid`.
- If the left half `nums[low..mid]` is sorted:
  - If `target` lies in `nums[low..mid]`, move `high = mid-1`.
  - Else, move `low = mid+1`.
- Else, the right half `nums[mid..high]` is sorted:
  - If `target` lies in `nums[mid..high]`, move `low = mid+1`.
  - Else, move `high = mid-1`.

If the loop finishes without finding, return `-1`.

### Hinglish
Hum modified **binary search** use karte hain.  
Har step pe:
- Agar `nums[mid] == target`, to `mid` return karo.
- Agar left half `nums[low..mid]` sorted hai:
  - Agar `target` left half me hai, to `high = mid-1`.
  - Nahi to `low = mid+1`.
- Warna right half `nums[mid..high]` sorted hai:
  - Agar `target` right half me hai, to `low = mid+1`.
  - Nahi to `high = mid-1`.

Agar nahi mila, to `-1` return karo.

## Patterns / Concepts
Binary Search  
Search in Rotated Sorted Array  
Divide and Conquer

## Time Complexity
**O(log n)** — because each step halves the search space.

## Space Complexity
**O(1)** — only pointers used.

## Example
**Input:**  
`nums = [4,5,6,7,0,1,2]`, `target = 0`

**Output:**  
`4`

## Edge Cases
**Edge Case 1:**  
**Input:** `nums = [1]`, `target = 0`  
**Output:** `-1` (target not present)

**Edge Case 2:**  
**Input:** `nums = [1,3]`, `target = 3`  
**Output:** `1`

## Code with Comments
```python
def search(nums, target):
    n = len(nums)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[low] <= nums[mid]:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            # Right half is sorted
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1
```


# Find Square Root of a Number — Floor Value Using Binary Search

## Problem Statement
Given a **non-negative integer** `n`, find the **floor value of square root of `n`**.  
That is, return the largest integer `x` such that `x*x ≤ n`.

## Approach
### English
We use **binary search** to find the square root.  
We search in the range `[0, n//2]` and keep track of the last `mid` whose square `≤ n` as the answer.

At each step:
- If `mid*mid > n`, move `high = mid-1`.
- Else, store `mid` in `ans` and move `low = mid+1`.

When loop ends, `ans` will hold the floor of square root.

### Hinglish
Hum **binary search** use karke square root nikalte hain.  
Search range hoti hai `[0, n//2]`. Jo `mid*mid ≤ n` hota hai, usse `ans` me store karte hain.

Har step pe:
- Agar `mid*mid > n`, to `high = mid-1`.
- Nahi to `ans = mid` aur `low = mid+1`.

Loop ke baad `ans` me square root ka floor hota hai.

## Patterns / Concepts
Binary Search  
Search Space Reduction  
Square Root

## Time Complexity
**O(log n)** — binary search halves the range each step.

## Space Complexity
**O(1)** — no extra space.

## Example
**Input:**  
`n = 5`

**Output:**  
`2` — since `2*2=4 ≤ 5` but `3*3=9 > 5`

## Edge Cases
**Edge Case 1:**  
**Input:** `n = 0`  
**Output:** `0`

**Edge Case 2:**  
**Input:** `n = 1`  
**Output:** `1`

## Code with Comments
```python
def SqaureRoot(n):
    ans = 0
    low = 0
    high = n // 2

    while low <= high:
        mid = (low + high) // 2

        if mid * mid > n:
            high = mid - 1
        else:
            ans = mid
            low = mid + 1

    return ans

print(SqaureRoot(5))

```


# Find Nth Root of a Number — Using Binary Search

## Problem Statement
Given two integers `n` and `m`, find the integer **x** such that `x^n = m`.  
If no such integer exists, return `-1`.

## Approach 
### English
We use **binary search** to find the `n`th root of `m`.  
We search in the range `[1, m]` and at each step:
- Compute `mid^n` (mid to the power n).
- If `mid^n == m`, we found the root and return `mid`.
- If `mid^n < m`, we search the right half (`low = mid+1`).
- If `mid^n > m`, we search the left half (`high = mid-1`).

If no such integer root is found after the loop, return `-1`.

### Hinglish
Hum **binary search** use karke `n`th root of `m` nikalte hain.  
Search range hoti hai `[1, m]`. Har step pe:
- `mid^n` calculate karte hain.
- Agar `mid^n == m`, to `mid` return kar dete hain.
- Agar `mid^n < m`, to `low = mid+1`.
- Agar `mid^n > m`, to `high = mid-1`.

Agar loop ke baad bhi nahi mila, to `-1` return karte hain.

## Patterns / Concepts
Binary Search  
Nth Root Search  
Search Space Reduction

## Time Complexity
**O(log m)** — binary search on `m`.

## Space Complexity
**O(1)** — no extra space.

## Example
**Input:**  
`n = 2`, `m = 9`

**Output:**  
`3` — since `3^2 = 9`

## Edge Cases
**Edge Case 1:**  
**Input:** `n = 2`, `m = 10`  
**Output:** `-1` (no integer square root of 10)

**Edge Case 2:**  
**Input:** `n = 1`, `m = 5`  
**Output:** `5` (any number to power 1 is itself)

## Code with Comments
```python
def nthRoot(n, m):
    low = 1
    high = m

    while low <= high:
        mid = (low + high) // 2
        power = mid ** n

        if power == m:
            return mid  # found exact root
        elif power < m:
            low = mid + 1  # look in right half
        else:
            high = mid - 1  # look in left half

    return -1  # no integer root found

n = 2
m = 9
print(nthRoot(n, m))
```


# Find Minimum Eating Speed — Using Binary Search

## Problem Statement
Given an array `nums` where `nums[i]` represents the size of the `i-th` pile of bananas and an integer `h` representing the number of hours available, find the **minimum integer eating speed `k`** such that all bananas can be eaten within `h` hours.  

You can eat at most `k` bananas from a pile in an hour, and you must completely finish one pile before moving to the next.

## Approach / तरीका (English + Hinglish)
### English
We use **binary search** to find the smallest valid speed `k`.  
We search in the range `[1, max(nums)]`.  
At each step:
- Assume current `mid` as the eating speed.
- Calculate total hours required at this speed using `totalTime()`.
- If total hours ≤ `h`, store `mid` as answer and try to find smaller speed (`high = mid-1`).
- Otherwise, search in higher speeds (`low = mid+1`).

When the loop ends, `ans` is the minimum valid eating speed.

### Hinglish
Hum **binary search** use karke minimum valid speed `k` nikalte hain.  
Search range hoti hai `[1, max(nums)]`.  
Har step pe:
- Current `mid` ko speed maan ke total hours calculate karte hain.
- Agar total hours ≤ `h`, to `mid` ko `ans` me store karke aur chhoti speed try karte hain (`high = mid-1`).
- Warna badi speed check karte hain (`low = mid+1`).

Loop ke baad `ans` me minimum valid speed hoti hai.

## Patterns / Concepts
Binary Search  
Search on Answer Space  
Greedy Checking

## Time Complexity
**O(n * log(max(nums)))** — binary search on range and linear check at each step.

## Space Complexity
**O(1)** — no extra space.

## Example
**Input:**  
`nums = [3,6,7,11]`, `h = 8`

**Output:**  
`4` — minimum speed to finish all piles in 8 hours.

## Edge Cases
**Edge Case 1:**  
**Input:** `nums = [1]`, `h = 1`  
**Output:** `1` (only one pile)

**Edge Case 2:**  
**Input:** `nums = [30,11,23,4,20]`, `h = 6`  
**Output:** `23`

## Code with Comments
```python
import math

# Helper: calculate total hours at speed k
def totalTime(nums, k):
    hours = 0
    for num in nums:
        hours += math.ceil(num / k)
    return hours

# Main: binary search on k
def minEatingSpeed(nums, h):
    low = 1
    high = max(nums)
    ans = high

    while low <= high:
        mid = (low + high) // 2
        totalhours = totalTime(nums, mid)

        if totalhours <= h:
            ans = mid  # try to minimize
            high = mid - 1
        else:
            low = mid + 1

    return ans
```

# Minimum Days to Make m Bouquets — Binary Search on Answer

## Problem Statement
You are given an integer array `bloomDay`, where `bloomDay[i]` is the day the `i-th` flower blooms.  
You are also given integers `m` and `k`.  

You need to make exactly `m` bouquets, and each bouquet needs exactly `k` **adjacent** bloomed flowers.  
Return the **minimum number of days** you need to wait to be able to make `m` bouquets.  
If it is impossible, return `-1`.

### Example Question Context
This is a **LeetCode Hard problem** — a classic **binary search on answer space** pattern.  
We have to find the smallest day such that it is possible to pick `m` bouquets of `k` adjacent flowers on or before that day.

## Approach / तरीका (English + Hinglish)
### English
We binary search on the answer: the day.  
Range of possible days is `[min(bloomDay), max(bloomDay)]`.  
At each step:
- Assume `mid` day.
- Check if we can make `m` bouquets on `mid` day using `canMakeBouquets(mid)`:
  - Iterate `bloomDay`, count adjacent bloomed flowers on or before `mid`.
  - Every time `k` adjacent flowers are found, increment `bouquets`.
  - Reset counter if an unbloomed flower is encountered.
- If `m` bouquets can be made, try smaller day (`high = mid-1`).
- Else, try larger day (`low = mid+1`).

Return the minimum day found or `-1`.

### Hinglish
Hum **day** pe binary search karte hain.  
Possible day range: `[min(bloomDay), max(bloomDay)]`.  
Har step pe:
- Assume karte hain ki answer `mid` day hai.
- Check karte hain `canMakeBouquets(mid)` se ki `m` bouquets ban sakte hain ya nahi.
  - `bloomDay` iterate karke `k` adjacent bloomed flowers count karte hain.
  - Agar mil gaye, to `bouquets` increment karte hain aur flowers reset karte hain.
- Agar possible hai, to chhoti day try karte hain (`high = mid-1`), warna badi day (`low = mid+1`).

## Patterns / Concepts
Binary Search on Answer  
Greedy Check  
Search Space Reduction

## Time Complexity
**O(n * log(max(bloomDay)))** — binary search over days and linear scan at each check.

## Space Complexity
**O(1)** — only counters used.

## Example
**Input:**  
`bloomDay = [1,10,3,10,2]`, `m = 3`, `k = 1`

**Output:**  
`3` — minimum day to make 3 bouquets of 1 adjacent flower each.

## Edge Cases
**Edge Case 1:**  
**Input:** `bloomDay = [1,2,4,9,3,4,1]`, `m = 2`, `k = 4`  
**Output:** `-1` (not enough flowers)

**Edge Case 2:**  
**Input:** `bloomDay = [1,1,1,1]`, `m = 1`, `k = 4`  
**Output:** `1`

## Code with Comments
```python
from typing import List

def minDays(bloomDay: List[int], m: int, k: int) -> int:
    # If there are not enough flowers to form m bouquets
    if m * k > len(bloomDay):
        return -1

    # Helper: can we make m bouquets by day?
    def canMakeBouquets(day: int) -> bool:
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

    # Binary search on days
    while low <= high:
        mid = (low + high) // 2
        if canMakeBouquets(mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result
```

# Smallest Divisor Given a Threshold — Binary Search on Answer

## Problem Statement
You are given an integer array `nums` and an integer `threshold`.  
You must choose an integer `divisor` such that the sum of `ceil(nums[i] / divisor)` for all `i` ≤ `threshold`.  
Find the **smallest such divisor**.  

This is a classic **search on answer space** problem — the smaller the divisor, the larger the sum, and vice versa.

## Approach
### English
We binary search on the possible divisor in the range `[1, max(nums)]`.  
At each step:
- Assume `mid` as the current divisor.
- Calculate the sum of ceilings for all elements divided by `mid`.
- If sum ≤ threshold, store `mid` as current best (`k`) and search for a smaller divisor (`high = mid-1`).
- Else, search for a larger divisor (`low = mid+1`).

When the loop ends, `k` holds the smallest valid divisor.

### Hinglish
Hum possible divisor par **binary search** karte hain (`[1, max(nums)]`).  
Har step pe:
- `mid` ko current divisor maante hain.
- Sab elements ko `mid` se divide karke unka ceiling sum nikalte hain.
- Agar sum ≤ threshold hai, to `mid` ko `k` me store karke aur chhota divisor try karte hain (`high = mid-1`).
- Warna bada divisor try karte hain (`low = mid+1`).

Loop ke baad `k` minimum valid divisor hota hai.

## Patterns / Concepts
Binary Search on Answer  
Greedy Check  
Search Space Reduction

## Time Complexity
**O(n * log(max(nums)))** — binary search over divisors and linear scan at each check.

## Space Complexity
**O(1)** — constant space used.

## Example
**Input:**  
`nums = [1,2,5,9]`, `threshold = 6`

**Output:**  
`5` — smallest divisor such that `ceil(1/5) + ceil(2/5) + ceil(5/5) + ceil(9/5) = 6`

## Edge Cases
**Edge Case 1:**  
**Input:** `nums = [1,2,3]`, `threshold = 6`  
**Output:** `1` (dividing by 1 is always valid)

**Edge Case 2:**  
**Input:** `nums = [1000000]`, `threshold = 1`  
**Output:** `1000000` (must divide largest number itself)

## Code with Comments
```python
import math

def smallestDivisor(nums, threshold):
    # Helper: calculate sum of ceilings for a given divisor
    def calculateSum(nums, divisor):
        sum_ = 0
        for number in nums:
            sum_ += math.ceil(number / divisor)
        return sum_

    low = 1
    high = max(nums)
    k = high  # initial answer

    # Binary search on possible divisors
    while low <= high:
        mid = (low + high) // 2
        if calculateSum(nums, mid) <= threshold:
            k = mid  # found a smaller valid divisor
            high = mid - 1
        else:
            low = mid + 1

    return k
```

# Capacity to Ship Packages Within D Days — Binary Search on Answer

## Problem Statement
You are given an array `weights` where `weights[i]` is the weight of the `i-th` package and an integer `days`.  
You must ship all the packages within `days` days.  
You can ship packages in the same order, and on each day you can ship as many packages as you like, as long as the total weight does not exceed the ship’s capacity.

Find the **minimum ship capacity** needed to ship all the packages within `days`.

### Example Question Context
This is a **classic binary search on answer space problem** — as ship capacity increases, required days decrease.  
We need to find the smallest capacity such that all packages can be shipped within `days`.

## Approach / तरीका (English + Hinglish)
### English
We binary search on ship’s capacity in the range `[max(weights), sum(weights)]`:
- For each mid-capacity, use `calculateDays()` to determine how many days it would take.
- If days ≤ given `days`, try a smaller capacity (`high = mid-1`).
- Else, try a larger capacity (`low = mid+1`).

When the loop ends, `ans` is the smallest valid ship capacity.

### Hinglish
Hum ship ki **capacity** par binary search karte hain (`[max(weights), sum(weights)]`):
- Har mid-capacity ke liye `calculateDays()` se check karte hain kitne din lagenge.
- Agar din ≤ given `days`, to chhoti capacity try karte hain (`high = mid-1`).
- Warna badi capacity try karte hain (`low = mid+1`).

Loop ke baad `ans` me minimum valid capacity hoti hai.

## Patterns / Concepts
Binary Search on Answer  
Greedy Check  
Search Space Reduction

## Time Complexity
**O(n * log(sum(weights) - max(weights)))** — binary search over capacities and linear scan at each check.

## Space Complexity
**O(1)** — constant space.

## Example
**Input:**  
`weights = [1,2,3,4,5,6,7,8,9,10]`, `days = 5`

**Output:**  
`15` — minimum ship capacity to deliver all in 5 days.

## Edge Cases
**Edge Case 1:**  
**Input:** `weights = [1,1,1,1]`, `days = 4`  
**Output:** `1`

**Edge Case 2:**  
**Input:** `weights = [10,50,100,100]`, `days = 2`  
**Output:** `150`

## Code with Comments
```python
from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Helper: calculate required days for given capacity
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

        low = max(weights)  # ship must carry at least the heaviest package
        high = sum(weights)  # worst case: all in one day
        ans = high

        # Binary search on capacity
        while low <= high:
            mid = (low + high) // 2
            if calculateDays(weights, mid) <= days:
                ans = mid  # try to minimize
                high = mid - 1
            else:
                low = mid + 1

        return ans
```


# Find K-th Missing Positive Number — Binary Search

## Problem Statement
You are given a **sorted array** `arr` of unique positive integers and an integer `k`.  
You need to find the **k-th missing positive number**.

### Example Question Context
Since the array is strictly increasing and contains positive numbers, the difference between `arr[i]` and `(i+1)` gives the count of missing numbers **before index i**.  
We need to find the smallest index where missing numbers ≥ `k` and calculate the result accordingly.

## Approach / तरीका (English + Hinglish)
### English
We perform binary search on indices `[0, n-1]`:
- For each `mid`, compute how many numbers are missing before `arr[mid]`:  
  `missing = arr[mid] - (mid+1)`
- If `missing < k`, then look in the right half (`low = mid+1`) because we need more missing numbers.
- If `missing ≥ k`, then look in the left half (`high = mid-1`).
- Finally, `high+1+k` (or equivalently `low+k`) gives the k-th missing positive number.

### Hinglish
Hum binary search karte hain index par (`[0, n-1]`):
- Har `mid` par missing numbers nikalte hain:  
  `missing = arr[mid] - (mid+1)`
- Agar `missing < k`, to right half me search karte hain (`low = mid+1`).
- Agar `missing ≥ k`, to left half me search karte hain (`high = mid-1`).
- End me `high+1+k` (ya `low+k`) answer deta hai.

## Patterns / Concepts
Binary Search  
Search Space Reduction  
Counting Missing Elements

## Time Complexity
**O(log n)** — binary search.

## Space Complexity
**O(1)** — constant space.

## Example
**Input:**  
`arr = [2,3,4,7,11]`, `k = 5`

**Output:**  
`9` — the 5-th missing positive number is 9.

## Edge Cases
**Edge Case 1:**  
**Input:** `arr = [1,2,3,4]`, `k = 2`  
**Output:** `6`

**Edge Case 2:**  
**Input:** `arr = [5,6,7,8]`, `k = 1`  
**Output:** `1`

## Code with Comments
```python
def findKthPositive(arr, k):
    n = len(arr)
    low = 0
    high = n - 1

    # Binary search for smallest index where missing numbers ≥ k
    while low <= high:
        mid = (low + high) // 2
        missing = arr[mid] - (mid + 1)

        if missing < k:
            low = mid + 1  # need more missing numbers
        else:
            high = mid - 1  # too many, go left

    # k-th missing positive is before arr[low]
    return low + k
```


# Aggressive Cows — Maximum Minimum Distance (Binary Search)

## Problem Statement
You are given an array `arr` where each element represents a stall position along a straight line, and an integer `cows` representing the number of cows to place.  
Place the cows in the stalls such that the **minimum distance between any two cows is maximized**.  
Return that maximum minimum distance.

### Example Question Context
This is a classic **binary search on answer space** problem.  
We want to maximize the minimum distance between cows, so we check (using greedy) whether it is possible to place all cows with at least `dist` distance apart.

## Approach / तरीका (English + Hinglish)
### English
We binary search on possible minimum distances (`dist`) in range `[0, max(arr)]`:
- Sort the stalls.
- At each step, assume `mid` as the minimum distance.
- Use `canWePlaceCows()` to check if it is possible to place all cows with at least `mid` distance:
  - Place first cow at first stall.
  - For each stall, if the distance from the last placed cow ≥ `mid`, place next cow.
  - If at least `cows` cows are placed, return `True`.
- If possible, try to increase `dist` (`low = mid+1`).
- Else, decrease `dist` (`high = mid-1`).

Finally, `high` holds the maximum minimum distance.

### Hinglish
Hum possible minimum distance (`dist`) par binary search karte hain (`[0, max(arr)]`):
- Pehle stalls ko sort karte hain.
- Har step pe `mid` ko distance assume karke check karte hain:
  - Pehli cow ko pehli stall par rakho.
  - Agli stall tab chunni jab `last placed cow` se distance ≥ `mid` ho.
  - Agar `cows` place ho jayein, to `True` return karo.
- Agar possible ho, to aur bada distance try karo (`low = mid+1`), warna kam karo (`high = mid-1`).

Loop ke baad `high` me answer hota hai.

## Patterns / Concepts
Binary Search on Answer  
Greedy Placement  
Search Space Reduction

## Time Complexity
**O(n * log(max(arr)))** — binary search + linear check each step.

## Space Complexity
**O(1)** — constant space.

## Example
**Input:**  
`arr = [0,3,4,7,10]`, `cows = 4`

**Output:**  
`3` — maximum minimum distance possible is 3.

## Edge Cases
**Edge Case 1:**  
**Input:** `arr = [1,2,3,4,5]`, `cows = 2`  
**Output:** `4`

**Edge Case 2:**  
**Input:** `arr = [0,10]`, `cows = 2`  
**Output:** `10`

## Code with Comments
```python
def canWePlaceCows(arr, dist, cows):
    countCows = 1
    last = arr[0]
    for num in arr:
        if num - last >= dist:
            countCows += 1
            last = num
        if countCows >= cows:
            return True
    return False

def aggresiveCows(arr, cows):
    arr.sort()
    low = 0
    high = max(arr)

    while low <= high:
        mid = (low + high) // 2
        if canWePlaceCows(arr, mid, cows):
            low = mid + 1  # try for bigger distance
        else:
            high = mid - 1  # reduce distance

    return high

# Example call
arr = [0,3,4,7,10]
cows = 4
print(aggresiveCows(arr, cows))  # Output: 3
```
