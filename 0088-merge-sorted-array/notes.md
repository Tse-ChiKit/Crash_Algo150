# 88. Merge Sorted Array

## Day 1

Status: Accepted ✅

## Problem-solving idea

The key idea is **not** to insert elements from `nums2` into the middle of `nums1`.

Because both arrays are already sorted and `nums1` has enough empty space at the end, we can build the final sorted array **from right to left**.

Use three indices:

- `i = m - 1`: last valid element in `nums1`
- `j = n - 1`: last element in `nums2`
- `k = m + n - 1`: current position to write in `nums1`

At each step:

1. Compare `nums1[i]` and `nums2[j]`.
2. Put the larger one into `nums1[k]`.
3. Move the pointer that supplied the element one step left.
4. Always move `k` one step left.

The loop only needs to continue while `j >= 0`.

If `nums2` has been fully consumed, any remaining elements in `nums1` are already in their correct positions.

## Why backward filling works

Example:

```text
nums1 = [2, 3, 4, 0, 0, 0]
nums2 = [1, 5, 6]
```

We first compare the largest remaining values:

```text
4 vs 6 -> write 6 at the end
4 vs 5 -> write 5 before 6
4 vs 1 -> write 4
3 vs 1 -> write 3
2 vs 1 -> write 2
```

Only then does `1` go to the first position.

So we are not deciding "where should this `nums2` element be inserted?" Instead, we repeatedly decide:

> What is the largest remaining element, and put it into the current rightmost position?

## Mistakes and questions encountered

### 1. Initially tried to move both arrays with one offset

The initial idea used expressions similar to:

```python
nums1[m - 1 + i]
nums2[n - 1 - i]
```

This does not work because the two source pointers do not necessarily move together.

For example, if several elements from `nums2` are larger than `nums1[i]`, only the `nums2` pointer should move.

That is why independent pointers are needed.

### 2. Concern that a small `nums2` value would be placed into the wrong zero slot

For example:

```text
nums1 = [2, 3, 4, 0, 0, 0]
nums2 = [1, 5, 6]
```

The concern was that `1` might be placed into the first empty `0` position too early.

The important realization was that the algorithm is not inserting `nums2` values one by one. It is filling the final result from the right, so `1` stays unprocessed until all larger remaining values are placed.

### 3. Wrote to `nums1[i + 1]` instead of `nums1[k]`

Incorrect idea:

```python
nums1[i + 1] = nums1[i]
```

The correct destination is always the current output position:

```python
nums1[k] = nums1[i]
```

`i` tracks an input element. `k` tracks where the next final result should be written.

### 4. Python does not support `i--`

Incorrect:

```python
i--
```

Correct Python syntax:

```python
i -= 1
```

The same applies to `j` and `k`.

### 5. Missing colon after `else`

Incorrect:

```python
else
```

Correct:

```python
else:
```

### 6. Variable name typo

Used `num1` in some places instead of `nums1`.

Python treats them as different variable names.

## Python concepts reviewed

### List index access

```python
nums1[i]
nums2[j]
```

### In-place list assignment

```python
nums1[k] = nums2[j]
```

This changes the existing list instead of creating a new one.

### `while` loop

```python
while j >= 0:
```

Useful when pointer movement depends on conditions rather than a fixed number of iterations.

### Compound assignment

```python
i -= 1
j -= 1
k -= 1
```

### Short-circuit evaluation with `and`

```python
if i >= 0 and nums1[i] > nums2[j]:
```

Python evaluates the left side first. If `i >= 0` is false, it does not evaluate the second condition.

This prevents us from trying to use `nums1[i]` after the valid `nums1` elements have all been consumed.

## Algorithm concepts

- Two Pointers / multiple indices
- In-place array modification
- Backward traversal
- Using sorted order to avoid re-sorting

## Complexity

### Time

`O(m + n)`

Each element is processed at most once.

### Extra space

`O(1)`

The merge is performed directly inside `nums1` without creating another result array.

## Key takeaway

The most important mental model for this problem is:

> Do not insert `nums2` into `nums1`. Build the final sorted array from right to left.

Pointer responsibilities:

```text
i -> largest unprocessed valid element in nums1
j -> largest unprocessed element in nums2
k -> current output position in nums1
```
