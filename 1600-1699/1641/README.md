# 1641. Duties

[Timus 1641](https://acm.timus.ru/problem.aspx?space=1&num=1641) · difficulty 511 · constructive

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
`O(n² log n)` in C++; `O(n²)` otherwise.

Pitfalls:

- covering everyone first matters: filling the days in plain order
  could spend them all on the first students (test 07);
- with k = n every room has one student and every pair is allowed
  (test 06).

A checker accepts any valid plan; the program's plans pass it for all
1866 feasible inputs with n ≤ 12.

## Optimized solutions

C++ and Java keep the same balanced room assignment i mod k. With room sizes sᵢ, the number of cross-room pairs is (n²−Σsᵢ²)/2. When two rooms differ by at least two pupils, moving one from the larger room to the smaller reduces Σsᵢ². The balanced assignment therefore allows every feasible m. Emit disjoint neighbouring pupil pairs first. For odd n, pair the last pupil with pupil zero or one in a different room. These ceil(n/2) seeds cover everyone, and any feasible plan needs at least that many days. Then scan unordered cross-room pairs, skipping seeds by their index predicates, until m days are emitted. No used set/matrix, room array or complete day list is needed. Fixed 8192-byte output replaces the growing Java builder; Java also avoids Scanner. Worst time O(n²), extra storage O(1). All simple sources remain; Go, Python and Rust reuse admitted bases.

The accepted base implementations [1641_constructive.go](1641_constructive.go), [1641_constructive.py](1641_constructive.py), [1641_constructive.rs](1641_constructive.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1641_constructive.cpp](1641_constructive.cpp) | G++ 13.2 x64 | constructive | O(n² log n) | AC | 0.031 s | 300 KB | 11288471 |
| [1641_constructive.go](1641_constructive.go) \* | Go 1.14 x64 | constructive | O(n²) | AC | 0.031 s | 1576 KB | 11288472 |
| [1641_constructive.java](1641_constructive.java) | Java 1.8 | constructive | O(n²) | AC | 0.125 s | 2048 KB | 11288474 |
| [1641_constructive.py](1641_constructive.py) \* | Python 3.12 x64 | constructive | O(n²) | AC | 0.078 s | 1312 KB | 11288473 |
| [1641_constructive.rs](1641_constructive.rs) \* | Rust 1.75 x64 | constructive | O(n²) | AC | 0.031 s | 660 KB | 11328280 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1641_constructive_optimized.cpp](1641_constructive_optimized.cpp) | G++ 13.2 x64 | constructive | O(n²) | AC | 0.015 s | 104 KB | 11315496 |
| [1641_constructive_optimized.java](1641_constructive_optimized.java) \* | Java 1.8 | constructive | O(n²) | AC | 0.109 s | 388 KB | 11315497 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
