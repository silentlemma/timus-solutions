# 1764. Transsib

[Timus 1764](https://acm.timus.ru/problem.aspx?space=1&num=1764) · difficulty 1782 · math

Original problem by Alexander Ipatov, from the Fourteenth Ural Championship in Sports Programming, April 10, 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Freight goes from one city to another along four routes, and six
bridges limit it. With the bridges numbered in the input order, route 1
crosses bridges 1, 2 and 6, route 2 crosses 4, 5 and 6, route 3 crosses
4, 2 and 3, and route 4 crosses 1, 5 and 3; each bridge carries at most
its capacity per day in total. Choose the loads of the routes, not
necessarily whole, so that the total is as large as possible.

## Input

The six capacities, whole numbers from 1 to 10⁹.

## Output

The four loads, with an error of at most 10⁻³. Any best plan is
accepted.

## Examples

### Example 1

Input:

```
70 30 60 100 20 50
```

Output:

```
20.000 10.000 10.000 10.000
```

## Solution

Every bridge lies on exactly two routes, and the six bridges give all
six pairs of the four routes. So the task is a linear program: maximise
x₁ + x₂ + x₃ + x₄ under xᵢ + xⱼ ≤ c for each bridge and xᵢ ≥ 0. The
feasible loads form a bounded polytope, and the best plan is at one of
its corners, where four of the ten constraints hold with equality.

All 210 choices of four constraints are tried. Each gives a 4 × 4
system with entries 0, 1 and −1, solved exactly by Cramer's rule: the
loads are whole numerators over one whole denominator, so checking the
other constraints and comparing totals needs no rounding at all. The
best feasible corner is printed. `O(1)`.

In the example the bridges at Kotelnich (30) and Vyatskiye Polyany (20)
together lie on every route once, so no plan carries more than 50. The
program prints 30, 20, 0 and 0, another plan with the same total as the
example's.

Pitfalls:

- the best loads may be halves, as when every capacity is 1 and each
  route carries 0.5;
- the plan is not unique, so the checker compares totals;
- with capacities up to 10⁹, a floating-point search for corners can
  wrongly accept or reject one at its edge.

The totals agree with a search over all half-whole loads on 120 random
cases with small capacities and with an independent accepted
implementation on 90 random cases, all checked against the capacities.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1764_math.cpp](1764_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 224 KB |
| [1764_math.go](1764_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.046 s | 2404 KB |
| [1764_math.java](1764_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 2712 KB |
| [1764_math.py](1764_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 824 KB |
| [1764_math.rs](1764_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 284 KB |
