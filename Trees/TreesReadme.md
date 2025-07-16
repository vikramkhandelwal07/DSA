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
