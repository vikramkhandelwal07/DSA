# Trees

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

### 1. Preorder Traversal — Recursive Approach

#### Problem Statement
Given the root of a binary tree, return the **preorder traversal of its nodes' values** in a list.  
Order: **Root → Left → Right**

---

#### Approach
**English:**  
We use a simple recursive depth-first strategy. At each step:  
- Visit the current root node and add its value to the result list.
- Recursively traverse the left subtree.
- Then recursively traverse the right subtree.  

We maintain an auxiliary list `arr` to store the traversal sequence.

**Hinglish:**  
Hum simple recursive DFS strategy use karte hain. Har step par:  
- Current root node ko visit karke uska value result list me daal dete hain.
- Left subtree ko recursively visit karte hain.
- Fir right subtree ko recursively visit karte hain.

---

#### Notes
pattern: binary tree traversal, recursion, dfs  
time: O(n)  
space: O(h)

---

#### Example
Input:
```
      1
     / \
    2   3
   / \
  4   5
```
Output: `[1, 2, 4, 5, 3]`

---

#### Edge Cases
Input: `root = None` → Output: `[]`  
Input: Single node → Output: `[1]`

```python
def preorder(root, arr):
    if not root:
        return
    arr.append(root.value)
    preorder(root.left, arr)
    preorder(root.right, arr)

def preOrder(root):
    arr = []
    preorder(root, arr)
    return arr

print(preOrder(root))  # [1, 2, 4, 5, 3]
```

---

### 2. Preorder Traversal — Iterative Approach

#### Problem Statement
Same as above.

---

#### Approach
**English:**  
We use an explicit stack to simulate recursion. At each step:  
- Push the root node into the stack.  
- While the stack is not empty:  
  - Pop the top node, add its value to the result list.  
  - If the right child exists, push it to stack.  
  - If the left child exists, push it to stack.  

This ensures that left children are processed before right ones.

**Hinglish:**  
Hum recursion ko simulate karne ke liye ek explicit stack use karte hain. Har step par:  
- Root node ko stack me push karte hain.  
- Jab tak stack empty nahi hota:  
  - Top node ko pop karke uska value result me daal dete hain.  
  - Right child ho to stack me push karte hain.  
  - Left child ho to stack me push karte hain.  

Isse left subtree pehle visit hoti hai.

---

#### Notes
pattern: binary tree traversal, iterative dfs, stack  
time: O(n)  
space: O(h)

---

#### Example
Same tree as above. Output: `[1, 2, 4, 5, 3]`

```python
def preOrder(root):
    ans = []
    if not root:
        return ans
    stack = [root]
    while stack:
        root = stack.pop()
        ans.append(root.value)
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
    return ans

print(preOrder(root))  # [1, 2, 4, 5, 3]
```

---

### 3. Inorder Traversal — Recursive & Iterative Approaches

#### Problem Statement
Given the root of a binary tree, return the **inorder traversal of its nodes' values** in a list.  
Order: **Left → Root → Right**

---

#### Approach — Recursive
**English:**  
We use a recursive depth-first strategy. At each step:  
- Recursively traverse the left subtree.
- Visit the current root and add its value to the result.
- Recursively traverse the right subtree.

**Hinglish:**  
Hum recursive DFS strategy use karte hain. Har step par:  
- Left subtree ko recursively visit karte hain.  
- Current root ko visit karke result me daalte hain.  
- Fir right subtree ko recursively visit karte hain.

---

#### Approach — Iterative
**English:**  
We use an explicit stack to simulate recursion.  
- Start with the root node and push all its left descendants into the stack.  
- Pop the top node, add it to the result, and move to its right child.  
- Repeat the process until both stack and current node are empty.

**Hinglish:**  
Hum recursion ko simulate karne ke liye stack use karte hain.  
- Root se shuru karke leftmost tak sare nodes stack me daal dete hain.  
- Top node ko pop karke result me daalte hain aur uske right child pe move karte hain.  
- Jab tak stack aur current node non-empty hain, repeat karte hain.

---

#### Notes
pattern: binary tree traversal, recursion, iterative dfs, stack  
time: O(n)  
space: O(h)

---

#### Example
Input:
```
            1
          /   \
         2     3
       /  \   / \
      4   5  6   7
     / \ / \  \  / \
    8  9 10 11 12 13 14
```
Output: `[8, 4, 9, 2, 10, 5, 11, 1, 6, 12, 3, 13, 7, 14]`

---

#### Edge Cases
Input: `root = None` → Output: `[]`  
Input: Single node → Output: `[1]`

```python
# Recursive
def inorder(root, arr):
    if not root:
        return
    inorder(root.left, arr)
    arr.append(root.value)
    inorder(root.right, arr)

def inorderTraversal(root):
    arr = []
    inorder(root, arr)
    return arr

# Iterative
def Inorder(root):
    stack, ans = [], []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        ans.append(current.value)
        current = current.right
    return ans

print(inorderTraversal(root))  # [8, 4, 9, 2, 10, 5, 11, 1, 6, 12, 3, 13, 7, 14]
print(Inorder(root))           # [8, 4, 9, 2, 10, 5, 11, 1, 6, 12, 3, 13, 7, 14]
```

### 4. Postorder Traversal — Recursive & Iterative Approaches

#### Problem Statement
Given the root of a binary tree, return the **postorder traversal of its nodes' values** in a list.  
Order: **Left → Right → Root**

---

#### Approach — Recursive
**English:**  
We use a simple recursive depth-first strategy. At each step:  
- Recursively traverse the left subtree.  
- Then recursively traverse the right subtree.  
- Finally visit the current root and add its value to the result list.

**Hinglish:**  
Hum simple recursive DFS strategy use karte hain. Har step par:  
- Left subtree ko recursively visit karte hain.  
- Fir right subtree ko recursively visit karte hain.  
- Fir current root ko visit karke result me daal dete hain.

---

#### Approach — Iterative (Using 2 Stacks)
**English:**  
We use two stacks to simulate postorder traversal:  
- Push root to stack1.  
- While stack1 is not empty:  
  - Pop from stack1, push it to stack2.  
  - Push its left and right children (if any) to stack1.  
- Finally, pop all nodes from stack2 to get postorder sequence.

**Hinglish:**  
Hum do stacks use karke postorder simulate karte hain:  
- Root ko stack1 me push karte hain.  
- Jab tak stack1 non-empty ho:  
  - Top node ko stack1 se pop karke stack2 me daal dete hain.  
  - Uske left aur right children ko (agar ho) stack1 me push karte hain.  
- Last me stack2 ko pop karke result le lete hain.

---

#### Approach — Iterative (Using 1 Stack)
**English:**  
We use one stack and a `last_visited` pointer to track traversal:  
- Traverse left as much as possible, pushing nodes to stack.  
- Look at the top of the stack:  
  - If it has a right child not yet visited, move to right child.  
  - Otherwise, visit the node and pop it.

**Hinglish:**  
Hum ek stack aur `last_visited` pointer ka use karte hain:  
- Leftmost tak jaake sab nodes stack me daalte hain.  
- Stack ke top ko dekhte hain:  
  - Agar uska right child hai aur wo visit nahi hua, to right me move karte hain.  
  - Nahi to node ko visit karke stack se pop karte hain.

---

#### Notes
pattern: binary tree traversal, recursion, iterative dfs, stack  
time: O(n)  
space: O(h)

---

#### Example
Input:
```
      1
     / \
    2   3
   / \
  4   5
```
Output: `[4, 5, 2, 3, 1]`

---

#### Edge Cases
Input: `root = None` → Output: `[]`  
Input: Single node → Output: `[1]`

---

