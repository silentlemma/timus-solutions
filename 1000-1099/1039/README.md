# 1039. A guest list without direct bosses

[Timus 1039](https://acm.timus.ru/problem.aspx?space=1&num=1039) · difficulty 386 · dp, trees

Original problem by Marat Bakirov, from the Fifth Ural State University Team Programming Championship, October 2000.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`N` employees (`1 ≤ N ≤ 6000`) form a tree: everyone except the root has
one direct boss. Every employee has a rating from −128 to 127. Choose a set
of employees in which no one is invited together with their direct boss,
with the largest total rating. The set may be empty.

Time limit: 0.5 seconds. Memory limit: 8 MB.

## Input

`N`, then `N` lines with the ratings of employees `1..N`, then lines
`L K` meaning that `K` is the direct boss of `L`, ending with the line
`0 0`.

## Output

The largest total rating.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
7
1
1
1
1
1
1
1
1 3
2 3
6 4
7 4
4 5
3 5
0 0
```

Output:

```
5
```

### Example 2

Input:

```
4
3
-5
4
2
1 2
3 2
2 4
0 0
```

Output:

```
9
```

## Solution

The classic DP on a tree. For each employee `v` compute two values over
the subtree of `v`:

- `take[v]` — the best total when `v` is invited: `rating[v]` plus
  `skip[c]` for every subordinate `c`;
- `skip[v]` — the best total when `v` is not invited: the sum of
  `max(take[c], skip[c])` over the subordinates.

The answer is `max(take[root], skip[root])`. A negative rating is never
forced into the sum: `skip` always allows leaving the employee out, so
with all ratings negative the answer is `0`.

The tree can be a chain of 6000 levels, so the solutions do not recurse:
a breadth-first order from the root lists every boss before the
subordinates, and walking it backwards finishes every subtree before its
root, adding the two values into the boss. `O(N)`.

Pitfalls:

- the depth can reach 6000: a recursive DFS may overflow the stack;
- negative ratings: inviting nobody (total 0) is allowed;
- the root is not given explicitly: it is the employee without a boss.

## Language notes

- **C++**, **Go**, **Java**, **Rust**: the children are kept as linked
  lists in two arrays (`first`, `next`), which suits the 8 MB limit.
- **Python**: lists of children; the order list grows while it is being
  walked, which gives the breadth-first order.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1039_dp.cpp](1039_dp.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.015 s | 296 KB |
| [1039_dp.go](1039_dp.go) | Go 1.14 x64 | dp | O(N) | AC | 0.031 s | 1588 KB |
| [1039_dp.java](1039_dp.java) | Java 1.8 | dp | O(N) | AC | 0.093 s | 656 KB |
| [1039_dp.py](1039_dp.py) | Python 3.12 x64 | dp | O(N) | AC | 0.093 s | 3120 KB |
| [1039_dp.rs](1039_dp.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.015 s | 528 KB |
