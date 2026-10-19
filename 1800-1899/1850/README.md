# 1850. Space Tourism

[Timus 1850](https://acm.timus.ru/problem.aspx?space=1&num=1850) · difficulty 2662 · fenwick

Original problem by Dmitry Ivankov, from the Ural SU Contest at the Petrozavodsk summer session, August 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n planets lie on one ray from a star, each at its own distance and each
home to some race. A tourist's ship flies at most d without refuelling,
can refuel on any planet, and works only at distances from the star
within the tourist's range [low, high]; the tourist is brought to any
planet in that range. For every tourist find the largest number of
different races the tourist can meet.

## Input

n, s and d (1 ≤ n, s, d ≤ 10⁵), then the n planets as distance (distinct,
at most 10⁶) and race (1 to s); then m (1 ≤ m ≤ 10⁵) and the tourists'
ranges, with bounds up to 10⁶.

## Output

The answer for each tourist, one per line.

## Examples

### Example 1

Input:

```
5 5 11
10 1
50 2
30 1
20 1
60 3
2
5 65
15 45
```

Output:

```
2
1
```

## Solution

Sort the planets by distance. Inside a range, the tourist can go from a
planet to the next one exactly when they are at most d apart, so the
planets in the range fall into runs, and the answer is the largest
number of races in one run. The runs are the global pieces of planets
split at gaps over d, cut by the range: a range covering pieces P₁ … Pₖ
consists of a tail of P₁, the whole pieces P₂ … Pₖ₋₁ and a head of Pₖ.

So precompute, inside every piece, the number of races from its start
to each planet (head) and from each planet to its end (tail), and the
number of races of every whole piece, with a sparse table for the
largest one over a range of pieces. A range that spans several pieces
is answered by two lookups and one table query.

A range inside a single piece needs the number of different races among
consecutive planets. Answer these queries offline, sorted by their right
end: walking right, keep a Fenwick tree in which every race is counted
only at its latest planet so far; the races in [l, r] are then the
counts at positions l … r. `O((n + m) log n)`.

In the example the planets 10, 20 and 30 form one piece of race 1 and
the planets 50 and 60 another, of races 2 and 3, because 50 − 30 > 11.
The first tourist sees both pieces and meets two races at best; the
second sees only 20 and 30.

Pitfalls:

- the ship cannot leave the range even to reach another planet in it;
- a range may hold no planet at all;
- the same race may appear on several planets of one piece.

The answers agree with a direct count on three hundred small cases and
with an independent accepted implementation on the large tests. The
Python solution runs on PyPy.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1850_fenwick.cpp](1850_fenwick.cpp) | G++ 13.2 x64 | fenwick | O((n + m) log n) | AC | 0.328 s | 9700 KB |
| [1850_fenwick.go](1850_fenwick.go) | Go 1.14 x64 | fenwick | O((n + m) log n) | AC | 0.171 s | 21420 KB |
| [1850_fenwick.java](1850_fenwick.java) | Java 1.8 | fenwick | O((n + m) log n) | AC | 0.171 s | 12204 KB |
| [1850_fenwick.py](1850_fenwick.py) | PyPy 3.10 x64 | fenwick | O((n + m) log n) | AC | 0.953 s | 54928 KB |
| [1850_fenwick.rs](1850_fenwick.rs) | Rust 1.75 x64 | fenwick | O((n + m) log n) | AC | 0.078 s | 27020 KB |
