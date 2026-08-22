# 26. Remove Duplicates from Sorted Array

## Day 3 Summary

### Problem Pattern
This problem is a classic in-place two-pointer problem on a sorted array.

- `read` scans the array.
- `write` points to the next position where a new unique value should be written.
- Because the array is sorted, duplicates are adjacent, so comparing the current value with the last kept value is enough.

### Core Idea
Initialize both pointers at index `1` because the first element is always kept.

```python
read = 1
write = 1
```

For each element:

- If `nums[read] == nums[write - 1]`, the value is a duplicate, so only move `read`.
- Otherwise, copy the new unique value to `nums[write]`, then advance both pointers.

```python
if nums[read] == nums[write - 1]:
    read += 1
else:
    nums[write] = nums[read]
    write += 1
    read += 1
```

At the end, `write` is also the number of unique elements, so return it.

### Why `nums[write - 1]`?
`write` always points to the next free position for a unique value. Therefore `write - 1` is the index of the last unique value that has already been kept.

### Connection to Day 2
Day 2 used the same read/write pointer structure:

- `read` scans input.
- `write` maintains the valid prefix.

The main difference is the condition:

- Day 2: keep elements where `nums[read] != val`.
- Day 3: keep elements where `nums[read] != nums[write - 1]`.

### Python Concepts Reviewed

- `len(nums)` for list length.
- List indexing: `nums[index]`.
- In-place assignment: `nums[write] = nums[read]`.
- Incrementing indices with `+= 1`.
- `while read < len(nums)` as the safe traversal condition.

### Complexity

- Time: `O(n)`
- Extra space: `O(1)`

### Today's Progress
You correctly identified all pointer movements before writing the final code:

- Duplicate found: `read += 1`, `write` stays.
- New unique value found: write `nums[read]` into `nums[write]`, then increment both.

The final submitted solution was correct without needing algorithmic correction.
