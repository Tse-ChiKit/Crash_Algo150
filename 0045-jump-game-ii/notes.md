# Day 10 - 45. Jump Game II

## Problem

Given an integer array `nums`, where `nums[i]` is the maximum jump length from index `i`, return the minimum number of jumps needed to reach the last index. The problem guarantees that the last index is reachable.

## Core idea: Greedy by ranges

This problem is related to Day 9's Jump Game, but the goal is different:

- Day 9 asks whether the last index is reachable.
- Day 10 asks for the minimum number of jumps.

Instead of choosing one exact next index at each step, we think in terms of reachable ranges.

Maintain three variables:

```python
jumps = 0
current_end = 0
farthest = 0
```

Meaning:

- `jumps`: how many jumps have been used so far.
- `current_end`: the right boundary reachable with the current number of jumps.
- `farthest`: while scanning the current range, the farthest index the next jump could reach.

## Why `i + nums[i]`?

`i` is the current array index.

`nums[i]` is the maximum jump length from index `i`.

Therefore:

```python
i + nums[i]
```

is the farthest index reachable from `i`.

Example:

```text
nums = [2,3,1,1,4]

at i = 1:
nums[1] = 3
1 + 3 = 4
```

So from index 1, the farthest reachable index is 4.

## Why keep `farthest`?

Within the current reachable range, there may be several possible positions to jump from.

Example:

```text
nums = [2,3,1,1,4]
```

From index 0, one jump can reach index 1 or 2.

Check both:

```text
index 1 -> 1 + nums[1] = 4
index 2 -> 2 + nums[2] = 3
```

So the next jump can extend the reachable boundary as far as index 4.

We do not need to commit to a concrete path immediately. We only need the best boundary extension:

```python
farthest = max(farthest, i + nums[i])
```

## Why `if i == current_end`?

`current_end` is the right boundary of the current jump layer.

When:

```python
if i == current_end:
```

it means we have finished scanning every position reachable using the current number of jumps.

At that moment, we must move to the next jump layer:

```python
jumps += 1
current_end = farthest
```

Important distinction:

```text
farthest
= updated continuously while scanning the current range

current_end
= updated only when the current range has been fully scanned
```

## Example requiring multiple jumps

```text
nums = [2,1,2,1,1,1,4]
```

Start:

```text
jumps = 0
current_end = 0
farthest = 0
```

### i = 0

```text
farthest = max(0, 0 + 2) = 2
```

Since:

```text
i == current_end
0 == 0
```

we complete the first jump layer:

```text
jumps = 1
current_end = 2
```

Now one jump can cover indices up to 2.

### Scan i = 1 and i = 2

```text
i = 1 -> 1 + 1 = 2
i = 2 -> 2 + 2 = 4
```

So:

```text
farthest = 4
```

At `i = 2`, we again hit the current boundary:

```text
jumps = 2
current_end = 4
```

Continue the same process until the final index is covered.

## Why loop only to `len(nums) - 2`?

The standard loop is:

```python
for i in range(len(nums) - 1):
```

The final index only needs to be reached. It never needs to be used as a starting point for another jump.

If the last index were also processed, `i == current_end` could cause an unnecessary extra `jumps += 1`.

So we only scan possible jump-start positions, not the final destination.

## Accepted solution

```python
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, nums[i] + i)

            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps
```

## Mistakes encountered

### 1. `current_end += farthest`

Incorrect:

```python
current_end += farthest
```

`farthest` is already an absolute array index, not a distance.

Correct:

```python
current_end = farthest
```

### 2. Returning `farthest`

The problem asks for the number of jumps, so the return value must be:

```python
return jumps
```

not:

```python
return farthest
```

## Complexity

- Time: `O(n)`
- Space: `O(1)`

The array is scanned once, and only a few integer variables are maintained.

## Day 9 vs Day 10

### Jump Game I

Track:

```python
max_reach
```

Question:

> Can I still reach the current index / final index?

### Jump Game II

Track:

```python
current_end
farthest
jumps
```

Question:

> How many reachable ranges / jump layers are needed to cover the final index?

## Key takeaway

Do not think primarily in terms of a concrete jump path.

Think in terms of layers:

```text
current_end = boundary of the current jump layer
farthest    = best boundary for the next jump layer
```

When the scan reaches `current_end`, one jump layer is complete, so increment `jumps` and move the boundary to `farthest`.
