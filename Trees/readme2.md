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
