# 1005. Splitting weights into two piles

[Timus 1005](https://acm.timus.ru/problem.aspx?space=1&num=1005) · difficulty 78 · dp, bitmask, bruteforce

Original problem from the Ural State University Championship 1997.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given `n` positive integers `w1, ..., wn` (`1 ≤ n ≤ 20`,
`1 ≤ wi ≤ 100 000`), split them into two groups so that the difference
between the sums of the groups is as small as possible. Output that
difference. A group may be empty.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The number `n` and then the `n` weights, separated by whitespace.

## Output

One integer: the minimal possible difference.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
5
5 8 13 27 14
```

Output:

```
3
```

### Example 2

Input:

```
1
100000
```

Output:

```
100000
```

## Solution

If one group weighs `s`, the other weighs `total - s` and the difference is
`|total - 2s|`. So the task is to find the subset sum `s ≤ total / 2` closest
to `total / 2`.

**Subset sums (dp).** `reach[s]` tells whether some weights sum to exactly
`s`; start with `reach[0]` and add the weights one by one, going over `s`
downwards so that each weight is used at most once. Only sums up to
`total / 2 ≤ 1 000 000` matter, so this is at most `20 · 10^6` steps and
`O(total)` memory. The answer comes from the largest reachable `s ≤ total / 2`.

**Bitset (dp, bitmask).** The same table fits in one integer whose bit `s` is
`reach[s]`: adding a weight `x` is `reach |= reach << x`. In Python, with its
arbitrary-precision integers, this runs on whole machine words at a time and is
much faster than a loop over `s`.

**All subsets (bruteforce, bitmask).** With `n ≤ 20` all `2^20` subsets can be
listed. In Gray code order every next subset differs from the previous one in
one weight, so the sum is updated in `O(1)`; the last weight can stay in the
second group, which halves the work. `O(2^n)` time.

Pitfalls:

- the total is up to `2 · 10^6`: `int` is enough, but a table over all sums up
  to `total` wastes memory; `total / 2` is enough;
- `n = 1`: the answer is the only weight.

## Language notes

- **C++**, **Go**, **Java**, **Rust**: the boolean subset-sum table, about
  `2 · 10^7` simple steps.
- **C++** also has the Gray code enumeration of all subsets.
- **Python**: the big-integer bitset; a plain double loop over the weights and
  sums would be far too slow.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1005_bruteforce_bitmask.cpp](1005_bruteforce_bitmask.cpp) | G++ 13.2 x64 | bruteforce, bitmask | O(2^(n-1)) | AC | 0.015 s | 200 KB |
| [1005_dp.cpp](1005_dp.cpp) | G++ 13.2 x64 | dp | O(n·S) | AC | 0.015 s | 1124 KB |
| [1005_dp.go](1005_dp.go) | Go 1.14 x64 | dp | O(n·S) | AC | 0.062 s | 2000 KB |
| [1005_dp.java](1005_dp.java) | Java 1.8 | dp | O(n·S) | AC | 0.140 s | 1388 KB |
| [1005_dp.rs](1005_dp.rs) | Rust 1.75 x64 | dp | O(n·S) | AC | 0.031 s | 1144 KB |
| [1005_dp_bitmask.py](1005_dp_bitmask.py) | Python 3.12 x64 | dp, bitmask | O(n·S/64) | AC | 0.093 s | 920 KB |