```python
# Recursive
def postorder(root, arr):
    if not root:
        return
    postorder(root.left, arr)
    postorder(root.right, arr)
    arr.append(root.value)

def postOrderTraversal(root):
    arr = []
    postorder(root, arr)
    return arr

# Iterative — 2 Stacks
def postOrderIterative(root):
    if not root:
        return []
    stack1 = [root]
    stack2 = []
    ans = []
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    while stack2:
        ans.append(stack2.pop().value)
    return ans

# Iterative — 1 Stack
def postorderIterative(root):
    ans = []
    stack = []
    last_visited = None
    current = root
    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            peek = stack[-1]
            if peek.right and last_visited != peek.right:
                current = peek.right
            else:
                ans.append(peek.value)
                last_visited = stack.pop()
    return ans

# Example usage
print(postOrderTraversal(root))      # [4, 5, 2, 3, 1]
print(postOrderIterative(root))      # [4, 5, 2, 3, 1]
print(postorderIterative(root))      # [4, 5, 2, 3, 1]
```

### 5. Level Order Traversal — BFS Approach

#### Problem Statement
Given the root of a binary tree, return its **level order traversal** as a list of lists, where each inner list contains the values of the nodes at that level.  
Order: **Level by level from top to bottom.**

---

#### Approach
**English:**  
We use a queue to perform breadth-first traversal (BFS).  
- Start by adding the root node to the queue.  
- While the queue is not empty:  
  - Record the number of nodes in the current level (`sizeOfQueue`).  
  - For each node in this level:  
    - Pop it from the queue, add its value to the current level list.  
    - If it has a left child, push it to the queue.  
    - If it has a right child, push it to the queue.  
  - Add the current level list to the final result.  

**Hinglish:**  
Hum ek queue ka use karke BFS karte hain.  
- Root node ko queue me daalte hain.  
- Jab tak queue empty nahi ho jata:  
  - Current level me jitne nodes hain (`sizeOfQueue`) unka count lete hain.  
  - Har node ko queue se nikalte hain, uska value current level list me daalte hain.  
  - Uske left child ko (agar hai) queue me daal dete hain.  
  - Uske right child ko (agar hai) queue me daal dete hain.  
  - Current level list ko final result me daal dete hain.

---

#### Notes
pattern: binary tree traversal, bfs, queue  
time: O(n)  
space: O(n)

---

#### Example
Input:
```
      1
     / \
    2   3
   / \
  4   5
```
Output: `[[1], [2, 3], [4, 5]]`

---

#### Edge Cases
Input: `root = None` → Output: `[]`  
Input: Single node → Output: `[[1]]`

---

```python
from collections import deque

def levelOrderTraversal(root):
    ans = []
    if not root:
        return ans
    q = deque()
    q.append(root)

    while q:
        sizeOfQueue = len(q)
        level = []
        for i in range(sizeOfQueue):
            node = q.popleft()
            level.append(node.value)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans.append(level)
    return ans

# Example usage
print(levelOrderTraversal(root))  # [[1], [2, 3], [4, 5]]
```

### 6. All Traversals in One Pass — Iterative (Preorder, Inorder, Postorder)

#### Problem Statement
Given the root of a binary tree, return its **preorder**, **inorder**, and **postorder** traversals — all computed in a single pass — as three separate lists.

---

#### Approach
**English:**  
We use an explicit stack and maintain a `state` for each node:  
- State 1 → Node is being visited the first time → add to **preorder**, move to left child.  
- State 2 → Left subtree has been processed → add to **inorder**, move to right child.  
- State 3 → Both subtrees processed → add to **postorder**.  

We store `(node, state)` on the stack and update state as we process each node.

**Hinglish:**  
Hum ek stack aur har node ke liye ek `state` rakhte hain:  
- State 1 → Node ko pehli baar dekh rahe hain → preorder me daalo aur left child pe jao.  
- State 2 → Left subtree ho chuki hai → inorder me daalo aur right child pe jao.  
- State 3 → Dono subtree ho chuki hain → postorder me daalo.  

Har node ke saath `(node, state)` stack me store karte hain aur state update karte jaate hain.

---

#### Notes
pattern: iterative dfs, stack, all traversals  
time: O(n)  
space: O(h)

---

#### Example
Input:
```
      1
     / \
    2   3
   / \
  4   5
```
Output:  
Preorder: `[1, 2, 4, 5, 3]`  
Inorder:  `[4, 2, 5, 1, 3]`  
Postorder:`[4, 5, 2, 3, 1]`

---

#### Edge Cases
Input: `root = None` → Output: `([], [], [])`  
Input: Single node → Output: `([1], [1], [1])`

---

```python
def allTraversal(root):
    if not root:
        return [], [], []

    stack = [(root, 1)]
    pre, ino, post = [], [], []

    while stack:
        node, state = stack.pop()
        if state == 1:
            pre.append(node.val)
            stack.append((node, 2))
            if node.left:
                stack.append((node.left, 1))
        elif state == 2:
            ino.append(node.val)
            stack.append((node, 3))
            if node.right:
                stack.append((node.right, 1))
        else:
            post.append(node.val)

    return pre, ino, post

# Example usage
pre, ino, post = allTraversal(root)
print("Preorder:", pre)
print("Inorder:", ino)
print("Postorder:", post)
```

### 7. Height of Binary Tree — Recursive

#### Problem Statement
Given the root of a binary tree, return its **height** (the number of nodes on the longest path from root to a leaf).

---

#### Approach
**English:**  
We use a simple recursive approach:  
- If the node is `None`, height is 0.  
- Otherwise, compute the height of left and right subtrees.  
- Take the maximum of the two and add 1 (for the current node).  

**Hinglish:**  
Hum ek simple recursive approach use karte hain:  
- Agar node `None` hai, to height 0 hoti hai.  
- Warna, left aur right subtree ki height calculate karte hain.  
- Dono me se maximum lete hain aur usme 1 add kar dete hain (current node ke liye).

---

#### Notes
pattern: recursion, dfs, tree height  
time: O(n)  
space: O(h)

---

#### Example
Input:
```
      1
     / \
    2   3
   /
  4
```
Output: `3`

---

#### Edge Cases
Input: `root = None` → Output: `0`  
Input: Single node → Output: `1`

---

```python
def height(self, root):
    if not root:
        return 0
    lh = self.height(root.left)
    rh = self.height(root.right)
    return max(lh, rh) + 1

# Example usage
print(height(root))  # Output: 3
```

### 8. Check if Binary Tree is Height-Balanced

#### Problem Statement
Given the root of a binary tree, determine if the tree is **height-balanced**.  
A binary tree is balanced if, for every node, the difference between the heights of its left and right subtrees is at most 1.

---

#### Approach
**English:**  
We use a bottom-up recursive approach:  
- If the node is `None`, height is 0.  
- Recursively calculate the height of left and right subtrees.  
- If any subtree is already unbalanced (`-1`), propagate `-1` up.  
- At each node, if the height difference of left and right is more than 1, return `-1`.  
- Otherwise, return the height of the subtree.  
- Finally, check if the result of root is `-1` or not.

**Hinglish:**  
Hum bottom-up recursive approach use karte hain:  
- Agar node `None` hai, to height 0 hoti hai.  
- Left aur right subtree ki height recursively nikalte hain.  
- Agar kisi subtree me imbalance mila (`-1`), to `-1` propagate kar dete hain.  
- Har node par check karte hain ki left aur right ka height difference >1 to nahi. Agar hai to `-1`.  
- Warna maximum height +1 return karte hain.  
- Root ka result `-1` nahi hai to tree balanced hai.

---

#### Notes
pattern: recursion, dfs, balanced tree check  
time: O(n)  
space: O(h)

---

#### Example
Input:
```
      1
     / \
    2   3
   /
  4
 /
5
```
Output: `False` (Not balanced)

Input:
```
    1
   / \
  2   3
```
Output: `True` (Balanced)

---

#### Edge Cases
Input: `root = None` → Output: `True`  
Input: Single node → Output: `True`

