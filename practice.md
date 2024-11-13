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

```echo
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

## `Strings`

`Strings` in Python are immutable.

- can `delete` a complete string but not a part of it.
- can traverse a string.

## Common Functions

- len("hello world")
- max
- min
- sorted("hello world",reverse=True)

- .capitalize()
- .title()
- .upper()
- .Lower()
- .Swapcase()
- .count("ch to found")
- .find("ch to find return 1st index or -1")
- .index("letter jiska index find karna hai")
- .endswith()
- .startswith()
- .isalnum()
- .isalpha()
- .isdigit()
- .isidentifier()
- .split() eg:'hi my name is nitish'.split()
- .join() eg:" ".join(['hi', 'my', 'name', 'is', 'nitish'])
- .replace("jisko change karna hai ","jisse change karna hai")
- .strip() :used to remove uneccesary spaces
-

---

## `List`

## Characterstics of a List

- Ordered
- Changeble/Mutable
- Hetrogeneous
- Can have duplicates
- are dynamic
- can be nested
- items can be accessed
- can contain any kind of objects in python

## Common Functions for list

- .append()
- .extend()

```python

L = [1,2,3,4,5]
L.extend('delhi')
print(L)
```

[1, 2, 3, 4, 5, 'd', 'e', 'l', 'h', 'i']

---

- .insert(kidhar,kya)
- .del(index)
- .remove(jo nikalna hai)
- del is used when you know the index of the item to be removed, while remove() is used when you know the value of the item to be removed.
- .pop()  //deletes last item
- .clear() //pura saaf hojayega

```python
# len/min/max/sorted
L = [2,1,5,7,0]

print(len(L))
print(min(L))
print(max(L))
print(sorted(L,reverse=True))
```

- .count(number jo count karwna hai)
- .index(jiska index chahiye)
- .reverse()
- .sort()
- sorted(list ka naam)
  - Use sort() when you want to modify the original list directly.
    Use sorted() when you want to keep the original list unchanged and obtain a new sorted list.

---
List Comprehension
List Comprehension provides a concise way of creating lists.

newlist = [expression `for` item `in` iterable `if` condition == `True`]

expression - kya karna hai
iterable - eg:range(1,11) etc

## 2 ways to traverse a list

- itemwise
- indexwise

```python
# itemwise
L = [1,2,3,4]

for i in L:
  print(i)
```

```python
# indexwise
L = [1,2,3,4]

for i in range(0,len(L)):
  print(L[i])
```

```python
L1 = [1,2,3,4]
L2 = [-1,-2,-3,-4]

list(zip(L1,L2)) 

[i+j for i,j in zip(L1,L2)]

```

---
