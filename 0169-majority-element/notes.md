# Day 5 - 169. Majority Element

## Problem

Given an integer array `nums`, return the majority element. The majority element is the element that appears more than `n / 2` times. The problem guarantees that a majority element always exists.

## My first approach: HashMap / Python dict

The first idea was to scan from left to right and use a hash map to count how many times each number appears.

In Python, the built-in hash map structure is `dict`:

```python
count = {}
```

For every `num`:

```python
if num in count:
    count[num] += 1
else:
    count[num] = 1
```

As soon as one count is greater than `len(nums) / 2`, return that number.

## Accepted solution

```python
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

            if count[num] > len(nums) / 2:
                return num
```

## Python concepts learned

### 1. `dict` is Python's HashMap

```python
count = {}
```

### 2. Check whether a key exists

```python
if num in count:
```

### 3. Update the value associated with a key

```python
count[num] += 1
```

### 4. A shorter counting pattern

The following is equivalent to the `if/else` counting code:

```python
count[num] = count.get(num, 0) + 1
```

`dict.get(key, default)` returns the value if the key exists; otherwise it returns the supplied default value.

### 5. Python 3 division

```python
len(nums) / 2
```

uses true division and returns a float. For example:

```python
5 / 2 == 2.5
```

That is fine here because the condition is `count[num] > len(nums) / 2`.

## Complexity of HashMap solution

- Time: `O(n)`
- Space: `O(n)` in the worst case

The array is scanned once, but the dictionary may store many distinct values.

## Optimization: Boyer-Moore Voting Algorithm

The HashMap approach is easy to understand, but this problem can be solved with `O(1)` extra space.

The Boyer-Moore idea is to let different elements cancel each other out.

Maintain:

```python
candidate = None
count = 0
```

Rules:

1. If `count == 0`, choose the current number as the new `candidate`.
2. If the current number equals `candidate`, increment `count`.
3. Otherwise decrement `count`.

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
```

### Why it works

The majority element appears more than half of the time. Therefore its frequency is greater than the combined count of all non-majority elements.

We can think of every majority element cancelling one different element. Even after all possible cancellations, at least one majority element must remain, so the final `candidate` is the majority element.

Example:

```text
[2, 2, 1, 1, 1, 2, 2]

2 and 1 cancel
2 and 1 cancel
1 and 2 cancel
one 2 remains
```

This works directly here because the problem guarantees that a majority element exists.

If a majority element were not guaranteed to exist, the Boyer-Moore candidate would need a second pass to verify that it really appears more than `n / 2` times.

## Complexity comparison

| Approach | Time | Extra Space |
| --- | --- | --- |
| HashMap / `dict` | `O(n)` | `O(n)` |
| Boyer-Moore | `O(n)` | `O(1)` |

## Key takeaway

Two useful ways to think about this problem:

- HashMap: **count frequencies**.
- Boyer-Moore: **cancel different elements**.

The HashMap solution was the first solution derived independently and was useful for learning Python dictionaries. Boyer-Moore is the important algorithmic optimization to remember for this specific majority-element pattern.