---

```python
def check(root):
    if not root:
        return 0  # height of empty tree is 0

    lh = check(root.left)
    if lh == -1:  # left subtree is unbalanced
        return -1

    rh = check(root.right)
    if rh == -1:  # right subtree is unbalanced
        return -1

    if abs(lh - rh) > 1:  # current node is unbalanced
        return -1

    return max(lh, rh) + 1  # return height if balanced

def isBalanced(root):
    return check(root) != -1

# Example usage
print(isBalanced(root))  # True / False
```

### 9. Diameter of Binary Tree

#### Problem Statement
Given the root of a binary tree, return its **diameter**.  
The diameter of a binary tree is the length of the longest path between any two nodes in the tree.  
(The path may or may not pass through the root.)

---

#### Approach
**English:**  
We use a recursive depth-first search:  
- At each node, calculate the height of the left and right subtrees.  
- The path that passes through this node is `left height + right height`.  
- Keep track of the maximum such path found so far (the diameter) in a mutable variable.  
- Return the height of the current subtree to the parent call (`max(left, right) + 1`).  
- Finally, the maximum path length (stored in the mutable variable) is the diameter.

**Hinglish:**  
Hum recursive DFS approach use karte hain:  
- Har node ke liye left aur right subtree ki height calculate karte hain.  
- Us node ke through hone wala path hota hai: `left height + right height`.  
- Is path ka maximum value (diameter) ek list me maintain karte hain.  
- Parent ko height return karte hain: `max(left, right) + 1`.  
- Final me list me stored maximum path length return karte hain.

---

#### Notes
pattern: dfs, recursion, tree height, longest path  
time: O(n)  
space: O(h)

---

#### Example
Input:
```
      1
     / \
    2   3
   / \     
  4   5   
```
Output: `3`  
Explanation: Longest path is `4 → 2 → 5` or `4 → 2 → 1 → 3`, both have length 3.

---

#### Edge Cases
Input: `root = None` → Output: `0`  
Input: Single node → Output: `0`

---

```python
def diameterOfBinaryTree(root):
    diameter = [0]

    def height(node):
        if not node:
            return 0
        lh = height(node.left)
        rh = height(node.right)
        diameter[0] = max(diameter[0], lh + rh)
        return max(lh, rh) + 1

    height(root)
    return diameter[0]

# Example usage
print(diameterOfBinaryTree(root))  # Output: 3
```

### 10. Maximum Path Sum in Binary Tree

#### Problem Statement
Given the root of a binary tree, return the **maximum path sum**.  
A path is any sequence of nodes where each pair of adjacent nodes are connected by an edge — and each node appears at most once.  
The path does not need to pass through the root.

---

#### Approach
**English:**  
We use a recursive depth-first search:  
- At each node, calculate the **maximum path sum from this node down to any leaf** (called gain).  
- We only add positive gains from left or right (since negative values decrease the sum).  
- At each node, the path **through the node** can be:  
  `node value + left gain + right gain`.  
- Keep track of the maximum of all such paths in a mutable variable.  
- Return to parent only the **max gain path including this node and one of its children**.  

**Hinglish:**  
Hum recursive DFS use karte hain:  
- Har node pe calculate karte hain ki is node se leaf tak jane wali maximum path sum kitni ho sakti hai (gain).  
- Left aur right me se sirf positive gain hi consider karte hain.  
- Har node par ye bhi check karte hain ki:  
  `node value + left gain + right gain` kitna hai aur global maximum update karte hain.  
- Parent ko sirf ek child ka maximum gain + node value return karte hain.

---

#### Notes
pattern: dfs, recursion, tree dp  
time: O(n)  
space: O(h)

---

#### Example
Input:
```
      -10
      /  \
     9   20
        /  \
       15   7
```
Output: `42`  
Explanation: The path is `15 → 20 → 7`.

---

#### Edge Cases
Input: `root = None` → Output: `0`  
Input: Single node → Output: value of that node

---

```python
def maxPathSum(root):
    max_sum = [float('-inf')]

    def max_gain(node):
        if not node:
            return 0
        left_gain = max(0, max_gain(node.left))
        right_gain = max(0, max_gain(node.right))
        max_sum[0] = max(max_sum[0], node.val + left_gain + right_gain)
        return node.val + max(left_gain, right_gain)

    max_gain(root)
    return max_sum[0]

# Example usage
print(maxPathSum(root))  # Output: 42
```

### 11. Check if Two Trees are Identical

#### Problem Statement
Given two binary trees, determine if they are **structurally identical** and their corresponding nodes have the same value.

---

#### Approach
**English:**  
We use a recursive approach:  
- If both nodes are `None`, they are identical at this level, return `True`.  
- If only one is `None` or their values are different, return `False`.  
- Recursively check left subtree of both and right subtree of both.  
- If both left and right subtrees are identical, then the whole trees are identical.

**Hinglish:**  
Hum recursive approach use karte hain:  
- Agar dono nodes `None` hain to is level par identical hain → `True`.  
- Agar sirf ek `None` hai ya unke values alag hain → `False`.  
- Dono ke left subtrees aur right subtrees ko recursively check karte hain.  
- Dono subtrees identical mile to puri trees identical hongi.

---

#### Notes
pattern: dfs, recursion, tree comparison  
time: O(n)  
space: O(h)

---

#### Example
Input:
```
Tree 1:          Tree 2:
    1                1
   / \              / \
  2   3            2   3
```
Output: `True` (Identical)

Input:
```
Tree 1:          Tree 2:
    1                1
   /                  \
  2                    2
```
Output: `False` (Not identical)

---

#### Edge Cases
Input: Both trees `None` → Output: `True`  
Input: One tree `None`, other not → Output: `False`

---

```python
def isSameTree(self, p, q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Example usage
print(isSameTree(p_root, q_root))  # True / False
```

### 12. Zig-Zag (Spiral Order) Traversal of Binary Tree

#### Problem Statement
Given the root of a binary tree, return a **zig-zag level order traversal** of its nodes.  
That is, first level left→right, second level right→left, third level left→right, and so on.

---

#### Approach
**English:**  
We use a queue for level order and a flag for direction:  
- Initialize a queue with the root node.  
- For each level, collect all nodes in a temporary list.  
- If the level is **even**, add nodes left→right.  
- If the level is **odd**, reverse the temporary list to make it right→left.  
- Append the level list to the result.  
- Continue for all levels.

**Hinglish:**  
Hum ek queue aur ek direction flag use karte hain:  
- Root ko queue me daalte hain.  
- Har level ke liye ek temporary list banate hain.  
- Agar level even hai to nodes ko left→right daalte hain.  
- Agar level odd hai to nodes ki list ko reverse karke right→left kar dete hain.  
- Level list ko result me daal dete hain.  
- Sabhi levels ke liye repeat karte hain.

---

#### Notes
pattern: bfs, queue, level-order with direction toggle  
time: O(n)  
space: O(n)

---

#### Example
Input:
```
        1
      /   \
     2     3
    / \   / \
   4   5 6   7
```
Output:  
`[[1], [3, 2], [4, 5, 6, 7]]`

---

#### Edge Cases
Input: `root = None` → Output: `[]`  
Input: Single node → Output: `[[1]]`

---

```python
from collections import deque

def zigzagLevelOrder(root):
    ans = []
    if not root:
        return ans

    q = deque()
    q.append(root)
    left_to_right = True

    while q:
        size = len(q)
        level = deque()

        for _ in range(size):
            node = q.popleft()
            if left_to_right:
                level.append(node.val)
            else:
                level.appendleft(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        ans.append(list(level))
        left_to_right = not left_to_right

    return ans

# Example usage
print(zigzagLevelOrder(root))  # Output: [[1], [3, 2], [4, 5, 6, 7]]
```

