# 2177. Longest row of distinct numbers whose neighbours sum to X or V

[Timus 2177](https://acm.timus.ru/problem.aspx?space=1&num=2177) · difficulty 1242 · math

Original problem by Vadim Barinov, from the Ural School Programming Contest 2023.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Find the longest row of distinct positive integers in which every two
neighbours add up to X or to V. The limits are 1 second and 256 MB.

## Input

X and V, 3 ≤ X, V ≤ 10⁹.

## Output

The largest length.

## Examples

### Example 1

Input:

```
10
5
```

Output:

```
4
```

## Solution

Only numbers in [1, max(X, V) − 1] can occur in a row of length at least
two. Join distinct a and b in this range when a + b is X or V. Every
number has at most two partners, X − a and V − a, so the numbers form
disjoint paths and cycles, and the longest row is the largest of these
components.

Let X ≤ V and d = V − X. If d = 0, components are pairs or isolated
vertices; a pair always exists, so the answer is 2. Otherwise, taking
the two kinds of partners in turn moves a number by d:
a, X − a, a + d, X − a − d, … So a component lives
in at most two residue classes modulo d, r and X − r, inside [1, V − 1].
A path ends when the next partner is nonpositive or would repeat the
current number (at X / 2 or V / 2 when integral).

- d = 1: one class, the whole range, V − 1 numbers.
- d = 2: if V is odd, the two classes are the two parities and the
  answer is again V − 1; if V is even, both partners keep the parity and
  the best class has V / 2 numbers.
- d ≥ 3: the best component takes two different classes with
  ⌊(V − 3) / d⌋ + 1 numbers each, so the answer is
  2 (⌊(V − 3) / d⌋ + 1).

These closed forms agree with a direct count of the components for all
X, V below 60. The work is O(1).

In the example d = 5, and the row 8, 2, 3, 7 uses the classes of 2 and
3 modulo 5: 2 (⌊7 / 5⌋ + 1) = 4.

Pitfall (tests 03 and 21): a missing partner need not be a self-partner.
In test 03, X = 3, V = 4, the longest row 2, 1, 3 ends at 3 because its
other partner is zero. Equal even sums, as in test 21, also leave the
midpoint isolated; they do not make every component a pair.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2177_math.cpp](2177_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.031 s | 400 KB |
| [2177_math.go](2177_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1120 KB |
| [2177_math.java](2177_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 448 KB |
| [2177_math.py](2177_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 456 KB |
| [2177_math.rs](2177_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 232 KB |
