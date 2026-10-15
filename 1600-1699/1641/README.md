# 1641. Duties

[Timus 1641](https://acm.timus.ru/problem.aspx?space=1&num=1641) · difficulty 508 · constructive

Original problem by Pavel Atnashev, from the USU Junior Contest, October 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Each of n students is put in charge of one of k rooms, and every room
needs someone. On each of m days two students in charge of different
rooms are on duty. No pair may be on duty twice, and every student must
be on duty at least once. Output such a plan; one is known to exist.

## Input

n, k and m (2 ≤ k ≤ n ≤ 100).

## Output

n lines with each student's room, then m lines with the pair on duty
each day. Any valid plan is accepted.

## Examples

### Example 1

Input:

```
5 3 4
```

Output:

```
1
2
1
2
3
1 2
3 4
3 5
4 5
```

### Example 2

Input:

```
4 2 4
```

Output:

```
1
2
1
2
1 2
3 4
1 4
2 3
```

## Solution

In graph terms: split the students into k non-empty groups and pick m
distinct edges between different groups that cover every student. At
least ⌈n/2⌉ edges are needed to cover n students, and at most as many
edges as the complete k-partite graph has. That count is largest when
the groups are as even as possible, so giving rooms in turn,
student i to room i mod k, is never worse than any other split; since a
plan exists, m fits.

With rooms in turn, students i and i + 1 always have different rooms,
so the pairs (0, 1), (2, 3), … cover everyone in ⌈n/2⌉ days; an odd
last student joins student 0, or student 1 if 0 shares its room. The
remaining days take any unused pairs from different rooms in order.
`O(n²)`.

Pitfalls:

- covering everyone first matters: filling the days in plain order
  could spend them all on the first students (test 07);
- with k = n every room has one student and every pair is allowed
  (test 06).

A checker accepts any valid plan; the program's plans pass it for all
1866 feasible inputs with n ≤ 12.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1641_constructive.cpp](1641_constructive.cpp) | G++ 13.2 x64 | constructive | O(n²) | AC | 0.031 s | 300 KB |
| [1641_constructive.go](1641_constructive.go) | Go 1.14 x64 | constructive | O(n²) | AC | 0.031 s | 1576 KB |
| [1641_constructive.java](1641_constructive.java) | Java 1.8 | constructive | O(n²) | AC | 0.125 s | 2048 KB |
| [1641_constructive.py](1641_constructive.py) | Python 3.12 x64 | constructive | O(n²) | AC | 0.078 s | 1312 KB |
| [1641_constructive.rs](1641_constructive.rs) | Rust 1.75 x64 | constructive | O(n²) | AC | 0.031 s | 644 KB |