### 13. Boundary Traversal of Binary Tree

#### Problem Statement
Given the root of a binary tree, return its **boundary traversal** in anti-clockwise order.  
Boundary traversal = Root → Left boundary → All leaves → Right boundary (in reverse).

---

#### Approach
**English:**  
We divide the traversal into 3 parts:  
✅ Left boundary (excluding leaves)  
✅ All leaf nodes (from left to right)  
✅ Right boundary (excluding leaves, added in reverse)  

Steps:  
- Add the root if it’s not a leaf.  
- Traverse down the leftmost path, adding nodes except leaves.  
- Add all leaf nodes by doing DFS.  
- Traverse down the rightmost path, adding nodes except leaves, and reverse them.  
Finally, concatenate all 3 parts into one list.

**Hinglish:**  
Traversal ko 3 parts me todte hain:  
✅ Left boundary (leaves ko chhodkar)  
✅ Saare leaf nodes (left to right)  
✅ Right boundary (leaves ko chhodkar, reverse me)  

Steps:  
- Root ko add karo agar wo leaf nahi hai.  
- Leftmost path pe jao aur leaves ko chhodkar sab add karo.  
- DFS karke sabhi leaf nodes ko add karo.  
- Rightmost path pe jao aur leaves ko chhodkar sab add karo aur reverse karke add karo.  
Ye sabko ek list me jod do.

---

#### Notes
pattern: dfs, tree traversal, boundary  
time: O(n)  
space: O(h)

---

#### Example
Input:
```
        1
      /   \
     2     3
    / \   / \
   4   5 6   7
      / \
     8   9
```
Output:  
`[1, 2, 4, 8, 9, 6, 7, 3]`

---

#### Edge Cases
Input: `root = None` → Output: `[]`  
Input: Single node → Output: `[1]`

---

```python
def isleaf(root):
    return not root.left and not root.right

def leftBoundary(root, ans):
    curr = root.left
    while curr:
        if not isleaf(curr):
            ans.append(curr.value)
        if curr.left:
            curr = curr.left
        else:
            curr = curr.right

def rightBoundary(root, ans):
    curr = root.right
    temp = []
    while curr:
        if not isleaf(curr):
            temp.append(curr.value)
        if curr.right:
            curr = curr.right
        else:
            curr = curr.left
    for i in range(len(temp)-1, -1, -1):
        ans.append(temp[i])

def addLeaves(root, ans):
    if isleaf(root):
        ans.append(root.value)
        return
    if root.left:
        addLeaves(root.left, ans)
    if root.right:
        addLeaves(root.right, ans)

def boundaryTraversal(root):
    ans = []
    if not root:
        return []
    if not isleaf(root):
        ans.append(root.value)
    addLeaves(root, ans) if isleaf(root) else (
        leftBoundary(root, ans),
        addLeaves(root, ans),
        rightBoundary(root, ans)
    )
    return ans

# Example usage
print(boundaryTraversal(root))  # Output: [1, 2, 4, 8, 9, 6, 7, 3]
```

### 14. Vertical Order Traversal of Binary Tree

#### Problem Statement
Given the root of a binary tree, return its **vertical order traversal**.  
Nodes in the same vertical column appear together (top to bottom, leftmost to rightmost).  
If multiple nodes appear at the same position, output them in **sorted order by value**.

---

#### Approach
**English:**  
We use a BFS traversal with coordinates `(x, y)` for each node:  
- `x` → horizontal distance from root (column index)  
- `y` → depth level (row index)  
- Use a nested map `nodes[x][y]` to store all nodes at position `(x, y)`.  
- Traverse the tree using a queue (BFS), updating `(x, y)` for left child as `(x-1, y+1)` and right child as `(x+1, y+1)`.  
- After traversal, collect nodes column by column (`x` ascending), row by row (`y` ascending), and sort values at same position.  

**Hinglish:**  
Hum BFS traversal karte hain aur har node ka `(x, y)` coordinate maintain karte hain:  
- `x` → root se horizontal distance (column)  
- `y` → depth level (row)  
- Ek nested map `nodes[x][y]` me har position ke nodes store karte hain.  
- Queue me `(node, (x,y))` store karke BFS chalaate hain. Left child ka `(x-1,y+1)` aur right ka `(x+1,y+1)` hota hai.  
- BFS ke baad sabhi columns ko `x` ascending me aur rows ko `y` ascending me traverse karke values ko sorted order me collect karte hain.

---

#### Notes
pattern: bfs, hash map, vertical traversal  
time: O(n log n) (because of sorting)  
space: O(n)

---

#### Example
Input:
```
        1
      /   \
     2     3
    / \   / \
   4   5 6   7
            /
           8
```
Output:  
`[[4], [2], [1, 5, 6], [3, 8], [7]]`

---

#### Edge Cases
Input: `root = None` → Output: `[]`  
Input: Single node → Output: `[[1]]`

---

```python
from collections import defaultdict, deque

def verticalTraversal(root):
    nodes = defaultdict(lambda: defaultdict(list))
    todo = deque([(root, (0, 0))])

    while todo:
        temp, (x, y) = todo.popleft()
        nodes[x][y].append(temp.value)

        if temp.left:
            todo.append((temp.left, (x-1, y+1)))
        if temp.right:
            todo.append((temp.right, (x+1, y+1)))

    ans = []
    for x in sorted(nodes.keys()):  # Columns left-to-right
        col = []
        for y in sorted(nodes[x].keys()):  # Rows top-to-bottom
            col.extend(sorted(nodes[x][y]))  # sort same-level nodes
        ans.append(col)
    return ans

# Example usage
print(verticalTraversal(root))  # Output: [[4], [2], [1, 5, 6], [3, 8], [7]]
```

### 15. Top View of Binary Tree

#### Problem Statement
Return the nodes visible when the tree is viewed from the **top**.  
We see only the first node at each horizontal distance (hd) when looking from above.

---

#### Approach
**English:**  
We use **Level Order Traversal (BFS)** and track each node's horizontal distance (`hd`) from the root:  
- Root is at `hd = 0`.  
- Left child is at `hd - 1`, right child at `hd + 1`.  
- Use a map `hd → node value` to store the **first node encountered** at each horizontal distance.  
- Traverse the tree level by level using a queue of `(node, hd)`.  
- For each node, if `hd` is not yet in the map, record its value.  
- At the end, output all node values sorted by `hd` from smallest to largest.

**Hinglish:**  
Hum **BFS (Level Order Traversal)** karte hain aur har node ka `hd` (horizontal distance) maintain karte hain:  
- Root ka `hd = 0`.  
- Left child ka `hd -1`, right child ka `hd +1`.  
- Ek map me `hd → node value` tabhi set karte hain jab wo pehli bar mile.  
- Queue me `(node, hd)` store karke level by level traverse karte hain.  
- BFS ke baad, map ko `hd` ke order me read karke answer banate hain.

---

#### Example
Input:  
```
       1
      / \
     2   3
      \
       4
        \
         5
          \
           6
```
Output:  
`[2, 1, 3, 6]`

---

#### Code
```python
from collections import deque

def topView(root):
    if not root:
        return []
    q = deque([(root, 0)])
    hd_map = dict()
    min_hd, max_hd = 0, 0

    while q:
        node, hd = q.popleft()
        if hd not in hd_map:
            hd_map[hd] = node.value
        min_hd = min(min_hd, hd)
        max_hd = max(max_hd, hd)

        if node.left:
            q.append((node.left, hd - 1))
        if node.right:
            q.append((node.right, hd + 1))

    return [hd_map[hd] for hd in range(min_hd, max_hd + 1)]
```

---

### 16. Bottom View of Binary Tree

#### Problem Statement
Return the nodes visible when the tree is viewed from the **bottom**.  
We see only the **lowest node at each horizontal distance (hd)** when looking from below.

---

