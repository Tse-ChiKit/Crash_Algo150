# Day 9 - 55. Jump Game

## Problem

Given an integer array `nums`, where `nums[i]` represents the maximum jump length from index `i`, determine whether it is possible to reach the last index starting from index `0`.

Example:

```text
nums = [2,3,1,1,4]
```

One valid path is:

```text
0 -> 1 -> 4
```

So the answer is `True`.

For:

```text
nums = [3,2,1,0,4]
```

index `3` is reachable, but its value is `0`, so the reachable range cannot extend to index `4`. The answer is `False`.

## Initial thought

A natural first idea is to always jump as far as possible from the current position.

However, this greedy choice is not always correct.

Example:

```text
nums = [2,3,0,1,4]
```

If we always take the maximum jump from index `0`, we jump directly to index `2`, where the value is `0`, and get stuck.

But jumping only one step first works:

```text
0 -> 1 -> 4
```

So the problem should not be modeled as choosing one exact jump at every step.

## Better greedy idea: track the farthest reachable index

Instead of deciding where to jump, maintain:

```python
max_reach
```

which means:

> The farthest index that can be reached using all positions processed so far.

At each index `i`, first check whether `i` itself is reachable.

```python
if i > max_reach:
    return False
```

If `i` is beyond the farthest reachable position, then it is impossible to stand at `i`, so `nums[i]` cannot help us anymore.

If `i` is reachable, use it to extend the reachable range:

```python
max_reach = max(max_reach, i + nums[i])
```

## Why `i == max_reach` is still okay

`i == max_reach` does not mean failure.

It means the current index is exactly at the current reachable boundary, but it is still reachable.

Example:

```text
nums = [2,0,2]
```

At index `2`:

```text
i = 2
max_reach = 2
```

The position is reachable, and it is already the final index.

The failure condition is only:

```python
i > max_reach
```

## Important order of operations

The check must happen before updating `max_reach`:

```python
for i in range(len(nums)):
    if i > max_reach:
        return False

    max_reach = max(max_reach, i + nums[i])
```

Why?

Using:

```text
nums = [3,2,1,0,4]
```

we eventually get:

```text
i = 3
max_reach = 3
```

Index `3` is reachable, but it cannot extend the range because `nums[3] = 0`.

The next loop has:

```text
i = 4
max_reach = 3
```

Since `4 > 3`, index `4` is unreachable, so we must return `False` immediately.

It would be incorrect to compute:

```python
max_reach = max(3, 4 + nums[4])
```

because we never had the ability to reach index `4` in the first place.

A useful interpretation is:

> First check whether I am allowed to stand here; only then use this position to jump farther.

## Accepted solution

```python
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach:
                return False

            max_reach = max(max_reach, i + nums[i])

        return True
```

## Walkthrough

For:

```text
nums = [2,3,1,1,4]
```

```text
i = 0
max_reach = max(0, 0 + 2) = 2

 i = 1
1 <= 2, reachable
max_reach = max(2, 1 + 3) = 4
```

Now the final index is already within the reachable range.

For:

```text
nums = [3,2,1,0,4]
```

```text
i = 0 -> max_reach = 3
i = 1 -> max_reach = 3
i = 2 -> max_reach = 3
i = 3 -> max_reach = 3
i = 4 -> 4 > 3 -> False
```

## Complexity

- Time: `O(n)`
- Space: `O(1)`

The array is scanned once and only one main state variable is maintained.

## Key takeaway

The important greedy shift is:

> Do not choose an exact jump. Track the farthest reachable boundary instead.

At every position:

1. Check whether the current index is reachable.
2. If reachable, use it to extend `max_reach`.
3. If the current index is beyond `max_reach`, the game is already lost.

This is another example of a broader pattern seen in greedy problems: instead of storing every possible path, keep only the best boundary or best state needed for future decisions.
