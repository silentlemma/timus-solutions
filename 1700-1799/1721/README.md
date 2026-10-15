# 1721. Two Sides of the Same Coin

[Timus 1721](https://acm.timus.ru/problem.aspx?space=1&num=1721) · difficulty 581 · matching

Original problem by Pavel Atnashev, from the NEERC 2009 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Every problem is prepared by two people: one writes the statement, the
other prepares the tests, and their ranks differ by exactly 2. Each
person writes statements, prepares tests or can do both, and takes part
in at most one problem. Find the largest number of problems and who
prepares each.

## Input

n (2 ≤ n ≤ 1000), then n lines: a name of up to 20 Latin letters, the
specialization `statements`, `testdata` or `anything`, and the rank, an
integer from 3 to 1000. All names differ.

## Output

The largest number of problems, then for each problem the name of the
statement writer and the name of the test preparer. Any best plan is
accepted.

## Examples

### Example 1

Input:

```
7
Poll anything 8
Tejat statements 6
Mebsuta testdata 6
Propus testdata 4
Alzir anything 7
Mekbuda anything 3
Dirah testdata 9
```

Output:

```
3
Poll Mebsuta
Tejat Propus
Alzir Dirah
```

## Solution

Join two people by an edge when their ranks differ by exactly 2 and one
of them can write the statement while the other prepares the tests. A
plan is a set of edges with no common person, so the task is a maximum
matching.

The graph is bipartite. Along an edge ⌊rank/2⌋ changes by exactly 1, so
its parity flips: the people with ⌊rank/2⌋ even form one side, those
with it odd the other. Graph construction and Hopcroft–Karp take
`O(n² + E √n)`, where E reaches 250 000 when 500 people have rank 3 and 500
rank 5. For each matched pair choose a valid assignment of roles;
when both can do both, either way works.

In the example Poll (8) and Mebsuta (6), Tejat (6) and Propus (4), and
Alzir (7) and Dirah (9) make three problems. Mekbuda (3) has nobody of
rank 1 or 5 and stays out.

Pitfalls:

- the ranks must differ by exactly 2, not by at most 2;
- two `statements` specialists, or two `testdata` specialists, never
  make a problem, even with ranks 2 apart;
- the bipartite split lets Hopcroft–Karp find augmenting paths
  without handling odd cycles;
- the Python solution walks the augmenting paths with an explicit
  stack, since a path can pass through hundreds of people.

The checker verifies the count against the best one, that every pair
can prepare a problem and that nobody takes part twice. The counts
match an exhaustive search over all plans for 300 random sets of up to
8 people, and an independent accepted implementation on 60 random sets
of 1000.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1721_matching.cpp](1721_matching.cpp) | G++ 13.2 x64 | matching | O(n² + E √n) | AC | 0.015 s | 924 KB |
| [1721_matching.go](1721_matching.go) | Go 1.14 x64 | matching | O(n² + E √n) | AC | 0.031 s | 4476 KB |
| [1721_matching.java](1721_matching.java) | Java 1.8 | matching | O(n² + E √n) | AC | 0.156 s | 6132 KB |
| [1721_matching.py](1721_matching.py) | Python 3.12 x64 | matching | O(n² + E √n) | AC | 0.171 s | 2840 KB |
| [1721_matching.rs](1721_matching.rs) | Rust 1.75 x64 | matching | O(n² + E √n) | AC | 0.031 s | 1800 KB |
