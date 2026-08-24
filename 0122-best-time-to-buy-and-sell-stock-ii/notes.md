# Day 8 - 122. Best Time to Buy and Sell Stock II

## Problem

Given an integer array `prices`, where `prices[i]` is the stock price on day `i`, return the maximum profit you can achieve.

Unlike Day 7 / LeetCode 121, this problem allows multiple transactions, but you can only hold at most one share at a time. You must sell before buying again.

## First intuition

The first idea was to start from each index as a possible buy day, scan forward for higher prices, sell, buy again, and repeat. This would lead toward repeated scanning and potentially `O(n^2)` work.

The important observation is that because multiple transactions are allowed, we do not need to search all possible buy/sell pairs.

## Core greedy idea

Whenever the next day's price is higher than today's price, we can safely take that positive difference as profit.

```python
if prices[i + 1] > prices[i]:
    profit += prices[i + 1] - prices[i]
```

Example:

```text
prices = [7, 1, 5, 3, 6, 4]

7 -> 1   difference = -6  ignore
1 -> 5   difference = +4  take it
5 -> 3   difference = -2  ignore
3 -> 6   difference = +3  take it
6 -> 4   difference = -2  ignore

profit = 4 + 3 = 7
```

This is equivalent to the actual transactions:

```text
buy at 1 -> sell at 5 = 4
buy at 3 -> sell at 6 = 3

total = 7
```

## Why checking only adjacent days works

A continuous rising interval can always be decomposed into the sum of adjacent positive differences.

For example:

```text
[1, 2, 4]
```

Buying at `1` and selling at `4` gives:

```text
4 - 1 = 3
```

Taking every adjacent rise gives:

```text
(2 - 1) + (4 - 2)
= 1 + 2
= 3
```

So:

```text
4 - 1 = (2 - 1) + (4 - 2)
```

This is why we do not need to skip indexes or explicitly search for a valley and a later peak. Summing every positive adjacent difference already captures the full profit of each rising segment.

General form:

```text
[a, b, c, d]

d - a
= (b - a) + (c - b) + (d - c)
```

as long as the whole segment is increasing.

## Accepted solution

```python
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        i = 0
        while i < len(prices) - 1:
            if prices[i + 1] > prices[i]:
                profit += prices[i + 1] - prices[i]

            i += 1

        return profit
```

## Python concepts learned

### 1. Compare explicitly instead of relying on truthiness of a difference

This was an important bug during the first attempt:

```python
if prices[i] - prices[i + 1]:
```

This does **not** mean the first price is larger. It only checks whether the difference is non-zero.

For example:

```python
if 3 - 5:
```

`3 - 5 == -2`, and `-2` is truthy in Python, so the condition would still run.

To test whether the next price is higher, write the comparison explicitly:

```python
if prices[i + 1] > prices[i]:
```

### 2. Direction of subtraction matters

Profit is:

```python
sell_price - buy_price
```

For two adjacent days:

```python
prices[i + 1] - prices[i]
```

not the other way around.

### 3. Remember to update a `while` loop counter

The first draft omitted:

```python
i += 1
```

Without this line, `i` stays at `0` forever and the loop becomes an infinite loop.

### 4. Loop boundary

Because the code accesses:

```python
prices[i + 1]
```

`i` must stop before the final index.

Therefore:

```python
while i < len(prices) - 1:
```

is safe.

## Complexity

- Time: `O(n)`
- Extra Space: `O(1)`

We scan the array once and only store the running `profit` and index `i`.

## Greedy pattern

This is an important greedy algorithm pattern:

> When every locally positive gain can be taken without preventing a better future decision, take every positive local gain.

For this stock problem:

```python
profit += max(0, prices[i + 1] - prices[i])
```

is another compact way to express the same idea.

## Day 7 vs Day 8

### Day 7 - LeetCode 121

Only one transaction is allowed.

We need to remember the minimum historical buy price and maximize one final buy/sell pair.

```text
min_price + max_profit
```

### Day 8 - LeetCode 122

Multiple transactions are allowed.

We can collect every positive adjacent price difference.

```text
sum of all positive daily differences
```

## Key takeaway

The most important realization from Day 8 is:

> A long rising interval can be split into multiple adjacent rising intervals without changing total profit.

Therefore:

```text
[1, 2, 4]

1 -> 4 profit = 3

is equivalent to

1 -> 2 profit = 1
2 -> 4 profit = 2

total = 3
```

This mathematical decomposition is why the greedy `O(n)` solution works.
