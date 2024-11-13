# Python Coding Revision

## `in` / `not in` Operators

These operators are used to check the presence of an element in a collection (e.g., list, string, tuple, etc.).

### Example

```python
# Checking if a character is not in a string
print('D' not in 'Delhi')  # Output: False

# Checking if an element is in a list
print(1 in [2, 3, 4, 5, 6])  # Output: False
```

---

```python
help(modules)
```

---

### `Problem 3`:Write a program to print the following pattern

         *
       * * *
     * * * * *

```python
# Define the number of rows (height of the pattern)
n = 5

# Loop to print the rows
for i in range(1, n + 1):

    # Print leading spaces to center the stars
    print(" " * (n - i), end="")

    # Print the stars for the current row
    print("* " * (2 * i - 1))
```

### `Problem 8`: Write a program to print all the unique combinations of 1,2,3 and 4

`Output`:

```
1 2 3 4
1 2 4 3
1 3 2 4
1 3 4 2
1 4 2 3
1 4 3 2
2 1 3 4
2 1 4 3
2 3 1 4
2 3 4 1
2 4 1 3
.
.
and so on
```

```python
def generate_permutations(arr, start, end):
    if start == end:
        print(" ".join(map(str, arr)))
    else:
       
        for i in range(start, end + 1):
            arr[start], arr[i] = arr[i], arr[start]
            generate_permutations(arr, start + 1, end)
            arr[start], arr[i] = arr[i], arr[start]

numbers = [1, 2, 3, 4]
generate_permutations(numbers, 0, len(numbers) - 1)
```

```python
import itertools

# Given list of numbers
numbers = [1, 2, 3, 4]

# Generate all unique permutations
permutations = itertools.permutations(numbers)

# Print each permutation in the required format
for perm in permutations:
    print(" ".join(map(str, perm)))
```

---
`Strings` in Python are immutable.

can `delete` a complete string but not a part of it.
thankyou
