# 1031. The cheapest set of railway tickets with three fare bands

[Timus 1031](https://acm.timus.ru/problem.aspx?space=1&num=1031) · difficulty 390 · dp, two_pointers

Original problem from the Third Ural Collegiate Team Programming Championship, 1999.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`N` stations (`2 ≤ N ≤ 10 000`) lie on a line; station 1 is at distance 0
and the others at given increasing distances (at most `10^9`, neighbouring
stations at most `L3` apart). A ticket covers one ride between two stations
at distance `X`: it costs `C1` if `X ≤ L1`, `C2` if `L1 < X ≤ L2`, `C3` if
`L2 < X ≤ L3`, and longer rides need several tickets, changing at stations
(`1 ≤ L1 < L2 < L3 ≤ 10^9`, `1 ≤ C1 < C2 < C3 ≤ 10^9`). Find the cheapest
way between two given stations; the answer does not exceed `10^9`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`L1 L2 L3 C1 C2 C3`, then `N`, then the two stations (in any order), then
the `N - 1` distances of stations 2..`N` from station 1.

## Output

The smallest total price.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
3 6 8 20 30 40
7
2 6
3
5
9
12
17
19
```

Output:

```
70
```

### Example 2

Input:

```
1 2 3 1 2 3
2
2 1
1
```

Output:

```
1
```

## Solution

Swap the stations so that `a < b`; going backwards never helps. Let
`cost[i]` be the cheapest way from `a` to station `i`, with `cost[a] = 0`;
the last ticket goes from some station `j` to `i` and costs the price of the
band of `x[i] - x[j]`.

**Quadratic DP.** Try every `j` with `x[i] - x[j] ≤ L3`. That is up to
`N^2 / 2 = 5·10^7` steps when one ticket reaches far — enough in C++, not in
Python.

**Three pointers.** `cost` never decreases along the line: a way to station
`i + 1` ends with a ticket from some `j`, and the ticket from `j` to `i` is
not longer, so not more expensive. Therefore, for a ticket of band `k`, the
best start is the **farthest** station `j` with `x[i] - x[j] ≤ Lk` — it has
the smallest `cost` among all starts that band reaches. As `i` grows, these
farthest starts only move forward, so keep one pointer per band and advance
it while the distance exceeds `Lk`. Each step tries three candidates:
`O(N)` in total.

Pitfalls:

- the stations may be given in decreasing order;
- a ticket of a cheaper band is used for any shorter ride, so a ride of
  length `X ≤ L1` costs `C1`, not `C3`;
- the answer fits in 32 bits, but use 64-bit integers for sums anyway.

## Language notes

- **C++**, **Go**, **Python**, **Java**, **Rust**: three pointers.
- **C++** also has the quadratic DP.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1031_dp.cpp](1031_dp.cpp) | G++ 13.2 x64 | dp | O(N^2) | AC | 0.078 s | 284 KB |
| [1031_dp_two_pointers.cpp](1031_dp_two_pointers.cpp) | G++ 13.2 x64 | dp, two_pointers | O(N) | AC | 0.015 s | 280 KB |
| [1031_dp_two_pointers.go](1031_dp_two_pointers.go) | Go 1.14 x64 | dp, two_pointers | O(N) | AC | 0.031 s | 1440 KB |
| [1031_dp_two_pointers.java](1031_dp_two_pointers.java) | Java 1.8 | dp, two_pointers | O(N) | AC | 0.093 s | 668 KB |
| [1031_dp_two_pointers.py](1031_dp_two_pointers.py) | Python 3.12 x64 | dp, two_pointers | O(N) | AC | 0.078 s | 1684 KB |
| [1031_dp_two_pointers.rs](1031_dp_two_pointers.rs) | Rust 1.75 x64 | dp, two_pointers | O(N) | AC | 0.031 s | 516 KB |