#### Approach
**English:**  
We use **Level Order Traversal (BFS)** and track each node's horizontal distance (`hd`) from the root:  
- Root is at `hd = 0`.  
- Left child is at `hd - 1`, right child at `hd + 1`.  
- Use a map `hd → node value` and overwrite it each time we visit a node at the same `hd`.  
- At the end, output all node values sorted by `hd` from smallest to largest.  
Because BFS processes level by level, the last node seen at each `hd` is the bottom-most one.

**Hinglish:**  
Hum **BFS (Level Order Traversal)** karte hain aur har node ka `hd` (horizontal distance) maintain karte hain:  
- Root ka `hd = 0`.  
- Left child ka `hd -1`, right child ka `hd +1`.  
- Ek map me `hd → node value` har bar overwrite karte hain jab wo `hd` dobara mile.  
- BFS ke baad, map ko `hd` ke order me read karke answer banate hain.

---

#### Example
Input:  
```
       1
      / \
     2   3
      \
       4
        \
         5
          \
           6
```
Output:  
`[2, 4, 5, 6]`

---

#### Code
```python
def bottomView(root):
    if not root:
        return []
    q = deque([(root, 0)])
    hd_map = dict()
    min_hd, max_hd = 0, 0

    while q:
        node, hd = q.popleft()
        hd_map[hd] = node.value
        min_hd = min(min_hd, hd)
        max_hd = max(max_hd, hd)

        if node.left:
            q.append((node.left, hd - 1))
        if node.right:
            q.append((node.right, hd + 1))

    return [hd_map[hd] for hd in range(min_hd, max_hd + 1)]
```

---

### 17. Left View of Binary Tree

#### Problem Statement
Return the nodes visible when the tree is viewed from the **left side**.  
We see the **first node at each level**.

---

#### Approach
**English:**  
We use **Level Order Traversal (BFS)** and process each level from left to right:  
- For each level, the **first node encountered** is part of the left view.  
- Use a queue and for each level, loop over its nodes and pick the first one.  
- Append that first node’s value to the answer list.

**Hinglish:**  
Hum **BFS (Level Order Traversal)** karte hain aur har level ko left to right process karte hain:  
- Har level ki **pehli node** ko hi left view me lete hain.  
- Queue me har level ke sab nodes dal kar pehle wale ko answer me daal dete hain.

---

#### Example
Input:  
```
       1
      / \
     2   3
    / \
   4   5
        \
         6
```
Output:  
`[1, 2, 4, 6]`

---

#### Code
```python
from collections import deque

def leftView(root):
    if not root:
        return []
    q = deque([root])
    ans = []

    while q:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            if i == 0:
                ans.append(node.value)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return ans
```

---

### 18. Right View of Binary Tree

#### Problem Statement
Return the nodes visible when the tree is viewed from the **right side**.  
We see the **last node at each level**.

---

#### Approach
**English:**  
We use **Level Order Traversal (BFS)** and process each level from left to right:  
- For each level, the **last node encountered** is part of the right view.  
- Use a queue and for each level, loop over its nodes and pick the last one.  
- Append that last node’s value to the answer list.

**Hinglish:**  
Hum **BFS (Level Order Traversal)** karte hain aur har level ko left to right process karte hain:  
- Har level ki **last node** ko hi right view me lete hain.  
- Queue me har level ke sab nodes dal kar last wale ko answer me daal dete hain.

---

#### Example
Input:  
```
       1
      / \
     2   3
      \
       5
        \
         6
```
Output:  
`[1, 3, 5, 6]`

---

#### Code
```python
def rightView(root):
    if not root:
        return []
    q = deque([root])
    ans = []

    while q:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            if i == size - 1:
                ans.append(node.value)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return ans
```

---

### 19. Root-to-Node Path in Binary Tree

#### Problem Statement
Given the root of a binary tree and an integer `x`, return the path from the **root to the node containing value `x`** as a list of values.  
If the node with value `x` does not exist in the tree, return an empty list.

---

#### Approach
**English:**  
We use a simple **DFS (Depth First Search)** with recursion:  
- At each node, add the node’s value to the current path (`ds`).  
- If the current node matches `x`, return `True` (path is found).  
- Recursively check the left and right subtrees.  
- If neither returns `True`, remove (backtrack) the current node from the path and return `False`.  
- At the end, the `ds` list will contain the path if `x` is found.

**Hinglish:**  
Hum **DFS (recursion)** use karte hain:  
- Har node pe apni value ko current path (`ds`) me daal dete hain.  
- Agar current node ka value `x` hai, to `True` return kar dete hain.  
- Left aur right subtree me recursively check karte hain.  
- Agar dono me `x` nahi mila, to current node ko path (`ds`) se hata dete hain (backtrack) aur `False` return karte hain.  
- DFS ke baad `ds` me path hoga agar `x` mila.

---

#### Example
Input:  
```
       1
      / \
     2   3
    / \
   4   5
```
x = 5

Output:  
`[1, 2, 5]`

---

#### Code
```python
def rootToNode(root, x):
    def helper(node, ds, x):
        if not node:
            return False
        
        ds.append(node.value)
        
        if node.value == x:
            return True
        
        if helper(node.left, ds, x) or helper(node.right, ds, x):
            return True
        
        ds.pop()  # backtrack if x not found in this path
        return False
    
    ds = []
    helper(root, ds, x)
    return ds
```

---

### 20. Lowest Common Ancestor (LCA) in Binary Tree

#### Problem Statement
Given the root of a binary tree and two nodes `p` and `q`, find their **Lowest Common Ancestor (LCA)**.  
The LCA of two nodes `p` and `q` is the lowest node in the tree that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself).

---

#### Approach
**English:**  
We use a **recursive DFS** approach:  
- If the current `root` is `None`, `p`, or `q`, we return `root`.  
- Recursively find LCA in the left subtree and the right subtree.  
- If both left and right recursive calls return non-`None`, then `root` is the LCA (because `p` and `q` are in different subtrees).  
- Otherwise, return whichever is not `None`.

**Hinglish:**  
Hum **recursive DFS** approach use karte hain:  
- Agar current `root` me se koi `None`, `p`, ya `q` ho to wahi return kar dete hain.  
- Left aur right subtree me recursively LCA dhoondte hain.  
- Agar left aur right dono me `None` nahi hai to current `root` hi LCA hai (kyuki `p` aur `q` alag subtrees me hain).  
- Nahi to jo bhi `None` nahi hai wahi return karte hain.

---

#### Example
Input:  
```
       3
      / \
     5   1
    / \ / \
   6  2 0  8
     / \
    7   4
```
p = 5, q = 1  
Output:  
`3`

---

#### Code
```python
def lowestCommonAncestor(self, root, p, q):
    if not root or root == p or root == q:
        return root

    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root  # p and q found in different subtrees

    return left if left else right
```

---

### 21. Maximum Width of Binary Tree

#### Problem Statement
Given the root of a binary tree, return the **maximum width of the tree**.  
The width of a level is defined as the length between the leftmost and rightmost non-null nodes at that level (including `null`s in-between).

---

#### Approach
**English:**  
We use **Level Order Traversal (BFS)** and assign a positional index to each node:  
- Root is at index `0`.  
- For each node at index `i`, its left child gets index `2*i+1` and right child gets `2*i+2`.  
- For each level, calculate the width as `last_index - first_index + 1`.  
- Keep track of the maximum width encountered across all levels.  

**Hinglish:**  
Hum **BFS (Level Order Traversal)** karte hain aur har node ko ek index assign karte hain:  
- Root ka index `0` hota hai.  
- Left child ka index `2*i+1` aur right child ka index `2*i+2` hota hai.  
- Har level me `last_index - first_index + 1` se width nikalte hain.  
- Sabhi levels me se maximum width ko track karte hain.

---

