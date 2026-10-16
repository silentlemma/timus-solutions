# 1765. Error 404

[Timus 1765](https://acm.timus.ru/problem.aspx?space=1&num=1765) · difficulty 4244 · number_theory

Original problem by Igor Chevdar (idea by Dmitry Poletayev), from the Fourteenth Ural Championship in Sports Programming, April 10, 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A turbine had n blades whose tips formed a regular n-gon; k of them
broke off. Remove as few of the remaining blades as possible so that
the centre of mass of the blades left is on the axis, keeping at least
one blade. n has at most two distinct prime factors.

## Input

n and k (3 ≤ n ≤ 20000, 1 ≤ k ≤ n − 1), then the numbers of the broken
blades in increasing order; blades are numbered 1 to n around the
circle.

## Output

The number of blades to remove and their numbers in any order, or −1
if no balanced set of blades can be left. Any best answer is accepted.

## Examples

### Example 1

Input:

```
12 3
3 4 12
```

Output:

```
2
8 9
```

### Example 2

Input:

```
3 1
1
```

Output:

```
-1
```

## Solution

The tips are the n-th roots of unity, and the blades left balance when
their tips sum to zero. For n with at most two prime factors p and q, a
theorem of de Bruijn on vanishing sums of roots of unity says that such
a set of tips is a union of disjoint regular p-gons and q-gons. So the
task is to keep as many whole blades as possible in such polygons.

Every polygon stays among the blades with the same remainder modulo
n/(pq). Those pq blades form a p by q grid, with blade t of the group
at row t mod p and column t mod q: a q-gon is a row and a p-gon a
column. A row and a column always cross, so the blades kept in a group
are either all rows without a broken blade or all such columns,
whichever holds more; every other whole blade of the group is removed.
With one prime factor only the p-gons exist, so a group is kept exactly
when none of its blades is broken. If nothing is kept, the answer is
−1. `O(n + √n)`.

In the first example p = 2 and q = 3. Among the odd-numbered blades the
broken 3 spoils one triangle and one diameter; keeping the two whole
diameters (1, 7 and 5, 11) beats keeping one triangle, so 9 goes. Among
the even-numbered blades, 4 and 12 spoil one triangle and two
diameters; the other triangle, 2, 6 and 10, stays, so 8 goes.

Pitfalls:

- with one prime factor, single blades are not balanced sets;
- a row and a column cannot both be kept, since they share a blade;
- if no polygon is whole, all blades would have to go, which is not
  allowed: the answer is −1.

The answers agree with a search over every subset of the whole blades,
summing the tips, on 250 random cases with up to 16 blades, and give
the same number of blades as an independent accepted implementation on
100 random cases up to 20000 blades.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1765_number_theory.cpp](1765_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(n + sqrt(n)) | AC | 0.031 s | 288 KB |
| [1765_number_theory.go](1765_number_theory.go) | Go 1.14 x64 | number_theory | O(n + sqrt(n)) | AC | 0.031 s | 2020 KB |
| [1765_number_theory.java](1765_number_theory.java) | Java 1.8 | number_theory | O(n + sqrt(n)) | AC | 0.140 s | 3204 KB |
| [1765_number_theory.py](1765_number_theory.py) | Python 3.12 x64 | number_theory | O(n + sqrt(n)) | AC | 0.093 s | 3452 KB |
| [1765_number_theory.rs](1765_number_theory.rs) | Rust 1.75 x64 | number_theory | O(n + sqrt(n)) | AC | 0.031 s | 1160 KB |
