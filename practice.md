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

## Tuples

A tuple in Python is similar to a list. The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas we can change the elements of a list.

In short, a tuple is an immutable list. A tuple can not be changed in any way once it is created.

Characterstics

- Ordered
- Unchangeble
- Allows duplicate

```python

# tuple unpacking
a,b,c = (1,2,3)
print(a,b,c)
--->
a,b,*others = (1,2,3,4)
print(a,b)
print(others)
--->
# zipping tuples
a = (1,2,3,4)
b = (5,6,7,8)

tuple(zip(a,b))
--------------------------------
output : ((1, 5), (2, 6), (3, 7), (4, 8))
```
---

## Sets

A set is an unordered collection of items. Every set element is unique (no duplicates) and must be immutable (cannot be changed).

However, a set itself is mutable. We can add or remove items from it.

Sets can also be used to perform mathematical set operations like union, intersection, symmetric difference, etc.

Characterstics:

- Unordered
- Mutable
- No Duplicates
- Can't contain mutable data types.

```python
S = {1,2,3,4}
# add
S.add(5)
---------->
output: {1, 2, 3, 4, 5}

S.update([5,6,7])
print(S)
---------->
output :{1, 2, 3, 4, 5, 6, 7}

s = {1, 2, 3, 4, 5}
s.discard(3)  # Removes 3 from the set
print(s)  # Output: {1, 2, 4, 5}

s.discard(6)  # Does nothing, as 6 is not in the set
print(s)  # Output: {1, 2, 4, 5}

```

`Comparing remove() and discard()`:

The main difference between remove() and discard() is how they handle cases where the element is not found in the set. discard() does nothing, while remove() raises an error.
Choose discard() when you want to avoid potential errors if the element might not be present.
Choose remove() when you want to be notified of errors if the element is not found.

```python
s = {1, 2, 3, 4, 5}
element = s.pop()  # Removes and returns a random element (e.g., 3)
print(element)  # Output: 3 (or any other element from the set)
print(s)  # Output: {1, 2, 4, 5} (or the set without the popped element)

s.clear()  # Empties the set
s.pop()  # Raises KeyError, as the set is now empty

```

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union
union_set_symbol = set1 | set2
union_set_word = set1.union(set2)
print("Union:", union_set_symbol)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
print("Union:", union_set_word)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}


# Intersection
intersection_set_symbol = set1 & set2
intersection_set_word = set1.intersection(set2)
print("Intersection:", intersection_set_symbol)  # Output: {4, 5}
print("Intersection:", intersection_set_word)  # Output: {4, 5}


# Difference
difference_set_symbol = set1 - set2
difference_set_word = set1.difference(set2)
print("Difference (set1 - set2):", difference_set_symbol)  # Output: {1, 2, 3}
print("Difference (set1 - set2):", difference_set_word)  # Output: {1, 2, 3}

difference_set2_symbol = set2 - set1
difference_set2_word = set2.difference(set1)
print("Difference (set2 - set1):", difference_set2_symbol)  # Output: {8, 6, 7}
print("Difference (set2 - set1):", difference_set2_word)  # Output: {8, 6, 7}


# Symmetric Difference
symmetric_difference_set_symbol = set1 ^ set2
symmetric_difference_set_word = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_difference_set_symbol)  # Output: {1, 2, 3, 6, 7, 8}
print("Symmetric Difference:", symmetric_difference_set_word)  # Output: {1, 2, 3, 6, 7, 8}

```

---

## Dictionary

Dictionary in Python is a collection of keys values, used to store data values like a map, which, unlike other data types which hold only a single value as an element.

In some languages it is known as map or assosiative arrays.

dict = { 'name' : 'Vikram' , 'age' : 13 , 'gender' : 'male' }

Characterstics:

- Mutable
- Indexing has no meaning
- keys can't be duplicated
- keys can't be mutable items.
  
## functions in dictionary

.get()

### dictionary comprehension

### "{`key:value` for `vars` in `iterable`}"

```python
# using zip
days = ["Sunday", "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
temp_C = [30.5,32.6,31.8,33.4,29.8,30.2,29.9]

{i:j for (i,j) in zip(days,temp_C)}
----------------->
output:{'Sunday': 30.5,
 'Monday': 32.6,'Tuesday': 31.8,'Wednesday': 33.4,
 'Thursday': 29.8,'Friday': 30.2,'Saturday': 29.9}

```