# 1777. Anindilyakwa

[Timus 1777](https://acm.timus.ru/problem.aspx?space=1&num=1777) · difficulty 128 · simulation

Original problem by Ivan Burmistrov, from the XV Open USU Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Three piles of stones of different sizes lie in a field. Each person in
turn finds two piles whose sizes differ least and brings a new pile of
exactly that difference; all piles stay. The questions stop with the
person who finds two piles of equal size. How many people are asked?

## Input

The three different sizes x₁, x₂, x₃ (1 ≤ xᵢ ≤ 10¹⁸).

## Output

The number of people asked.

## Examples

### Example 1

Input:

```
11 5 9
```

Output:

```
3
```

## Solution

The process is simulated as it is: sort the piles, take the smallest
difference between neighbours, stop if it is 0, otherwise add a pile of
that size. The smallest difference keeps shrinking much as the numbers
do in Euclid's algorithm, so the run is short: the longest found, from
three consecutive Fibonacci numbers near 10¹⁸, asks 85 people, and
a sample of 10,000 uniformly random valid triples averaged 3.7 people
(median 3). `O(s² log s)` for s steps.

In the example the differences are 2, 4 and 6: the first person brings
a pile of 2, the second sees 9 and 11 again and brings another 2, and
the third points at the two piles of 2.

Pitfalls:

- the person who finds equal piles is counted too;
- the new pile can repeat an old size, which ends the run one person
  later;
- sizes up to 10¹⁸ need 64-bit numbers;
- short random runs do not establish the worst case: test 08 asks
  85 people.

The answers agree with an independent accepted implementation on
90 random triples, including triples of Fibonacci numbers.

## Optimized solutions

The optimized C++ solution keeps no list of piles: only the two smallest
piles a < b and the current smallest difference g. The new pile g is at
most b − a, so it is smaller than b, and in sorted order its only
possible neighbours are a and b. All old differences stay, so the next
smallest difference is the least of g, |g − a| and b − g, and the two
smallest piles become g and a, or a and g. Every step takes `O(1)` time
and the whole run `O(1)` memory instead of sorting a growing vector; all
values fit in `long long`, since they are at most 10¹⁸:
{1777_simulation_optimized.cpp}.

The optimized Java solution reads the three sizes byte by byte from
`System.in` instead of creating a `Scanner`, whose regular expressions
and locale data cost more than the short simulation, which stays the
same: {1777_simulation_optimized.java}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1777_simulation_optimized.cpp`: time reduction +0.00%; memory
  reduction +47.92%; base: `1777_simulation.cpp`.

- `1777_simulation_optimized.java`: time reduction +0.00%; memory
  reduction +74.18%; base: `1777_simulation.java`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1777_simulation.go](1777_simulation.go).
- [1777_simulation.rs](1777_simulation.rs).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1777_simulation.cpp](1777_simulation.cpp) | G++ 13.2 x64 | simulation | O(s^2 log s) for s steps | AC | 0.015 s | 192 KB | 11304057 |
| [1777_simulation.go](1777_simulation.go) | Go 1.14 x64 | simulation | O(s^2 log s) for s steps | AC | 0.031 s | 1124 KB | 11289732 |
| [1777_simulation.java](1777_simulation.java) | Java 1.8 | simulation | O(s^2 log s) for s steps | AC | 0.140 s | 1704 KB | 11304058 |
| [1777_simulation.py](1777_simulation.py) | Python 3.12 x64 | simulation | O(s^2 log s) for s steps | AC | 0.093 s | 436 KB | 11289733 |
| [1777_simulation.rs](1777_simulation.rs) | Rust 1.75 x64 | simulation | O(s^2 log s) for s steps | AC | 0.046 s | 252 KB | 11304059 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1777_simulation_optimized.cpp](1777_simulation_optimized.cpp) | G++ 13.2 x64 | simulation | O(s) for s steps | AC | 0.015 s | 100 KB | 11304425 |
| [1777_simulation_optimized.java](1777_simulation_optimized.java) | Java 1.8 | simulation | O(s^2 log s) for s steps | AC | 0.140 s | 440 KB | 11304426 |
