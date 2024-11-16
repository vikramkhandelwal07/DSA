
## `Hashing`:

```python

def get_integer_input(prompt):
    return int(input(prompt))

def get_list_input(prompt, size):
    return [int(num) for num in input(prompt).split()]

n = get_integer_input("Enter the size of the array: ")
arr = get_list_input(f"Enter {n} integers separated by spaces: ", n)

hash_map = [0] * 13
for num in arr:
    if 0 <= num <= 12:
        hash_map[num] += 1

q = get_integer_input("Enter the number of queries: ")

for i in range(q):
    number = get_integer_input(f"Query {i+1}: Enter a number to check its frequency: ")
    if 0 <= number <= 12:
        print(f"Frequency of {number}: {hash_map[number]}")
    else:
        print(f"Frequency of {number}: 0")

print("Program completed.")
```

---

## character hashing