#### Example
Input:  
```
       1
      / \
     3   2
    /     \
   5       9
  /         \
 6           7
```

Output:  
`8`

---

#### Code
```python
from collections import deque

def maxWidthOfTree(root):
    if not root:
        return 0
    ans = 0
    q = deque()
    q.append((root, 0))
    while q:
        size = len(q)
        mmin = q[0][1]
        first, last = None, None
        for i in range(size):
            node, idx = q.popleft()
            currid = idx - mmin
            if i == 0:
                first = currid
            if i == size - 1:
                last = currid
            if node.left:
                q.append((node.left, currid * 2 + 1))
            if node.right:
                q.append((node.right, currid * 2 + 2))
        ans = max(ans, last - first + 1)
    return ans
```

---

### 22. Children Sum Property in Binary Tree

#### Problem Statement
Modify the given binary tree so that it satisfies the **Children Sum Property**,  
i.e., for every node, its value becomes equal to the sum of its children's values.  
You can only **increase node values**, never decrease them.

---

#### Approach
**English:**  
We solve this using **Postorder Traversal (Bottom-Up DFS)**:  
- At each node, calculate the sum of its left and right children's values (`child`).  
- If `child >= root.value`, then set `root.value = child`.  
- Otherwise, propagate `root.value` down to its children by setting their values to at least `root.value`.  
- Recur for left and right subtrees.  
- On returning back up, update the current `root.value` to the sum of updated children’s values if it is not a leaf.

**Hinglish:**  
Hum **postorder traversal (bottom-up)** karte hain:  
- Har node ke left aur right child ka sum (`child`) calculate karte hain.  
- Agar `child >= root.value`, to `root.value = child`.  
- Nahi to, apni value ko children me propagate kar dete hain.  
- Fir left aur right subtree me recurse karte hain.  
- Wapas aate hue apni value ko updated children ke sum ke barabar kar dete hain (agar leaf nahi hai).

---

#### Example
Input:  
```
        50
       /  \
      7    2
     / \  / 
    3  5 1  
```

Output:  
```
        50
       /  \
     12   38
     / \  /
    3  9 1
```

---

#### Code
```python
def childrenSumProperty(root):
    if not root:
        return

    # Step 1: Get sum of children
    child = 0
    if root.left:
        child += root.left.value
    if root.right:
        child += root.right.value

    # Step 2: If child sum >= root, update root
    if child >= root.value:
        root.value = child
    else:
        # Else propagate root's value down
        if root.left:
            root.left.value = root.value
        if root.right:
            root.right.value = root.value

    # Step 3: Recur for left and right
    childrenSumProperty(root.left)
    childrenSumProperty(root.right)

    # Step 4: Update root value to sum of updated children
    tot = 0
    if root.left:
        tot += root.left.value
    if root.right:
        tot += root.right.value

    if root.left or root.right:
        root.value = tot
```

---

### 23. Nodes at Distance K in Binary Tree

#### Problem Statement
Given a binary tree, a **target node**, and an integer `k`, find all nodes that are at distance `k` from the target node.  
Distance between two nodes is defined as the number of edges in the shortest path connecting them.

---

#### Approach
**English:**  
We solve this using **BFS (Breadth-First Search) + Parent Mapping**:  
- Traverse the tree and store each node’s parent in a map (`parentMap`) so we can move upwards as well.  
- Start BFS from the target node, exploring its left child, right child, and parent (if they exist and are unvisited).  
- Use a `visited` set to avoid revisiting nodes.  
- Stop BFS once we reach level `k`.  
- The nodes left in the queue at level `k` are the answer.

**Hinglish:**  
Hum **BFS + Parent Mapping** ka use karte hain:  
- Sabse pehle tree me traverse karke har node ka parent ek map (`parentMap`) me store kar lete hain, taaki upar bhi ja saken.  
- Fir target node se BFS start karte hain, aur uske left, right, aur parent ko explore karte hain (agar unvisited ho).  
- Ek `visited` set rakhenge taaki node dobara visit na ho.  
- Jaise hi level `k` tak pahunchte hain, BFS ko rok dete hain.  
- Queue me jo nodes bache hain wo hi answer hain.

---

#### Example
Input:  
```
        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4
Target: 5, k = 2
```

Output:  
```
[7, 4, 1]
```

---

#### Code
```python
from collections import deque

def markParents(root, parentMap):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.left:
            parentMap[node.left] = node
            queue.append(node.left)
        if node.right:
            parentMap[node.right] = node
            queue.append(node.right)

def nodesAtDistanceK(root, target, k):
    if not root:
        return []

    parentMap = {}
    markParents(root, parentMap)

    visited = set()
    queue = deque()

    queue.append(target)
    visited.add(target)
    level = 0

    while queue:
        if level == k:
            break
        for _ in range(len(queue)):
            node = queue.popleft()
            for neighbor in (node.left, node.right, parentMap.get(node)):
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        level += 1

    return [node.value for node in queue]
```

---

#### Complexity
- **Time Complexity:** `O(N)` — where `N` is the number of nodes in the tree (to build parent map and BFS traversal).  
- **Space Complexity:** `O(N)` — for parent map, visited set, and BFS queue.

---


### 24. Time to Infect Binary Tree

#### Problem Statement
Given a binary tree and a **starting node value**, determine the minimum time required to infect the entire tree if infection spreads to adjacent nodes (left child, right child, and parent) each minute.  
In one unit of time, all currently infected nodes spread the infection to their uninfected neighbors.

---

#### Approach
**English:**  
We solve this using **BFS (Breadth-First Search) + Parent Mapping**:  
- First, traverse the tree and build a map (`parentMap`) that stores the parent of each node.  
- Then, locate the starting node in the tree.  
- From the starting node, perform BFS: at each level, infect all uninfected adjacent nodes (left, right, and parent).  
- Count the number of levels we traverse — this is the total time to infect the entire tree.

**Hinglish:**  
Hum **BFS + Parent Mapping** ka use karte hain:  
- Sabse pehle tree ko traverse karke har node ka parent ek map (`parentMap`) me store kar lete hain.  
- Fir tree me starting node ko locate karte hain.  
- BFS start karte hain starting node se: har level me left, right, aur parent ko infect karte hain (agar wo abhi tak infect nahi hue ho).  
- Jitne levels traverse karenge, utna hi time lagta hai tree ko poora infect karne me.

---

#### Example
Input Tree:  
```
        1
       / \
      2   3
     / \ / \
    4  5 6  7
Start: 2
```

Output:  
```
Time to infect entire tree starting from 2: 3
```

---

#### Code
```python
from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def markParent(root, parentMap):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.left:
            parentMap[node.left] = node
            queue.append(node.left)
        if node.right:
            parentMap[node.right] = node
            queue.append(node.right)

def findNode(root, value):
    if not root:
        return None
    if root.value == value:
        return root
    left = findNode(root.left, value)
    if left:
        return left
    return findNode(root.right, value)

def timeToInfect(root, start):
    if not root:
        return 0
    
    # Step 1: build parent map
    parentMap = {}
    markParent(root, parentMap)
    
    # Step 2: find starting node
    target = findNode(root, start)
    if not target:
        return 0  # start node not found
    
    # Step 3: BFS from target
    visited = set()
    queue = deque([target])
    visited.add(target)
    
    time = 0
    
    while queue:
        size = len(queue)
        any_infected = False
        
        for _ in range(size):
            node = queue.popleft()
            for neighbor in (node.left, node.right, parentMap.get(node)):
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    any_infected = True
        if any_infected:
            time += 1  # next level of infection
    return time
```

---

#### Complexity
- **Time Complexity:** `O(N)` — where `N` is the number of nodes in the tree (to build parent map and perform BFS).  
- **Space Complexity:** `O(N)` — for parent map, visited set, and BFS queue.

---


### 25. Construct Binary Tree from Inorder and Postorder Traversal

