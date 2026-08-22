# Day 4 — 80. Remove Duplicates from Sorted Array II

## Problem

Given a sorted integer array `nums`, remove duplicates in-place so that each unique element appears at most twice. Return the number of valid elements `k`.

## Core idea

This is a direct extension of Day 3.

- Day 3: each value may appear at most once.
- Day 4: each value may appear at most twice.

Use two pointers:

- `read`: scans the original array.
- `write`: points to the next position where a valid value should be written.

Because the first two elements are always allowed, initialize:

```python
read = 2
write = 2
```

For every later element, compare it with the element two positions before the current write position:

```python
nums[read] != nums[write - 2]
```

If they are different, the current value has appeared fewer than two times in the valid prefix, so it can be kept.

If they are equal, keeping it would create a third occurrence, so skip it.

## Why `write - 2` works

`write` is the length of the valid prefix, so `nums[write - 2]` is the second-last retained element.

If the current value is equal to `nums[write - 2]`, then the valid prefix already contains at least two copies of that value.

Example:

```text
valid prefix: [1, 2, 3, 3]
write = 4

nums[write - 2] = nums[2] = 3
```

If the next value is also `3`, it must be skipped.

This also explains why a value that has appeared only once is still allowed a second time. For example, with a valid prefix `[1, 2, 3]`, `write = 3`, so `nums[write - 2] = nums[1] = 2`. A new `3` is different from `2`, so the second `3` is kept.

## Edge case

The initial version started with:

```python
read = 2
write = 2
```

That fails for arrays of length 0 or 1 because returning `write` would incorrectly return `2`.

So handle short arrays first:

```python
if len(nums) <= 2:
    return len(nums)
```

## Final solution

```python
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        read = 2
        write = 2

        while read < len(nums):
            if nums[read] == nums[write - 2]:
                read += 1
            else:
                nums[write] = nums[read]
                read += 1
                write += 1

        return write
```

## Connection to Day 3

Day 3 used:

```python
nums[read] != nums[write - 1]
```

because only one copy was allowed.

Day 4 uses:

```python
nums[read] != nums[write - 2]
```

because up to two copies are allowed.

General pattern:

```text
at most 1 copy  -> compare with nums[write - 1]
at most 2 copies -> compare with nums[write - 2]
at most k copies -> compare with nums[write - k]
```

## Python concepts reviewed

- `len(nums)`
- list indexing such as `nums[write - 2]`
- in-place assignment: `nums[write] = nums[read]`
- `while` loops
- `+= 1`
- early return for edge cases

## Algorithm concepts

- Two pointers
- Read/write pointer pattern
- In-place array modification
- Exploiting sorted-array structure
- Edge-case handling

## Complexity

- Time: `O(n)`
- Extra space: `O(1)`

## Main learning point

The important idea is not memorizing `write - 2`, but understanding that `write` describes the current valid prefix. Looking back `k` positions from `write` tells us whether adding the current value would exceed the allowed duplicate count.
