## Question: Linked List Implementation

### Problem Statement
Implement a basic singly linked list in Python with operations like:
- Convert array to linked list
- Display linked list
- Find length
- Search an element
- Insert at head, tail, k-th position, or before a given value
- Delete head, tail, k-th element, or a node by value

---

### Approach

**English:**  
We define a `Node` class to represent each element in the linked list. Using this, we perform all common linked list operations such as insertion, deletion, and traversal.

**Hinglish:**  
Hum `Node` class banate hain jo linked list ka basic block hota hai. Phir isse use karke hum insertion, deletion aur traversal jaise operations implement karte hain.

---

### Example

**Input:**  
Operations like:  
- Convert `[1, 2, 3]` into a linked list  
- Insert `4` at head  
- Delete element with value `2`  
- Find length  

**Output:**  
Modified list structure displayed with arrows (`->`), and values like `Length = 3`, `Found = True` etc.

---

### Code
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def array_to_linkedlist(array):
    if not array:
        return None
    head = Node(array[0])
    current = head
    for value in array[1:]:
        current.next = Node(value)
        current = current.next
    return head

def display_linkedlist(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next

def lengthofLinkedList(head):
    cnt = 0
    current = head
    while current:
        current = current.next
        cnt += 1
    return cnt

def searchInLinkedList(element):
    current = head
    while current:
        if current.value == element:
            return True
        current = current.next
    return False 

def delete_head(head):
    if not head:
        print("The linked list is already empty.")
        return None
    new_head = head.next
    head.next = None
    return new_head  

def delete_tail(head):
    if not head:
        print("The linked list is already empty.")
        return None
    if not head.next:
        del head
        return None
    current = head
    while current.next and current.next.next:
        current = current.next
    del current.next
    current.next = None
    return head

def delete_kth_element(head, k):
    if not head:
        print("The linked list is empty.")
        return None
    if k == 1:
        new_head = head.next
        del head
        return new_head
    current = head
    count = 1
    while current and count < k - 1:
        current = current.next
        count += 1
    if current and current.next:
        node_to_delete = current.next
        current.next = current.next.next
        del node_to_delete
    return head

def delete_value(head, value):
    if not head:
        print("The linked list is empty.")
        return None
    if head.value == value:
        new_head = head.next
        del head
        return new_head
    current = head
    while current.next:
        if current.next.value == value:
            node_to_delete = current.next
            current.next = current.next.next
            del node_to_delete
            return head
        current = current.next
    print(f"Value {value} not found in the list.")
    return head

def insert_at_head(head, value):
    new_node = Node(value)
    new_node.next = head
    return new_node

def insert_at_tail(head, value):
    new_node = Node(value)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

def insert_at_k(head, value, k):
    new_node = Node(value)
    if k == 0:
        new_node.next = head
        return new_node
    current = head
    count = 0
    while current and count < k - 1:
        current = current.next
        count += 1
    if not current:
        return head
    new_node.next = current.next
    current.next = new_node
    return head

def insert_before_x(head, x, value):
    new_node = Node(value)
    if not head:
        return new_node
    if head.value == x:
        new_node.next = head
        return new_node
    current = head
    while current.next and current.next.value != x:
        current = current.next
    if current.next:
        new_node.next = current.next
        current.next = new_node
    return head
```

---

## Question: Doubly Linked List Implementation

### Problem Statement
Implement a basic **Doubly Linked List** in Python with operations like:
- Convert array to doubly linked list
- Display list
- Insert at head, tail, k-th position, or before a value
- Delete head, tail, k-th element, or a node by reference

---

### Approach

**English:**  
We define a `Node` class with `value`, `next`, and `prev` pointers. Using it, we create a doubly linked list and perform insertions and deletions at various positions.  
- Each node connects both to its previous and next node.  
- This allows traversal in both directions and easier deletion.

**Hinglish:**  
Hum `Node` class banate hain jisme `value`, `next` aur `prev` hote hain. Isse hum doubly linked list banate hain jisme har node apne aage aur peeche ke node se connected hoti hai.  
- Ye structure insertion aur deletion ko efficient banata hai.  
- Hum head, tail, kth position aur kisi value ke pehle bhi insert/delete kar sakte hain.

---

### Example

**Input:**  
Operations like:  
- Convert `[1, 2, 3]` into DLL  
- Insert `4` at position 2  
- Delete element at position 3  
- Display list  

**Output:**  
Formatted list like `1 <-> 4 <-> 2 <-> 3`  
and values like `Head deleted`, `Value not found` etc.

---

### Code
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

def print_list(head):
    current = head
    while current:
        print(f"{current.value}", end=" <-> " if current.next else "")
        current = current.next
    print()

def arrayToLl(array):
    if not array:
        return None
    head = Node(array[0])
    current = head
    for number in array[1:]:
        new_node = Node(number)
        current.next = new_node
        new_node.prev = current
        current = new_node
    return head  

def deleteHead(head):
    if not head:
        return None
    if head.next is None:
        del head
        return None
    new_head = head.next  
    new_head.prev = None  
    del head 
    return new_head

def deleteTail(head):
    if not head:
        return None
    if head.next is None:
        del head
        return None
    current = head
    while current.next:
        current = current.next 
    current.prev.next = None
    del current
    return head

def deleteKthElement(head, k):
    if not head or k < 1:
        return head
    if k == 1:
        return deleteHead(head)
    current = head
    count = 1
    while current and current.next:
        current = current.next
        count += 1
    if k == count:
        return deleteTail(head)
    current = head
    count = 1
    while current and count < k:
        current = current.next
        count += 1
    if not current:
        return head
    if current.prev:
        current.prev.next = current.next
    if current.next:
        current.next.prev = current.prev
    del current
    return head

def removeNode(node):
    if not node:
        return
    if not node.prev and not node.next:
        del node
        return
    if not node.prev:
        node.next.prev = None
        del node
        return
    if not node.next:
        node.prev.next = None
        del node
        return
    node.prev.next = node.next
    node.next.prev = node.prev
    del node

def insertAtHead(head, value):
    new_node = Node(value)
    if not head:
        return new_node
    new_node.next = head
    head.prev = new_node
    return new_node

def insertAtTail(head, value):
    new_node = Node(value)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    new_node.prev = current
    return head

def insertAtK(head, value, k):
    if k <= 1:
        return insertAtHead(head, value)
    new_node = Node(value)
    current = head
    count = 1
    while current and count < k - 1:
        current = current.next
        count += 1
    if not current:
        return insertAtTail(head, value)
    new_node.next = current.next
    new_node.prev = current
    if current.next:
        current.next.prev = new_node
    current.next = new_node
    return head

def insertBeforeX(head, value, x):
    new_node = Node(value)
    if not head:
        return new_node
    if head.value == x:
        return insertAtHead(head, value)
    current = head
    while current and current.value != x:
        current = current.next
    if not current:
        print(f"Value {x} not found in the list.")
        return head
    new_node.next = current
    new_node.prev = current.prev
    if current.prev:
        current.prev.next = new_node
    current.prev = new_node
    return head
```

---

## Question: Find Middle Element of Linked List (Optimal)

### Problem Statement
Given the head of a singly linked list, return the **middle element's value**.  
If the list has an even number of elements, return the **second** middle.

---

### Approach

**English:**  
We use the **two-pointer technique**:  
- Initialize both `slow` and `fast` pointers at the head.  
- Move `slow` one step and `fast` two steps at a time.  
- When `fast` reaches the end, `slow` will be at the middle.  
This approach works in **O(n)** time and **O(1)** space.

**Hinglish:**  
Hum **slow aur fast pointer** use karte hain:  
- `slow` ek step chalta hai aur `fast` do step.  
- Jab `fast` end tak pahuchta hai, `slow` middle node pe hota hai.  
Iska time complexity **O(n)** hai aur space **O(1)**.

---

### Example

**Input:**  
`Linked List: 1 -> 2 -> 3 -> 4 -> 5`  
**Output:**  
`3`

**Input:**  
`Linked List: 10 -> 20 -> 30 -> 40`  
**Output:**  
`30` (second middle)

---

### Code
```python
def findMiddleOptimal(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.value
```

---

## Question: Reverse a Singly Linked List

### Problem Statement
Given the head of a singly linked list, reverse the list and return the **new head**.

---

### Approach

**English:**  
We maintain three pointers:  
- `current` to track the current node,  
- `prev` to track the previous node (initially `None`),  
- `front` to preserve the next node before reversing.  
At each step, we **reverse the `.next` pointer** of the current node and move forward.

**Hinglish:**  
Hum teen pointer rakhte hain:  
- `current` current node ke liye,  
- `prev` previous node ke liye (initially `None`),  
- `front` next node ko temporarily store karne ke liye.  
Har step par hum `.next` pointer ko reverse karte hain aur aage badhte hain.

---

### Example

**Input:**  
`Linked List: 1 -> 2 -> 3 -> 4`  
**Output:**  
`4 -> 3 -> 2 -> 1`

---

### Code
```python
def reverseLinkedList(head):
    current = head
    prev = None
    while current:
        front = current.next
        current.next = prev
        prev = current
        current = front
    return prev
```

---

## Question: Reverse a Doubly Linked List

### Problem Statement
Given the head of a **doubly linked list**, reverse the list in-place and return the new head.

---

### Approach

**English:**  
We iterate through the list, and for each node:
- Swap its `.prev` and `.next` pointers.
- Move to the next node using the updated `.prev` pointer (since we reversed them).
At the end, `last.prev` will be the **new head**.

**Hinglish:**  
Har node par hum:
- Uska `.prev` aur `.next` swap kar dete hain.
- Naye `.prev` (jo pehle `.next` tha) se aage badhte hain.
Akhri mein `last.prev` hi hamara **naya head** hota hai.

---

### Example

**Input:**  
`1 <-> 2 <-> 3 <-> 4`  
**Output:**  
`4 <-> 3 <-> 2 <-> 1`

---

### Code
```python
def reverseDLL(head):
    if head is None or head.next is None:
        return head
    current = head
    last = None
    while current:
        last = current.prev
        current.prev = current.next
        current.next = last
        current = current.prev
    return last.prev
```
---

## Question: Detect Cycle in a Singly Linked List

### Problem Statement
Given the `head` of a singly linked list, determine if the linked list contains a **cycle**.

---

### Approach 1: Using Hashing (Visited Set)

**English:**  
We maintain a dictionary (`visited_nodes`) to track all visited nodes.  
- If we visit a node that is already in the dictionary, a cycle exists.  
- Else, we store the node and move forward.

**Hinglish:**  
Hum ek dictionary use karte hain taaki har node ko track karein.  
- Agar koi node dobara mile, to cycle hai.  
- Nahi to us node ko dictionary mein store karke aage badhte hain.

---

### Code (Approach 1)
```python
def hasCycle(head):
    visited_nodes = {}
    current = head

    while current:
        if current in visited_nodes:
            return True
        visited_nodes[current] = True
        current = current.next

    return False
```

---

### Approach 2: Floyd’s Cycle Detection (Tortoise & Hare)

**English:**  
We use two pointers – `slow` and `fast`.  
- `slow` moves one step, `fast` moves two.  
- If there's a cycle, they will eventually meet.

**Hinglish:**  
Do pointers lete hain – `slow` aur `fast`.  
- `slow` ek step, `fast` do steps chalta hai.  
- Agar cycle hai to dono kisi point par takraenge.

---

### Code (Approach 2)
```python
def isCycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
```
---

## Question: Detect the Starting Point and Length of a Cycle in a Singly Linked List

### Problem Statement
Given the `head` of a singly linked list that contains a **cycle**, determine:
1. The **starting node** of the cycle.
2. The **length** of the cycle.

---

### Part 1: Finding the Starting Point of the Cycle

**English:**  
Use Floyd’s cycle detection method.  
- After `slow` and `fast` meet, reset `slow` to the head.  
- Move both `slow` and `fast` one step at a time.  
- The node where they meet again is the start of the loop.

**Hinglish:**  
Floyd's algorithm lagate hain.  
- Jab `slow` aur `fast` mil jaayein, tab `slow` ko head se dobara chalu karte hain.  
- Dono ek-ek step chalte hain.  
- Jahan phir se milte hain, wahi cycle ka starting node hai.

#### Code
```python
def startingPoint(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None
```

---

### Part 2: Finding the Length of the Cycle

**English:**  
Once `slow` and `fast` meet, start counting steps from that point until the loop is completed.

**Hinglish:**  
Jab `slow` aur `fast` milte hain, tab se count karna start karo jab tak `fast` fir se `slow` ke paas na aa jaye.

#### Code
```python
def findLengthOfLoop(head):
    fast = head
    slow = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            length = 1
            fast = fast.next
            while slow != fast:
                fast = fast.next
                length += 1
            return length
    return 0
```
---

## Question: Check if a Singly Linked List is a Palindrome

### Problem Statement
Given the `head` of a singly linked list, determine whether the list is a **palindrome** (i.e., it reads the same forward and backward).

---

### Approach

This approach uses **O(n) time** and **O(1) space**.

#### Step-by-step:

**Step 1: Find the middle of the linked list**  
Use two pointers, `slow` and `fast`.  
- `slow` moves one step, `fast` moves two steps.  
- When `fast` reaches the end, `slow` will be at the middle.

**Step 2: Reverse the second half**  
From the middle node onwards, reverse the linked list.

**Step 3: Compare both halves**  
Compare values from the start and from the reversed second half.  
- If all nodes match, it's a palindrome.

---

### Code
```python
def isPalindrome(head):
    if not head or not head.next:
        return True  # A single node or empty list is always a palindrome

    # Step 1: Find the middle of the linked list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the list
    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp

    # Step 3: Compare the two halves
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True
```

---

### Notes
- This method **does not restore** the original linked list.  
- If restoring is required, reverse the second half again after the comparison.

---

## Question: Reorder Linked List by Odd and Even Indices

### Problem Statement
Given the `head` of a singly linked list, group all nodes positioned at **odd indices** together followed by the nodes at **even indices**.  
Return the reordered linked list.

> **Note**: The relative order within the odd and even groups should remain the same. Indexing is **1-based** (i.e., first node is index 1, second is index 2, etc.).

---

### Approach

This algorithm rearranges the list in **O(n)** time with **O(1)** space.

#### Step-by-step:

1. **Initialize Pointers**:
   - `odd` points to the first node.
   - `even` points to the second node.
   - `even_head` stores the starting point of even-indexed nodes to attach later.

2. **Traverse and Rearrange**:
   - While `even` and `even.next` exist:
     - Point `odd.next` to the next odd node (`even.next`).
     - Move `odd` forward.
     - Point `even.next` to the next even node (`odd.next`).
     - Move `even` forward.

3. **Link Final Nodes**:
   - Connect the end of the odd-indexed list to `even_head`.

---

### Code
```python
def oddEvenList(head):
    if not head or not head.next:
        return head

    odd = head
    even = head.next
    even_head = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    odd.next = even_head

    return head
```

---

### Notes
- The reordering is done **in-place**.
- The function maintains the relative ordering of nodes within the odd and even index groups.

---

## Question: Remove Nth Node from End of Linked List

### Problem Statement
Given the `head` of a singly linked list and an integer `n`, remove the **n-th node from the end** of the list and return its head.

---

### Approach

This uses the **two-pointer technique** with a **dummy node** to handle edge cases easily (like deleting the head node).

#### Step-by-step:

1. **Initialize a Dummy Node**:
   - `dummy` is a new node pointing to the head, to handle edge cases smoothly.

2. **Advance the First Pointer**:
   - Move `first` pointer `n + 1` steps ahead so there is a gap of `n` nodes between `first` and `second`.

3. **Advance Both Pointers**:
   - Move both `first` and `second` one step at a time until `first` reaches the end.
   - Now, `second` is at the node **just before** the one to be removed.

4. **Delete the Node**:
   - Modify `second.next` to skip the node to be deleted.

5. **Return**:
   - Return `dummy.next` as the new head of the modified list.

---

### Code
```python
def removeNthFromEnd(head, n):
    dummy = Node(0)
    dummy.next = head
    first = dummy
    second = dummy

    for _ in range(n + 1):
        first = first.next

    while first:
        first = first.next
        second = second.next

    second.next = second.next.next
    return dummy.next
```

---

### Notes
- Handles edge cases like removing the first node or when the list has only one node.
- Time Complexity: **O(n)**  
- Space Complexity: **O(1)**

---

## Question: Delete the Middle Node of a Linked List

### Problem Statement
Given the `head` of a singly linked list, **delete the middle node** and return the modified list.  
If the list has only one node, return `None`.

---

### Approach

This uses the **slow and fast pointer** technique to find the middle node in a single pass.

#### Step-by-step:

1. **Edge Case**:
   - If list is empty or has only one node, return `None`.

2. **Initialize Pointers**:
   - `slow` moves one step, `fast` moves two steps.
   - `prev` keeps track of the node before `slow`.

3. **Traverse the List**:
   - When `fast` reaches the end, `slow` will be at the middle.
   - `prev` will be just before the middle node.

4. **Delete the Middle**:
   - Set `prev.next = slow.next` to remove the middle node.

---

### Code
```python
def deleteMiddle(head):
    if head is None or head.next is None:
        return None  # No middle to delete

    slow, fast, prev = head, head, None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = slow.next
    return head
```

---

### Notes
- Time Complexity: **O(n)**  
- Space Complexity: **O(1)**
- Efficient one-pass algorithm with no extra data structures.

---
### Problem: Sort a Linked List

---

#### 1. Brute-force Approach

```python
def sortLinkedList(head):
    current = head
    array = []
    while current:
        array.append(current.value)
        current = current.next
    
    array = sorted(array)
    current = head
    for num in array:
        current.value = num
        current = current.next
    
    return head
```

**Approach:**  
- Traverse the linked list and store its elements in an array.
- Sort the array using Python’s built-in sorting.
- Traverse the list again and overwrite node values with sorted ones.

**Time Complexity:** O(n log n)  
**Space Complexity:** O(n)  

---

#### 2. Optimal Approach – Merge Sort on Linked List

**a. Finding Middle of the List**

```python
def findMiddle(head):
    slow, fast = head, head
    prev = None  
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    if prev:
        prev.next = None  # Split the list into two halves
    return slow
```

**b. Merging Two Sorted Linked Lists**

```python
def mergeTwoSortedLinkedLists(list1, list2):
    dummyNode = Node(-1)
    temp = dummyNode

    while list1 and list2:
        if list1.data <= list2.data:
            temp.next = list1
            list1 = list1.next
        else:
            temp.next = list2
            list2 = list2.next
        temp = temp.next

    temp.next = list1 if list1 else list2
    return dummyNode.next
```

**c. Recursive Merge Sort on Linked List**

```python
def SortedListMergeSort(head):
    if not head or not head.next:
        return head

    middle = findMiddle(head)
    leftHalf = SortedListMergeSort(head)
    rightHalf = SortedListMergeSort(middle)

    return mergeTwoSortedLinkedLists(leftHalf, rightHalf)
```

**Approach:**  
- Use the slow-fast pointer method to find the middle.
- Recursively divide the list into halves.
- Merge the sorted halves using two-pointer technique.

**Time Complexity:** O(n log n)  
**Space Complexity:** O(log n) (recursive stack)  

---

**Input Format:**  
- A singly linked list `head` containing integers.

**Output Format:**  
- The same linked list sorted in ascending order.

---

### Problem: Sort a Linked List using Merge Sort

#### 🧠 Problem Statement:
Given the head of a singly linked list, sort the list in **ascending order** using **merge sort** algorithm.  
Your algorithm should have a time complexity of *O(n log n)* and must use constant space complexity (i.e., not creating new nodes for sorting).

---

### ✅ Brute Force Approach

#### 🔸Approach:
- Traverse the list and store the values in an array.
- Sort the array using Python's built-in sort.
- Traverse the list again and update node values using sorted array.

#### 🔸Code:
```python
def sortList(head):
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next

    arr.sort()
    current = head
    i = 0
    while current:
        current.val = arr[i]
        i += 1
        current = current.next
    return head
```

#### ⏱️ Time Complexity: O(n log n)  
#### 📦 Space Complexity: O(n)  

---

### 🚀 Optimal Approach (Using Merge Sort)

#### 🔸Step 1: Find the middle of the list
```python
def getMid(head):
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

#### 🔸Step 2: Merge two sorted lists
```python
def merge(left, right):
    dummy = ListNode()
    tail = dummy

    while left and right:
        if left.val <= right.val:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next

    if left:
        tail.next = left
    else:
        tail.next = right

    return dummy.next
```

#### 🔸Step 3: Main merge sort function
```python
def sortList(head):
    if not head or not head.next:
        return head

    mid = getMid(head)
    right_head = mid.next
    mid.next = None

    left = sortList(head)
    right = sortList(right_head)

    return merge(left, right)
```

#### ⏱️ Time Complexity: O(n log n)  
#### 📦 Space Complexity: O(log n) (due to recursive stack)

---

### 🧪 Input:
Linked List: 4 → 2 → 1 → 3

### ✅ Output:
1 → 2 → 3 → 4

---

### Problem: Intersection Point in Y Shaped Linked Lists

#### 🧠 Problem Statement:
Given two singly linked lists that intersect at some point, find the node at which they intersect. The linked lists are **not cyclic** and have nodes that may or may not merge at some node onward.

You must **not modify** the original lists and **not use extra space for node copying**. Return the reference to the **intersection node**, or `None` if no intersection exists.

---

### ✅ Hashing-Based Approach

#### 🔸Approach:
- Use two hash maps to store visited nodes from both lists.
- Traverse both lists simultaneously and mark nodes in hash maps.
- If any node from one list is found in the hash map of the other, that’s the intersection point.
- Continue traversal until one or both pointers reach the end.

---

#### 🔸Code:
```python
def getIntersectionNode(headA, headB):
    hashA = {}
    hashB = {}
    one = headA
    two = headB

    while one and two:
        if one in hashB:
            return one
        hashA[one] = one.val
        if two in hashA:
            return two
        hashB[two] = two.val
        one = one.next
        two = two.next

    while one:
        if one in hashB:
            return one
        hashA[one] = one.val
        one = one.next

    while two:
        if two in hashA:
            return two
        hashB[two] = two.val
        two = two.next

    return None
```

---

#### ⏱ Time Complexity:
- **O(M + N)**  
Where M and N are the lengths of the two linked lists.

#### 💾 Space Complexity:
- **O(M + N)**  
Two hash maps are used for storing the nodes from both lists.

---

#### 🧪 Input:
List A: `1 -> 2 -> 3 -> 4 -> 5`  
List B: `9 -> 4 -> 5` *(4 and 5 are shared nodes)*

#### ✅ Output:
Returns reference to node with value `4`

---

### Problem: Add 1 to a Number Represented as a Linked List

#### 🧠 Problem Statement:
Given a singly linked list where each node contains a single digit, the digits represent a number in **forward order** (most significant digit comes first). Your task is to **add 1** to the number and return the head of the updated linked list.

Example:
- Input: `1 -> 9 -> 9`
- Output: `2 -> 0 -> 0`

---

### ✅ Reversal + Carry Handling Approach

#### 🔸Approach:
1. **Reverse** the linked list to simplify addition from least significant digit.
2. Traverse the list and **add 1** to the number using a carry.
3. If carry is left after reaching the end, create a **new node**.
4. **Reverse** the list again to return it in correct order.

---

#### 🔸Code:
```python
def addOne(head):
    # Helper function to reverse a linked list
    def reversell(head):
        if not head or not head.next:
            return head
        current = head
        prev = None 
        while current:
            front = current.next
            current.next = prev
            prev = current
            current = front
        return prev

    # Step 1: Reverse the linked list
    head = reversell(head)

    # Step 2: Add one to the reversed list
    carry = 1
    current = head
    while current or carry:
        current.data += carry
        carry = current.data // 10
        current.data %= 10
        if not current.next and carry > 0:
            current.next = Node(carry)
            carry = 0
        current = current.next

    # Step 3: Reverse the list back to its original order
    head = reversell(head)
    
    return head
```

---

#### ⏱ Time Complexity:
- **O(N)** — Each node is visited thrice (two reversals and one addition pass)

#### 💾 Space Complexity:
- **O(1)** — No extra space used except pointers (in-place operation)

---

#### 🧪 Example:
**Input**:  
`1 -> 9 -> 9`  
**Output**:  
`2 -> 0 -> 0`

---

### Problem: Add Two Numbers Represented by Linked Lists

#### 🧠 Problem Statement:
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each node contains a single digit. Add the two numbers and return the sum as a linked list.

Example:
- Input:  
  `l1 = 2 -> 4 -> 3`  
  `l2 = 5 -> 6 -> 4`  
- Output:  
  `7 -> 0 -> 8`  
  Explanation: 342 + 465 = 807

---

### ✅ Carry-based Traversal Approach

#### 🔸Approach:
- Initialize a dummy node to simplify result construction.
- Use a carry to store sums > 9.
- Traverse both linked lists until all digits and carry are processed.
- Create a new node for each digit of the sum and link it.

---

#### 🔸Code:
```python
def addTwoNumbers(l1, l2):
    dummyNode = Node(-1)
    current = dummyNode
    carry = 0

    while l1 or l2 or carry:
        sum = carry
        if l1:
            sum += l1.value
            l1 = l1.next
        if l2:
            sum += l2.value
            l2 = l2.next
        
        carry = sum // 10
        new_node = Node(sum % 10)
        current.next = new_node
        current = current.next

    return dummyNode.next
```

---

#### ⏱ Time Complexity:
- **O(max(N, M))** — N and M are the lengths of `l1` and `l2`

#### 💾 Space Complexity:
- **O(max(N, M))** — For storing the result linked list

---

#### 🧪 Example:
**Input**:  
`l1 = 2 -> 4 -> 3`  
`l2 = 5 -> 6 -> 4`  

**Output**:  
`7 -> 0 -> 8`  

---

### Problem: Delete All Occurrences of a Key in a Doubly Linked List

#### 🧠 Problem Statement:
Given a doubly linked list and a key, delete **all occurrences** of the given key from the list.

Example:  
- Input: `10 <-> 20 <-> 30 <-> 20 <-> 40`, key = `20`  
- Output: `10 <-> 30 <-> 40`

---

### ✅ Two-Pointer Traversal Approach

#### 🔸Approach:
- Traverse the list node by node.
- If the current node’s value matches the key:
  - Rewire the `prev` and `next` pointers to exclude the current node.
  - Update `head` if the deleted node was the head.

---

#### 🔸Code:
```python
def deleteAllOccurrences(head, key):
    curr = head
    while curr:
        if curr.val == key:
            if curr.prev:
                curr.prev.next = curr.next
            else:
                head = curr.next  # Update head if first node is deleted
            if curr.next:
                curr.next.prev = curr.prev
        curr = curr.next

    return head
```

---

#### ⏱ Time Complexity:
- **O(N)** — Each node is visited once

#### 💾 Space Complexity:
- **O(1)** — No extra space used

---

#### 🧪 Example:
**Input**:  
`head = 1 <-> 2 <-> 3 <-> 2 <-> 4`, key = `2`

**Output**:  
`1 <-> 3 <-> 4`

---

### Problem: Find Pairs with Given Sum in Doubly Linked List

#### 🧠 Problem Statement:
Given a **sorted doubly linked list**, find **all pairs of nodes** whose sum equals a given `target`.

Example:  
- Input: `1 <-> 2 <-> 4 <-> 5 <-> 6 <-> 8 <-> 9`, target = `7`  
- Output: `[[1, 6], [2, 5]]`

---

### ✅ Approaches:

---

#### 🔸Brute Force Approach

- Compare every pair of nodes and check if their sum is equal to the target.

```python
def finSumPair(head, target):
    curr1 = head
    ans = []
    while curr1:
        curr2 = curr1.next
        while curr2:
            if curr1.val + curr2.val == target:
                ans.append([curr1.val, curr2.val])
            curr2 = curr2.next
        curr1 = curr1.next
    return ans
```

**Time Complexity**: O(N²)  
**Space Complexity**: O(1)

---

#### 🔹Optimized Two-Pointer Approach (For Sorted DLL)

- Use two pointers: one from the beginning, one from the end.
- Move them toward each other based on sum comparison.

```python
def finSumPairOptimised(head, target):
    left = head
    right = head
    while right.next:
        right = right.next  # Move to tail

    ans = []
    while left != right and left.prev != right:
        total = left.val + right.val
        if total == target:
            ans.append([left.val, right.val])
            left = left.next
            right = right.prev
        elif total < target:
            left = left.next
        else:
            right = right.prev
    return ans
```

**Time Complexity**: O(N)  
**Space Complexity**: O(1)

---

#### 🔄 Input:
`1 <-> 2 <-> 4 <-> 5 <-> 6 <-> 8 <-> 9`, target = `7`

#### ✅ Output:
`[[1, 6], [2, 5]]`

---
### Problem: Remove Duplicates from Sorted Doubly Linked List

#### 🧠 Problem Statement:
Given the head of a **sorted doubly linked list**, remove all duplicate nodes such that each element appears only once.

Example:  
- Input: `1 <-> 2 <-> 2 <-> 3 <-> 3 <-> 4`  
- Output: `1 <-> 2 <-> 3 <-> 4`

---

### ✅ Optimized Approach:

- Traverse the list.
- If current node’s value equals the next node’s value, skip the next node.
- Adjust `next` and `prev` pointers accordingly.

```python
def removeDuplicates(head):
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            next_node = curr.next.next
            curr.next = next_node
            if next_node:
                next_node.prev = curr
        else:
            curr = curr.next
    return head
```

**Time Complexity**: O(N)  
**Space Complexity**: O(1)

---

#### 🔄 Input:
`1 <-> 2 <-> 2 <-> 3 <-> 3 <-> 4`

#### ✅ Output:
`1 <-> 2 <-> 3 <-> 4`
---

