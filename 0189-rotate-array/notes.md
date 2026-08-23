# Day 6 - 189. Rotate Array

## Problem

Given an integer array `nums`, rotate the array to the right by `k` steps.

Example:

```text
nums = [1,2,3,4,5,6,7]
k = 3

result = [5,6,7,1,2,3,4]
```

## First approach: Python slicing

The first idea was to split the array into two parts:

```text
A = [1,2,3,4]
B = [5,6,7]
```

The target is:

```text
B + A
```

In Python:

```python
nums[len(nums) - k:]   # last k elements
nums[:len(nums) - k]   # remaining elements
```

Then concatenate them:

```python
nums[len(nums) - k:] + nums[:len(nums) - k]
```

### Handling k larger than the array length

Rotation is cyclic. For example:

```text
nums = [1,2]
k = 5
```

Rotating 2 times returns to the original array, so rotating 5 times is equivalent to rotating once:

```python
5 % 2 == 1
```

Therefore normalize `k` first:

```python
k = k % len(nums)
```

### Important: `nums = ...` vs `nums[:] = ...`

This is a key Python concept from this problem.

```python
nums = new_list
```

only makes the local variable `nums` point to a new list.

But LeetCode requires the original list object to be modified in-place.

So use slice assignment:

```python
nums[:] = new_list
```

Accepted slicing version:

```python
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]
```

### Complexity

- Time: `O(n)`
- Extra space: `O(n)`

The slices and concatenation create new lists.

## Optimal approach: Three reversals

To achieve `O(1)` extra space, use three in-place reversals.

For:

```text
[1,2,3,4 | 5,6,7]
          A | B
```

The target is:

```text
B + A
```

### Step 1: Reverse the whole array

```text
[1,2,3,4,5,6,7]
        ↓
[7,6,5,4,3,2,1]
```

Conceptually:

```text
A + B
↓ reverse everything
reverse(B) + reverse(A)
```

### Step 2: Reverse the first k elements

```text
[7,6,5 | 4,3,2,1]
     ↓
[5,6,7 | 4,3,2,1]
```

### Step 3: Reverse the remaining elements

```text
[5,6,7 | 4,3,2,1]
              ↓
[5,6,7 | 1,2,3,4]
```

So:

```text
A + B
→ reverse(B) + reverse(A)
→ B + A
```

## Accepted optimal solution

```python
from typing import List


class Solution:
    def reverse(self, nums: List[int], left: int, right: int) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)

        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)
```

## Python concepts learned

### 1. List slicing

```python
nums[:4]
```

means from the beginning up to index 4, excluding index 4.

```python
nums[4:]
```

means from index 4 to the end.

General form:

```python
nums[start:end]
```

includes `start` but excludes `end`.

### 2. JavaScript comparison

Equivalent JavaScript operations:

```javascript
nums.slice(0, 4)  // Python nums[:4]
nums.slice(4)     // Python nums[4:]
nums.slice(1, 4)  // Python nums[1:4]
```

JavaScript `slice()` does not modify the original array, while `splice()` does.

### 3. Tuple-style swapping

Python allows swapping without a temporary variable:

```python
nums[left], nums[right] = nums[right], nums[left]
```

### 4. Instance methods and `self`

A helper method defined inside a class needs `self` as its first parameter:

```python
def reverse(self, nums, left, right):
```

It must then be called through the current object:

```python
self.reverse(nums, 0, len(nums) - 1)
```

Calling just:

```python
reverse(nums, ...)
```

causes:

```text
NameError: name 'reverse' is not defined
```

because `reverse` is a method on the `Solution` instance, not a standalone function in the local scope.

## Complexity comparison

| Approach | Time | Extra Space |
| --- | --- | --- |
| Slicing + concatenation | `O(n)` | `O(n)` |
| Three reversals | `O(n)` | `O(1)` |

## Key takeaways

- Use `%` when an operation repeats cyclically.
- Python slicing is convenient but usually creates a new list.
- `nums[:] = ...` modifies the existing list; `nums = ...` only rebinds the variable.
- A subarray can be reversed in-place with two pointers.
- Three reversals transform `A + B` into `B + A` with constant extra space.
- Methods inside a class are usually called through `self`.
