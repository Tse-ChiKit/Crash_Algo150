# 27. Remove Element

## Day 2 Summary

### Problem goal
Given an integer array `nums` and an integer `val`, remove all occurrences of `val` **in place** and return the number `k` of remaining elements. LeetCode only requires the first `k` positions of `nums` to contain the kept elements; values after index `k - 1` do not matter.

## Core idea: read/write two pointers

Use two pointers:

- `read`: scans every element in the original array.
- `write`: points to the next position where a valid element should be written.

For every `nums[read]`:

- If `nums[read] == val`, skip it. Only move `read`.
- If `nums[read] != val`, copy it to `nums[write]`, then move both `write` and `read`.

At the end, `write` is exactly the number of valid elements, so return `write`.

```python
read = 0
write = 0

while read < len(nums):
    if nums[read] != val:
        nums[write] = nums[read]
        write += 1

    read += 1

return write
```

## Why `write` does not move when the current element equals `val`

A key misunderstanding during the solution was whether `write` should still increase when `nums[read] == val`.

It should **not**.

`write` represents the next slot for a valid element. If the current element should be removed, no valid element was produced, so the write position must stay where it is and wait for a later valid element to overwrite that slot.

Example:

```text
nums = [0, 1, 2, 2, 3]
val = 2

read  -> index 2 (value 2)
write -> index 2
```

Because `2 == val`, skip it:

```text
read moves to index 3
write stays at index 2
```

Later, when `read` reaches `3`, that value can overwrite index 2.

## No need to fill the tail with zeroes

Another question was whether positions after `write` should be replaced with `0`.

This is unnecessary. The problem only checks the first `k` elements, where `k` is the returned value. Anything after that can remain unchanged.

## Python syntax learned

### `len(nums)` instead of `nums.length`

Python lists do not have a `.length` property.

```python
len(nums)
```

returns the number of elements in the list.

### List indexing

If:

```python
len(nums) == 4
```

valid indices are:

```text
0, 1, 2, 3
```

The final valid index is therefore:

```python
len(nums) - 1
```

### Correct loop boundary

The submitted code originally used:

```python
while read <= len(nums):
```

This caused:

```text
IndexError: list index out of range
```

because when `read == len(nums)`, the code still entered the loop and attempted:

```python
nums[read]
```

which is outside the list.

The correct condition is:

```python
while read < len(nums):
```

This is a classic **off-by-one error**.

## Mistakes and corrections

### 1. Compared `nums[read]` with `nums[write]`

Original idea:

```python
if nums[read] == nums[write]:
```

But the task is not to detect duplicates. The current element must be compared with the target value:

```python
if nums[read] == val:
```

or, more compactly, keep the element when:

```python
if nums[read] != val:
```

### 2. Returned the array instead of the count

The problem requires the number of remaining elements, so the correct return value is:

```python
return write
```

not `return nums`.

### 3. Off-by-one loop condition

Wrong:

```python
while read <= len(nums):
```

Correct:

```python
while read < len(nums):
```

## Algorithm pattern

This problem introduces an important reusable pattern:

> **Read pointer scans the input; write pointer maintains the valid prefix.**

This same idea appears frequently in array problems such as removing duplicates and moving zeroes.

## Complexity

- Time: `O(n)` — each element is inspected once.
- Extra space: `O(1)` — the array is modified in place and no extra array is created.

## Day 2 status

- Problem: 27. Remove Element
- Result: Accepted
- Main topic: Two pointers / in-place array modification
- Python focus: `len()`, list indices, `while`, assignment, `+=`, loop boundaries
