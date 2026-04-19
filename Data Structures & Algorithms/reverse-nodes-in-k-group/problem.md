---
tags:
 - Linked-List
 - Recursion

created: 2026-04-19

---

## Notes

<!-- Add your thoughts, edge cases, mistakes -->

---

# **Reverse Nodes in K-Group**

You are given the head of a singly linked list `head` and a positive integer `k`.

You must reverse the first `k` nodes in the linked list, and then reverse the next `k` nodes, and so on. If there are fewer than `k` nodes left, leave the nodes as they are.

Return the modified list after reversing the nodes in each group of `k`.

You are only allowed to modify the nodes' `next` pointers, not the values of the nodes.

**Example 1:**



```
Input: head = [1,2,3,4,5,6], k = 3

Output: [3,2,1,6,5,4]
```

**Example 2:**



```
Input: head = [1,2,3,4,5], k = 3

Output: [3,2,1,4,5]
```

**Constraints:**

- The length of the linked list is n.
- $1 <= k <= n <= 100$
- $0 <= Node.val <= 100$



### Topics

Linked List
Recursion


### Recommended Time & Space Complexity

You should aim for a solution with O(n) time and O(1) space, where n is the length of the given list.


### Hint 1

A brute-force solution would involve storing the linked list node values in an array, reversing the k groups one by one, and then converting the array back into a linked list, requiring extra space of O(n). Can you think of a better way? Perhaps you could apply the idea of reversing a linked list in-place without using extra space.


### Hint 2

We can avoid extra space by reversing each group in-place while keeping track of the head of the next group. For example, consider the list [1, 2, 3, 4, 5] with k = 2. First, we reverse the group [1, 2] to [2, 1]. Then, we reverse [3, 4], resulting in [2, 1, 4, 3, 5]. While reversing [3, 4], we need to link 1 to 4 and also link 3 to 5. How can we efficiently manage these pointers?


### Hint 3

We create a dummy node to handle modifications to the head of the linked list, pointing its next pointer to the current head. We then iterate k nodes, storing the address of the next group's head and tracking the tail of the previous group. After reversing the current group, we reconnect it by linking the previous group's tail to the new head and the current group's tail to the next group's head. This process is repeated for all groups, and we return the new head of the linked list.
    