#### Problem Statement
Given two arrays — `inorder` and `postorder` — representing the inorder and postorder traversal of a binary tree, construct and return the binary tree.

- You may assume that there are no duplicate elements in the tree.

---

#### Approach
**English:**  
We solve this using **recursive DFS + index mapping**:
- The last element of `postorder` is always the root of the current subtree.  
- Use a hashmap (`idxMap`) to store the indices of elements in `inorder` for `O(1)` lookups.  
- Recursively build the right subtree first (since we pop elements from the end of `postorder`), then the left subtree.  
- Base case: if the current `inleft > inright`, return `None`.

**Hinglish:**  
Hum **DFS + index map** ka use karte hain:  
- `postorder` ka last element hamesha current subtree ka root hota hai.  
- Ek hashmap (`idxMap`) me `inorder` ke elements ke indices store karte hain fast lookup ke liye.  
- Right subtree pehle banate hain (kyunki `postorder` ka end se pop kar rahe hain), fir left subtree.  
- Base case: agar `inleft > inright`, to `None` return karte hain.

---

#### Example
Input:  
```
inorder   = [9,3,15,20,7]
postorder = [9,15,7,20,3]
```

Output Tree:  
```
      3
     / \
    9  20
      /  \
     15   7
```

---

#### Code
```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def buildTree(postorder, inorder):
    if not postorder and not inorder:
        return None
    
    idxMap = {val: idx for idx, val in enumerate(inorder)}
    
    def helper(inleft, inright):
        if inleft > inright:
            return None
        
        rootVal = postorder.pop()
        root = TreeNode(rootVal)
        inRootIdx = idxMap[rootVal]
        
        root.right = helper(inRootIdx + 1, inright)
        root.left = helper(inleft, inRootIdx - 1)
        return root
    
    return helper(0, len(inorder) - 1)
```

---

#### Complexity
- **Time Complexity:** `O(N)` — each node is processed once and the hashmap provides `O(1)` lookups.  
- **Space Complexity:** `O(N)` — for recursion stack and hashmap.

---

### 26. Construct Binary Tree from Inorder and Preorder Traversal

#### Problem Statement
Given two arrays — `inorder` and `preorder` — representing the inorder and preorder traversal of a binary tree, construct and return the binary tree.

- You may assume that there are no duplicate elements in the tree.

---

#### Approach
**English:**  
We solve this using **recursive DFS + index mapping**:
- The first element of `preorder` is always the root of the current subtree.  
- Use a hashmap (`idx_map`) to store the indices of elements in `inorder` for `O(1)` lookups.  
- Recursively build the left subtree first (since in `preorder` left subtree nodes come before right subtree nodes), then the right subtree.  
- Track the size of the left subtree (`leftSize`) to adjust the indices correctly in `preorder`.

**Hinglish:**  
Hum **DFS + index map** ka use karte hain:  
- `preorder` ka first element hamesha current subtree ka root hota hai.  
- Ek hashmap (`idx_map`) me `inorder` ke elements ke indices store karte hain fast lookup ke liye.  
- Left subtree pehle banate hain (kyunki `preorder` me pehle left subtree ke nodes aate hain), fir right subtree.  
- Left subtree ka size nikalte hain (`leftSize`) aur uske hisaab se indices adjust karte hain.

---

#### Example
Input:  
```
inorder   = [9,3,15,20,7]
preorder  = [3,9,20,15,7]
```

Output Tree:  
```
      3
     / \
    9  20
      /  \
     15   7
```

---

#### Code
```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def buildTree(inorder, preorder):
    if not preorder or not inorder:
        return None
    
    idx_map = {val: idx for idx, val in enumerate(inorder)}
    
    def helper(preLeft, preRight, inLeft, inRight):
        if preLeft > preRight:
            return None
        
        rootVal = preorder[preLeft]
        root = TreeNode(rootVal)
        inRootIndex = idx_map[rootVal]
        leftSize = inRootIndex - inLeft
        
        root.left = helper(preLeft + 1, preLeft + leftSize, inLeft, inRootIndex - 1)
        root.right = helper(preLeft + leftSize + 1, preRight, inRootIndex + 1, inRight)
        
        return root
    
    return helper(0, len(preorder) - 1, 0, len(inorder) - 1)
```

---

#### Complexity
- **Time Complexity:** `O(N)` — each node is processed once and the hashmap provides `O(1)` lookups.  
- **Space Complexity:** `O(N)` — for recursion stack and hashmap.

---


### 27. Serialize and Deserialize Binary Tree

#### Problem Statement
Design an algorithm to **serialize** and **deserialize** a binary tree.  

- Serialization is the process of converting a tree into a string.
- Deserialization is the process of converting the encoded string back into a binary tree.
- You may assume the tree contains integer values, and you can use any string format.
- You should be able to serialize and then deserialize the tree without data loss.

---

#### Approach
**English:**  
We solve this using **Level Order Traversal (BFS)**:
- For serialization:
  - Perform BFS, appending each node’s value to the result list.
  - Use a marker (e.g., `"#"`) for `null` nodes to preserve the tree structure.
  - Join the result list into a single string.
- For deserialization:
  - Split the string back into a list.
  - Reconstruct the tree level by level using a queue.
  - Assign left and right children as we traverse the list.

**Hinglish:**  
Hum **BFS** ka use karke tree ko serialize aur deserialize karte hain:
- **Serialize:**
  - BFS karte hue har node ki value result me add karte hain.
  - `null` nodes ke liye `"#"` ka marker lagate hain taaki structure preserve rahe.
  - Result list ko ek string me join kar dete hain.
- **Deserialize:**
  - String ko split karke list banate hain.
  - BFS karte hue tree ko wapas reconstruct karte hain.
  - Queue me se nodes lete hain aur unke left aur right set karte hain.

---

#### Example
Input Tree:  
```
      1
     / \
    2   3
       / \
      4   5
```

Serialized String:  
```
"1 2 3 # # 4 5 # # # #"
```

Deserialized Tree:  
Same as the input tree.

---

#### Code
```python
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string."""
        if not root:
            return ""
        res = []
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("#")  # marker for null
        return ' '.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        if not data:
            return None
        nodes = data.split()
        root = TreeNode(int(nodes[0]))
        queue = deque([root])
        i = 1
        while queue:
            node = queue.popleft()
            if nodes[i] != "#":
                node.left = TreeNode(int(nodes[i]))
                queue.append(node.left)
            i += 1
            if nodes[i] != "#":
                node.right = TreeNode(int(nodes[i]))
                queue.append(node.right)
            i += 1
        return root
```

---

#### Complexity
- **Time Complexity:**
  - Serialization: `O(N)`
  - Deserialization: `O(N)`
  where `N` is the number of nodes in the tree.
- **Space Complexity:** `O(N)` — for the queue and result list.

---

### 28. Morris Inorder Traversal of Binary Tree

#### Problem Statement
Implement **Morris Inorder Traversal** of a binary tree.  
This algorithm performs an inorder traversal of a binary tree in **O(1) extra space** (i.e., without recursion or stack), while modifying the tree temporarily.

---

#### Approach
**English:**  
We solve this using the **Morris Traversal technique**:
- At each node:
  - If the left child is `None`, visit the current node and move to the right child.
  - Otherwise, find the inorder predecessor (`Ip`) of the current node in the left subtree.
    - If `Ip.right` is `None`, create a temporary thread from `Ip.right` to `curr` and move to `curr.left`.
    - If `Ip.right` already points to `curr`, remove the thread, visit `curr`, and move to `curr.right`.
- Continue this process until `curr` becomes `None`.
- The tree is restored to its original state as all temporary threads are removed during the traversal.

