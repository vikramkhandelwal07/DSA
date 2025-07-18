### Largest Element in an Array

#### Problem Statement
Given an array of integers, find the **largest element** in the array.

---

#### Approach
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

#### Example
Input:  
`numbers = [1, 2, 3, 4, 7, 9, 1]`

Output:  
`9`

---

#### Code
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

### Second Largest Element in an Array

#### Problem Statement
Given an array of integers, find the **second largest element** in the array.

---

#### Approach
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

#### Example
Input:  
`nums = [1, 9, 2, 8, 4, 7]`

Output:  
`8`

---

#### Code
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

### Rotate Array by `k` Steps (Left Rotation)

#### Problem Statement
Given an array of integers, rotate the array to the left by `k` steps.

---

### Brute Force

#### Approach
**English:**  
- Store the first `k` elements in a temporary array.  
- Shift the remaining `n-k` elements of the original array to the left by `k` places.  
- Copy the stored `k` elements back to the end of the array.

**Hinglish:**  
- Pehle `k` elements ko ek `temp` array me store karlo.  
- Bache hue elements ko `k` jagah left shift kardo.  
- Fir `temp` ke elements ko last me copy kardo.

#### Code
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

### Better

#### Approach
**English:**  
Same logic as brute force but instead of creating a separate variable `j`, we calculate the index directly using `i - (n-d)`.

**Hinglish:**  
Brute force jaisa hi hai lekin ek extra variable `j` lene ki jagah index calculate kar lete hain: `i - (n-d)`.

#### Code
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

### Best

#### Approach
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

#### Code
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
## 5. Move Zeroes to End

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
Input:  
`nums = [1, 0, 1, 0, 3, 12]`  

Output:  
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
## Missing Number in Range [0…n]

### Problem Statement
You’re given an array `nums` of length `n`, containing unique numbers from the range `0` to `n` (inclusive), with exactly one number missing.  
Find the missing number.

---

### Approach 1 — Brute Force  
**Idea:**  
For every number `i` from `0` to `n`, check if `i` is **not in** `nums`.  
Return that number.

**Time Complexity:** O(n²)  
(because `in` on a list is O(n) and runs for `n+1` iterations)  
**Space Complexity:** O(1)

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

Subtract the sum of elements of `nums` from it.  
The difference is the missing number.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

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
## Maximum Consecutive 1’s

### Problem Statement
Given a binary array `nums`, find the maximum number of consecutive `1`s.

---

### Approach 1 — Using Auxiliary List  
**Idea:**  
Traverse `nums`, count consecutive `1`s and append counts to a list `arr`.  
At the end, return `max(arr)`.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

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

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

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

## Single Number (XOR)

### Problem Statement
Given an integer array `nums` where every element appears **twice except for one**, find that single one.

---

### Approach — XOR  
**Idea:**  
- XOR of a number with itself is `0` (`a ^ a = 0`)
- XOR of a number with `0` is the number itself (`a ^ 0 = a`)
- So, XOR all elements. The duplicates cancel out and leave the unique number.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

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
