# Day 7 - 121. Best Time to Buy and Sell Stock

## Problem

Given an array `prices`, where `prices[i]` is the price of a stock on day `i`, choose one day to buy and a later day to sell in order to maximize profit.

If no profitable transaction is possible, return `0`.

## First idea: Brute force

The first idea was:

1. Buy on the first day.
2. Try selling on every later day and track the best profit.
3. Move the buy day forward by one.
4. Repeat until all buy/sell combinations have been checked.

This corresponds to two nested loops:

```python
for buy in range(len(prices)):
    for sell in range(buy + 1, len(prices)):
        profit = prices[sell] - prices[buy]
```

Complexity:

- Time: `O(n^2)`
- Space: `O(1)`

The logic is correct, but it repeats a lot of work.

## Optimization idea

When looking at the current day's price, we do not need to compare it with every previous day.

We only need to know:

- the lowest price seen so far: `min_price`
- the best profit seen so far: `max_profit`

For every current `price`:

```python
profit = price - min_price
```

If that profit is better than the current `max_profit`, update it.

Then update the minimum price seen so far:

```python
min_price = min(min_price, price)
```

## Accepted solution

```python
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            max_profit = max(price - min_price, max_profit)
            min_price = min(min_price, price)

        return max_profit
```

## Step-by-step example

For:

```text
prices = [7, 1, 5, 3, 6, 4]
```

We scan from left to right:

```text
price=7  min_price=7  max_profit=0
price=1  min_price=1  max_profit=0
price=5  min_price=1  max_profit=4
price=3  min_price=1  max_profit=4
price=6  min_price=1  max_profit=5
price=4  min_price=1  max_profit=5
```

Final answer:

```text
5
```

The best transaction is buying at `1` and selling later at `6`.

## Why this works

At each day, `min_price` represents the cheapest valid buy price seen before or on the current day.

So:

```python
price - min_price
```

represents the best profit achievable if we sell on the current day.

By checking this once per day and keeping the global maximum, we avoid trying every buy/sell pair.

## Why `max_profit` starts at 0

If prices only decrease, for example:

```text
[7, 6, 4, 3, 1]
```

there is no profitable transaction.

Starting with:

```python
max_profit = 0
```

ensures the algorithm returns `0` rather than a negative profit.

## Python concepts practiced

### 1. `min()`

```python
min_price = min(min_price, price)
```

Keeps the smaller of the current historical minimum and today's price.

### 2. `max()`

```python
max_profit = max(max_profit, price - min_price)
```

Keeps the best profit found so far.

### 3. Iterating directly over list values

```python
for price in prices:
```

If the index is not needed, iterating over values directly is cleaner than using `range(len(prices))`.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

The list is scanned only once and only two state variables are maintained.

## Key takeaway

The important pattern is:

> While scanning from left to right, keep the best information from the past that is needed to make the best decision for the current position.

For this problem:

- past information = lowest price seen so far
- current decision = profit if selling today
- global result = maximum profit seen so far

This turns a brute-force `O(n^2)` solution into an `O(n)` one-pass solution.