**Hinglish:**  
Hum **Morris Traversal** ka use karke binary tree ka inorder traversal karte hain bina stack ya recursion ke:
- Har node par:
  - Agar left child `None` ho to current node ko visit karte hain aur `right` me chalte hain.
  - Warna left subtree me current node ka inorder predecessor (`Ip`) dhundte hain.
    - Agar `Ip.right` `None` ho to ek temporary thread bana dete hain (`Ip.right = curr`) aur `left` me chalte hain.
    - Agar `Ip.right` already `curr` ho to thread tod dete hain, node visit karte hain aur `right` me chalte hain.
- Jab tak `curr` `None` nahi ho jata ye process chalta rahega.
- Traversal ke baad tree wapas apni original state me aa jata hai.

---

#### Example
Input Tree:  
```
      1
     / \
    2   3
   / \
  4   5
```

Inorder Traversal Output:  
```
[4, 2, 5, 1, 3]
```

---

#### Code
```python
def morrisInorder(root):
    ans = []
    curr = root

    while curr:
        if not curr.left:
            ans.append(curr.val)
            curr = curr.right
        else:
            # Find the inorder predecessor (rightmost in left subtree)
            Ip = curr.left
            while Ip.right and Ip.right != curr:
                Ip = Ip.right
            
            if not Ip.right:
                # Make a temporary thread to current
                Ip.right = curr
                curr = curr.left
            else:
                # Thread already exists; remove it
                Ip.right = None
                ans.append(curr.val)
                curr = curr.right

    return ans
```

---

#### Complexity
- **Time Complexity:** `O(N)` — each node is visited at most twice.
- **Space Complexity:** `O(1)` — no stack or recursion, only a few pointers.

---

### 29. Morris Inorder Traversal of Binary Tree

#### Problem Statement
Implement **Morris Inorder Traversal** of a binary tree.  
This algorithm performs an inorder traversal of a binary tree in **O(1) extra space**, without using recursion or a stack.

---

#### Approach
**English:**  
We solve this using the **Morris Traversal technique**:
- Start at the root.
- While the current node is not `None`:
  - If the current node has no left child:
    - Visit (add to result) the current node.
    - Move to the right child.
  - Else:
    - Find the **inorder predecessor** (`Ip`) of the current node in its left subtree.
    - If `Ip.right` is `None`:
      - Create a temporary thread (`Ip.right = curr`) and move to `curr.left`.
    - Else (thread already exists):
      - Remove the thread (`Ip.right = None`), visit the current node, and move to `curr.right`.
- The tree structure is restored to its original form as we remove all temporary threads.

**Hinglish:**  
Hum **Morris Traversal** ka use karte hain:
- Root se start karte hain.
- Jab tak current node `None` nahi hoti:
  - Agar current node ka left child nahi hai:
    - Node ko visit karte hain aur `right` child me move karte hain.
  - Warna:
    - Left subtree me current node ka **inorder predecessor (`Ip`)** dhoondte hain.
    - Agar `Ip.right` `None` hai:
      - Ek temporary thread bana kar `curr.left` me move karte hain.
    - Agar `Ip.right` already `curr` hai:
      - Thread ko todte hain, node visit karte hain aur `curr.right` me move karte hain.
- Sab threads remove ho jaate hain, aur tree wapas original ban jaata hai.

---

#### Example
Input Tree:  
```
      1
     / \
    2   3
   / \
  4   5
```

Inorder Traversal Output:  
```
[4, 2, 5, 1, 3]
```

---

#### Code
```python
def morrisInorder(root):
    ans = []
    curr = root

    while curr:
        if not curr.left:
            ans.append(curr.val)
            curr = curr.right
        else:
            # Find the inorder predecessor (rightmost in left subtree)
            Ip = curr.left
            while Ip.right and Ip.right != curr:
                Ip = Ip.right
            
            if not Ip.right:
                # Make a temporary thread to current
                Ip.right = curr
                curr = curr.left
            else:
                # Thread already exists; remove it
                Ip.right = None
                ans.append(curr.val)
                curr = curr.right

    return ans
```

---

#### Complexity
- **Time Complexity:** `O(N)` — each edge is traversed at most twice.
- **Space Complexity:** `O(1)` — no recursion or stack, just pointers.

---

### 30. Flatten Binary Tree to Linked List

#### Problem Statement
Given the root of a binary tree, flatten it into a **linked list in-place**.  
The linked list should use the right pointers of the tree nodes to form a path that follows the **preorder traversal** of the binary tree.  
The left pointers of all nodes should be set to `None`.

---

#### Approach
**English:**  
We solve this using **Reverse Postorder Traversal (Right → Left → Root)**:
- We maintain a `prev` pointer that always points to the previously processed node.
- Recursively traverse the tree in reverse postorder.
- At each node:
  - Set `root.right = prev`.
  - Set `root.left = None`.
  - Update `prev = root`.
- The recursion modifies the tree in-place to flatten it into a linked list.

**Hinglish:**  
Hum **Reverse Postorder Traversal (Right → Left → Root)** ka use karte hain:
- Ek `prev` pointer maintain karte hain jo pehle se processed node ko point karta hai.
- Recursively tree ko right → left → root order me traverse karte hain.
- Har node par:
  - `root.right = prev` set karte hain.
  - `root.left = None` kar dete hain.
  - `prev = root` update karte hain.
- Tree ko in-place modify karke linked list me badal dete hain.

---

#### Example
Input Tree:  
```
      1
     / \
    2   5
   / \   \
  3   4   6
```

Flattened Linked List:  
```
1 - 2 - 3 - 4 - 5 - 6
```

---

#### Code
```python
def flattenTree(root):
    prev = None
    def flatten(root):
        nonlocal prev
        if not root:
            return
        flatten(root.right)
        flatten(root.left)
        root.right = prev
        root.left = None
        prev = root
        return root
    flatten(root)
```

---

#### Complexity
- **Time Complexity:** `O(N)` — each node is visited once.
- **Space Complexity:** `O(H)` — due to recursion stack, where `H` is the height of the tree.

---

### 31. Check if Binary Tree is Symmetric

#### Problem Statement
Given the root of a binary tree, check whether it is **symmetric around its center**, i.e., whether it is a mirror of itself.

---

#### Approach
**English:**  
We solve this using recursion:
- A tree is symmetric if its left and right subtrees are **mirror images** of each other.
- Define a helper function `isMirror(t1, t2)`:
  - If both `t1` and `t2` are `None`, return `True`.
  - If only one of them is `None`, return `False`.
  - Otherwise:
    - Their values must be equal.
    - `t1.left` must be a mirror of `t2.right`.
    - `t1.right` must be a mirror of `t2.left`.
- Finally, call `isMirror(root.left, root.right)` to check symmetry.

**Hinglish:**  
Hum recursion ka use karke check karte hain:
- Tree tab symmetric hota hai jab uska left aur right subtree ek dusre ka mirror ho.
- Ek helper function `isMirror(t1, t2)` banate hain:
  - Agar dono `None` hain to `True` return.
  - Agar ek `None` ho aur doosra nahi to `False` return.
  - Warna:
    - Unki values barabar honi chahiye.
    - `t1.left` aur `t2.right` mirror honi chahiye.
    - `t1.right` aur `t2.left` mirror honi chahiye.
- Aakhir me `isMirror(root.left, root.right)` call karke symmetry check karte hain.

---

#### Example
Input Tree:  
```
      1
     / \
    2   2
   / \ / \
  3  4 4  3
```

Output:  
```
True
```

---

#### Code
```python
def isSymmetric(root):
    if not root:
        return True

    def isMirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.value == t2.value and
                isMirror(t1.left, t2.right) and
                isMirror(t1.right, t2.left))

    return isMirror(root.left, root.right)
```

---

#### Complexity
- **Time Complexity:** `O(N)` — each node is visited once.
- **Space Complexity:** `O(H)` — due to recursion stack, where `H` is the height of the tree.

---
