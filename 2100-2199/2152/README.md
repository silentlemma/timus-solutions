# 2152. Raising customs duties by changing one digit in k parcels

[Timus 2152](https://acm.timus.ru/problem.aspx?space=1&num=2152) · difficulty 1149 · greedy, sorting

Original problem by Ivan Sychev, from the Ural School Programming Contest 2020.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A parcel pays a credits per kilogram of weight above mxw and b percent
of every credit of price above mxp. Changing exactly one digit of the
weight or of the price is allowed for at most k of the n parcels.
Maximize the total duty and print it with the new data of every parcel.
Any optimal set of changes is accepted. The limits are 1 second and
256 MB.

## Input

n and k, 1 ≤ n ≤ 2 · 10⁵, 0 ≤ k ≤ n, then mxw, mxp, a, b with
1 ≤ mxw, mxp, a ≤ 10⁹ and 1 ≤ b ≤ 100, then the weights and prices, from
1 to 10⁹.

## Output

The largest total duty, then the weight and price of every parcel.

## Checking

A checker verifies the total within 10⁻⁹ absolute or relative error,
that the changes are allowed, and that the printed data give that total.
For a reported total x and the correct total y, the tolerance is
|x − y| ≤ 10⁻⁹ × max(1, |y|).

## Examples

### Example 1

Input:

```
4 2
30 500 4 30
6 1100
60 90
9 990
91 420
```

Output:

```
3217.000000000
6 9100
60 90
9 990
91 920
```

## Solution

The duty only grows with the weight and the price, so a parcel's best
change makes one of the two numbers as large as possible: turn its
first digit that is not 9 into 9. Compare the gain of doing that to the
weight with the gain for the price and keep the better one; a number of
all nines cannot grow.

The parcels do not affect each other, so take the k largest positive
gains after sorting. All amounts are kept in hundredths of a credit as
integers, since b percent of a whole number of credits has at most two
decimals, so the total is exact. The work is O(n log n).

In the example the price 1100 becomes 9100 and 420 becomes 920, the two
largest gains.

## Language notes

- Python runs under PyPy: under CPython 3.12 it exceeds the time limit on
  test 9 (1.015 s), while PyPy 3.10 is accepted in 0.281 s.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2152_greedy_sorting.cpp](2152_greedy_sorting.cpp) | G++ 13.2 x64 | greedy, sorting | O(n log n) | AC | 0.140 s | 16016 KB |
| [2152_greedy_sorting.go](2152_greedy_sorting.go) | Go 1.14 x64 | greedy, sorting | O(n log n) | AC | 0.140 s | 23532 KB |
| [2152_greedy_sorting.java](2152_greedy_sorting.java) | Java 1.8 | greedy, sorting | O(n log n) | AC | 0.281 s | 24904 KB |
| [2152_greedy_sorting.py](2152_greedy_sorting.py) | PyPy 3.10 x64 | greedy, sorting | O(n log n) | AC | 0.281 s | 18812 KB |
| [2152_greedy_sorting.rs](2152_greedy_sorting.rs) | Rust 1.75 x64 | greedy, sorting | O(n log n) | AC | 0.062 s | 19692 KB |
