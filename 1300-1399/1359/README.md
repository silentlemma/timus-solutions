# 1359. Construction

[Timus 1359](https://acm.timus.ru/problem.aspx?space=1&num=1359) · difficulty 1166 · dp

Original problem by Den Raskovalov (statement by Aleksandr Bikbaev), from the School Championship, March 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A barrel at rest has to get n metres to the left and m metres down,
1 ≤ n, m ≤ 50, rolling along a chain of boards. Every board has integer
ends, its lower end strictly below and not to the right of its upper
end. There is no friction, g = 10, and at each joint the barrel keeps
its speed and only turns. Print the least time of the descent with an
error of at most 10⁻³.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The numbers n and m.

## Output

The least time in seconds.

## Examples

### Example 1

Input:

```
2 2
```

Output:

```
0.8614
```

## Solution

Without friction, energy is conserved: at depth d the barrel moves at
v(d) = √(2·g·d), whatever path brought it there. Along one board the
acceleration is constant, so the barrel covers the length L at the
average of its end speeds, and the board takes 2L / (v₁ + v₂).

So only the lattice points matter. A board goes from (x, e) to
(y, d) with y ≥ x and d > e, measuring x to the left and depth down,
and best[d][y] = min(best[e][x] + 2L / (v(e) + v(d))). The answer is
best[m][n]. There are about n² · m² / 4 transitions, 1.6 million for
n = m = 50. `O(n² · m²)`.

Pitfalls:

- the first board starts at speed 0, which the formula 2L / (0 + v)
  handles;
- a board cannot go right or stay level, but it can be vertical;
- for a shallow slope the barrel is slow, and the answer can be large:
  22.3652 for n = 50, m = 1 (test 04).

For n = m = 1 the single board gives 2√2 / √20 = 0.6325 (test 02),
matching the formula worked out by hand.

## Language notes

- Python builds the times of all boards between two rows once and
  updates a whole row with `map(min, …)`, which keeps the largest case
  at about a quarter of a second.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1359_dp.cpp](1359_dp.cpp) | G++ 13.2 x64 | dp | O(n²·m²) | AC | 0.031 s | 248 KB |
| [1359_dp.go](1359_dp.go) | Go 1.14 x64 | dp | O(n²·m²) | AC | 0.046 s | 1128 KB |
| [1359_dp.java](1359_dp.java) | Java 1.8 | dp | O(n²·m²) | AC | 0.140 s | 1872 KB |
| [1359_dp.py](1359_dp.py) | Python 3.12 x64 | dp | O(n²·m²) | AC | 0.484 s | 776 KB |
| [1359_dp.rs](1359_dp.rs) | Rust 1.75 x64 | dp | O(n²·m²) | AC | 0.046 s | 280 KB |
