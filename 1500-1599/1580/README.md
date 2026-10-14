# 1580. Dean's Debts

[Timus 1580](https://acm.timus.ru/problem.aspx?space=1&num=1580) · difficulty 880 · graphs

Original problem by Alexey Efremov, from the USU Junior Contest (the Fourteenth Open Team Programming Contest for Schoolchildren of the Sverdlovsk Region), October 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The dean owes each of N ≤ 1000 students an unknown sum. On each of
M ≤ 10⁵ days a different pair of students tells the dean how much the
two of them are owed together. Print what each student is owed, with two
digits after the point, if the claims determine it uniquely, and
`IMPOSSIBLE` otherwise.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

N and M, then each claim as two students and their total A
(−10000 ≤ A ≤ 10000).

## Output

N sums, one per line, or `IMPOSSIBLE`.

## Examples

### Example 1

Input:

```
3 3
1 2 2
2 3 4
3 1 6
```

Output:

```
2.00
0.00
4.00
```

### Example 2

Input:

```
4 3
1 2 2
1 3 4
1 4 6
```

Output:

```
IMPOSSIBLE
```

## Solution

Each claim is an equation x_u + x_v = A, an edge of a graph on the
students. Inside a connected component, choose the debt t of one
student; walking the edges by breadth-first search, every other debt is
then ±t plus a constant, with the sign changing at every step. If the
component has no odd cycle, all its debts can shift by +d and −d along
the two sides and every claim still holds, so the answer is not unique.
An edge that closes an odd cycle joins two students with the same sign
and gives 2t = A − constants, which fixes t.

The debts are worked in halves of a rouble, where everything is an
integer, and printed as `.00` or `.50`. Finally every claim is checked
again: claims that contradict each other also leave no answer.
`O(N + M)`. The results were checked against exact Gaussian elimination
over the rationals on 500 random small systems.

Pitfalls:

- a sum may be half a rouble, also a negative one: −0.50 must keep its
  minus sign (tests 03, 04);
- every component must have an odd cycle, not just one of them
  (test 05);
- claims along two odd cycles may contradict each other (tests 06, gen2).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1580_graphs.cpp](1580_graphs.cpp) | G++ 13.2 x64 | graphs | O(N + M) | AC | 0.203 s | 7628 KB |
| [1580_graphs.go](1580_graphs.go) | Go 1.14 x64 | graphs | O(N + M) | AC | 0.156 s | 11500 KB |
| [1580_graphs.java](1580_graphs.java) | Java 1.8 | graphs | O(N + M) | AC | 0.109 s | 11772 KB |
| [1580_graphs.py](1580_graphs.py) | Python 3.12 x64 | graphs | O(N + M) | AC | 0.359 s | 47816 KB |
| [1580_graphs.rs](1580_graphs.rs) | Rust 1.75 x64 | graphs | O(N + M) | AC | 0.046 s | 10468 KB |
