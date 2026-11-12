# 1783. Nuclear Arms Race

[Timus 1783](https://acm.timus.ru/problem.aspx?space=1&num=1783) · difficulty 473 · simulation

Original problem by Pavel Atnashev, from the XV Open USU Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

One country plans to hold exactly aᵢ warheads at the end of month i.
Its rival starts with none, and at the start of month i, knowing the
plans aᵢ, …, aᵢ₊ₘ₋₁, picks the smallest whole change xᵢ such that
changing its stock by xᵢ in each of the next m months would keep it at
or above the plan at the end of each of them. Only that month's change
is made; the next month the choice is made again. Print x₁, …, xₙ.

## Input

n and m (1 ≤ n ≤ 10000, 1 ≤ m ≤ 50), then a₁, …, aₙ₊ₘ₋₁
(0 ≤ aᵢ ≤ 10⁵).

## Output

x₁, …, xₙ.

## Examples

### Example 1

Input:

```
4 3
0 0 4 2 1 0
```

Output:

```
2 1 1 -1
```

## Solution

With stock s at the start of month i, after t months of the same change
x the stock is s + t·x, which must be at least aᵢ₊ₜ₋₁. So x is the
largest of ⌈(aᵢ₊ₜ₋₁ − s)/t⌉ over t = 1…m. The stock then grows by x and
the next month repeats. The rounding must be up also for negative
numbers, where plain integer division in many languages rounds towards
zero. `O(n·m)`.

In the example the first order must reach 4 within three months: 2.
With 2 in stock, the next plans 0, 4, 2 need ⌈2/2⌉ = 1; then with 3 the
plans 4, 2, 1 need 1; then with 4 the plans 2, 1, 0 allow −1.

Pitfalls:

- orders may be negative when the plans fall;
- ⌈−3/2⌉ is −1, not −2 and not 0, so the division must round up
  explicitly;
- only the first of the planned months is carried out each time.

The answers agree with an independent accepted implementation on 60
random cases, from a few months to 10000 months of random, wavy and
spiky plans.

## Optimized solutions

C++/Go keep exactly the original maximum of m signed ceilings, but stream future plans through a ring of at most50 integers. Initially read m plans; after each actual order replace the expired slot with the next plan and advance the head. The ring therefore contains precisely the current lookahead window. Walk it with a wrapped index rather than a remainder per item. Nonnegative deltas use (delta+t−1)/t; negative deltas use truncation toward zero, which is their ceiling. Plans and resulting stock stay between0 and100000, so signed32-bit arithmetic suffices. Time remains O(nm); plan storage drops from O(n+m) to O(m), with bounded I/O. All ordinary files remain; Java, Python and Rust reuse their admitted bases.

The accepted base implementations [1783_simulation.java](1783_simulation.java), [1783_simulation.py](1783_simulation.py), [1783_simulation.rs](1783_simulation.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1783_simulation.cpp](1783_simulation.cpp) | G++ 13.2 x64 | simulation | O(n m) | AC | 0.031 s | 280 KB | 11289782 |
| [1783_simulation.go](1783_simulation.go) | Go 1.14 x64 | simulation | O(n m) | AC | 0.031 s | 1384 KB | 11289783 |
| [1783_simulation.java](1783_simulation.java) \* | Java 1.8 | simulation | O(n m) | AC | 0.156 s | 2388 KB | 11289785 |
| [1783_simulation.py](1783_simulation.py) \* | Python 3.12 x64 | simulation | O(n m) | AC | 0.187 s | 2472 KB | 11289784 |
| [1783_simulation.rs](1783_simulation.rs) \* | Rust 1.75 x64 | simulation | O(n m) | AC | 0.046 s | 840 KB | 11289786 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1783_simulation_optimized.cpp](1783_simulation_optimized.cpp) \* | G++ 13.2 x64 | simulation | O(n·m) | AC | 0.031 s | 88 KB | 11315303 |
| [1783_simulation_optimized.go](1783_simulation_optimized.go) \* | Go 1.14 x64 | simulation | O(n·m) | AC | 0.031 s | 300 KB | 11315305 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
