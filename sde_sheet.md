  

# 1. 🔢 Set Matrix Zeroes
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