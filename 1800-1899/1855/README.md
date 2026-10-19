# 1855. Trade Guilds of Erathia

[Timus 1855](https://acm.timus.ru/problem.aspx?space=1&num=1855) · difficulty 1263 · fenwick

Original problem by Alexander Fetisov (prepared by Denis Dublennykh), from the Ural SU Team.GOV Contest at the Petrozavodsk summer session, August 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n cities lie along a trade road, and every stretch between neighbouring
cities has a toll, at first 0. Events come in order: a change adds d to
the toll of every stretch between cities a and b, and a new guild works
in the cities a … b, its caravans running equally often between every
pair of those cities. For every new guild print the average toll one of
its caravans pays at that moment.

## Input

n and m (2 ≤ n ≤ 10⁵, 1 ≤ m ≤ 10⁵), then m events "change a b d" or
"establish a b" with 1 ≤ a < b ≤ n and |d| ≤ 10 000. Every toll stays
between 0 and 10 000.

## Output

The average for every new guild, with absolute or relative error at
most 10⁻⁶.

## Examples

### Example 1

Input:

```
4 5
change 1 4 2
change 1 2 -1
establish 1 2
establish 2 4
establish 1 4
```

Output:

```
1.00000000
2.66666667
2.83333333
```

## Solution

Let tᵢ be the toll of the stretch from city i to city i + 1. A guild on
cities a … b has (b − a + 1)(b − a)/2 routes, and stretch i lies on the
(i − a + 1)(b − i) of them that start at or before i and end after it.
Expanding the product, the total toll is
−S₂ + (a + b − 1)·S₁ + b(1 − a)·S₀ with S_k = Σ iᵏ·tᵢ over
i = a … b − 1, so range sums of tᵢ, i·tᵢ and i²·tᵢ under range additions
are enough.

Keep the tolls as prefix sums of differences dif_j: a change adds d at a
and −d at b. Then Σ over i ≤ x of iᵏ·tᵢ equals
P_k(x)·Σ dif_j − Σ dif_j·P_k(j − 1) over j ≤ x, where P_k(x) is the sum
of iᵏ for i = 1 … x, precomputed. Four Fenwick trees over the
differences, plain and weighted by P₀, P₁ and P₂, answer every event in
`O(log n)`.

In the example the tolls end up 1, 2 and 2. The guild on cities 1 … 4
has six routes paying 1, 3, 5, 2, 4 and 2, which is 17/6 ≈ 2.8333.

Pitfalls:

- Python's integers are exact, and the other solutions compute modulo
  2⁶⁴, which is exact for the final total since it is below 2.5·10¹⁸;
- the total of a guild needs no division until the very end;
- the Python solution runs on PyPy.

The averages agree with a direct computation on two hundred small cases
and with an independent accepted implementation on the large tests.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1855_fenwick.cpp](1855_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(n + m log n) | AC | 0.375 s | 4484 KB |
| [1855_fenwick.go](1855_fenwick.go) | Go 1.14 x64 | fenwick | O(n + m log n) | AC | 0.109 s | 8196 KB |
| [1855_fenwick.java](1855_fenwick.java) | Java 1.8 | fenwick | O(n + m log n) | AC | 0.421 s | 15736 KB |
| [1855_fenwick.py](1855_fenwick.py) | PyPy 3.10 x64 | fenwick | O(n + m log n) | AC | 0.406 s | 37656 KB |
| [1855_fenwick.rs](1855_fenwick.rs) | Rust 1.75 x64 | fenwick | O(n + m log n) | AC | 0.046 s | 11256 KB |
