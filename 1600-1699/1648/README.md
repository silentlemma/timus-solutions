# 1648. Yachts

[Timus 1648](https://acm.timus.ru/problem.aspx?space=1&num=1648) · difficulty 387 · greedy

Original problem by Alexey Samsonov, from the USU Junior Contest, October 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A shipyard builds at most d yachts a month. In month i, aᵢ new
billionaires come at the end of the month, each wanting a yacht at once;
anyone who finds none leaves for good. Yachts can be built in advance,
but keeping one for a month costs one gold bar. Find the largest number
of yachts that can be sold in n months, and the least storage cost for
selling that many.

## Input

n and d (1 ≤ n ≤ 20000, 1 ≤ d ≤ 100000), then a₁ … aₙ
(0 ≤ aᵢ ≤ 100000).

## Output

The most yachts sold and the least gold spent on storage.

## Examples

### Example 1

Input:

```
3 5
6 1 7
```

Output:

```
13 2
```

## Solution

Selling: by the end of month i the yard has built at most i · d yachts,
and buyers of month i only buy then. Serving every buyer that stock
allows is optimal, so the running total of sales is
Sᵢ = min(Sᵢ₋₁ + aᵢ, i · d), and Sₙ is the answer. Selling as early as
possible also leaves the least stock behind each month.

Storage: with the sales of each month fixed, build every yacht as late
as possible. Going from the last month backwards, a month builds what it
sells plus what later months could not build themselves, up to d; the
rest moves one month earlier and costs one bar for every month boundary
it waits across. The total of those carried amounts is the least
storage cost. `O(n)`.

Sales are at most 20000 · 100000 = 2,000,000,000 and fit signed 32-bit
integers. Storage needs 64 bits: it can reach about n² · d / 2.

Pitfalls:

- buyers of a month cannot be served later, so the sales of a month are
  capped by its buyers and by what exists by then (test 03);
- buyers bunched at the end force long storage (tests 04, 05), past
  32-bit integers (gen3).

The answers match an independent accepted implementation on 120 random
tests and an exhaustive search on small ones.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1648_greedy.cpp](1648_greedy.cpp) | G++ 13.2 x64 | greedy | O(n) | AC | 0.031 s | 360 KB |
| [1648_greedy.go](1648_greedy.go) | Go 1.14 x64 | greedy | O(n) | AC | 0.062 s | 1584 KB |
| [1648_greedy.java](1648_greedy.java) | Java 1.8 | greedy | O(n) | AC | 0.109 s | 688 KB |
| [1648_greedy.py](1648_greedy.py) | Python 3.12 x64 | greedy | O(n) | AC | 0.109 s | 3136 KB |
| [1648_greedy.rs](1648_greedy.rs) | Rust 1.75 x64 | greedy | O(n) | AC | 0.015 s | 844 KB |
