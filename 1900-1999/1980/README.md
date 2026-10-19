# 1980. Minimum speed allowance with a route

[Timus 1980](https://acm.timus.ru/problem.aspx?space=1&num=1980) · difficulty 638 · binary_search, dijkstra

Original problem by Denis Dublennykh, from the Ural Sport Programming Championship 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An undirected road has length `l` kilometres and speed limit `s`
kilometres per hour. A nonnegative common allowance `S` permits speed up
to `s+S` on every road. Find the smallest allowance that lets a route
from vertex 1 to vertex `n` take at most `T` hours, and output a
corresponding sequence of original road indices.

The limits are `2≤n≤10000`, `1≤m≤10000`, `1≤s≤300`, `1≤l≤1000`, and
integer `1≤T≤10⁶`. Road endpoints satisfy `1≤a<b≤n`. The destination is
reachable; parallel roads and irrelevant components are handled. Time
limit: 1 second; memory limit: 64 MB.

## Input

All input values are integers. Read `n m`, then `m` lines `a b s l`,
followed by `T`. Road indices are 1 through `m` in input order.

## Output

Print `S k` on the first line and the `k` road indices in traversal
order on the second. Any valid optimal route is allowed.

## Checking

A checker verifies that the printed roads form a walk from 1 to n and
checks optimality with absolute or relative error 10⁻⁶. Route feasibility
is tested at the printed allowance increased by the allowed numerical
tolerance; any such route is accepted.

## Examples

Input:

```
3 3
1 3 50 150
1 2 80 100
2 3 80 100
2
```

Output:

```
20.000000 2
2 3
```

Input:

```
2 1
1 2 60 60
1
```

Output:

```
0.000000 1
1
```

## Solution

For a fixed `S`, the fastest traversal time of a road is `l/(s+S)`.
These weights are positive, so Dijkstra's algorithm decides whether the
destination can be reached within `T`. Ignore heap entries whose stored
time is stale, and stop when the destination is removed with its current
best time. A candidate time greater than `T` can be discarded because
later roads only add time.

Increasing `S` decreases every road time, hence feasibility is monotone.
First check `S=0`. If it is feasible, zero is the optimum. Otherwise
binary-search an infeasible lower bound zero and a feasible upper bound
`U=Σl/T`. This upper bound works because a simple route uses total
length at most `Σl`, and at allowance `U` its time is strictly below
`Σl/U=T`.

Keep the upper bound feasible. Run at most 60 bisections; Python also
stops once the bracket width is at most `10⁻⁹ max(1,upper)`. Finally
rerun Dijkstra at the feasible upper bound. Each predecessor stores the
original road index, so parallel roads remain distinguishable. Starting
from `n`, follow those roads to the preceding endpoint and reverse the
collected list.

Every fixed-allowance test is correct by Dijkstra's invariant for
positive weights. Monotonicity preserves the search bracket containing
the optimum. The final predecessor chain witnesses feasibility at its
upper endpoint, proving both the numerical answer and the route.

For output, add `10⁻⁸ max(1,upper)` to the allowance. This small upward
guard keeps the printed route feasible despite summation and formatting
errors, while remaining well inside the required tolerance. It can make
a zero optimum appear as a tiny positive number. Positive route times
contain at most `n−1` terms; their binary64 accumulation error is much
smaller than this guard. Python's stopping error is also smaller than
the guard. Including divisions, the relative roundoff bound for at most
9999 positive terms is below `1.2·10⁻¹²`. Since `s≤300`, the speed guard
decreases every road time by at least `3.3·10⁻¹¹` relatively, which
dominates this error and output rounding.

Let `B≤62` count all Dijkstra runs, including the initial zero test and
final reconstruction. With lazy heap entries, time is `O(B(n+m)
log(n+m))` and memory is `O(n+m)`. The heap may contain more than `n`
entries when roads are parallel.

In the first example, roads 2 and 3 have total time `200/(80+20)=2`,
whereas the direct road takes `150/(50+20)>2`. Thus the minimum
allowance is 20. In the second example, one hour at the original speed
limit suffices, so the optimum is zero.

Pitfalls:

- Divide length by speed; increasing speed does not subtract a fixed
  amount from travel time.
- An allowance of zero must be tested before searching.
- Preserve road indices, including parallel roads, and print them from
  start to destination.
- Rerun the final feasible test: the last midpoint may have been infeasible.
- Keep the feasible upper endpoint and print enough digits; downward
  rounding can invalidate a tight path.
- For tight deadlines such as test `case_010`, distinguish exact route
  feasibility from checker acceptance: the checker applies the allowance
  tolerance to the route check too. For printed `P`, it uses `P+ε` when
  `P≤1−ε`, otherwise `P/(1−ε)`, where `ε=10⁻⁶`.

## Language notes

C++, Go, Python and Rust use standard binary heaps. Java stores
adjacency links and a binary heap in primitive arrays, reusing them
between checks. Costs are computed once per road for each test. Python
uses a bracket-width stopping test to avoid unnecessary bisections. All
versions retain predecessor road indices and include the small upward
numerical guard.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1980_binary_search_dijkstra.cpp](1980_binary_search_dijkstra.cpp) | G++ 13.2 x64 | binary_search, dijkstra | O(B(n+m)log(n+m)) | AC | 0.031 s | 1064 KB |
| [1980_binary_search_dijkstra.go](1980_binary_search_dijkstra.go) | Go 1.14 x64 | binary_search, dijkstra | O(B(n+m)log(n+m)) | AC | 0.093 s | 7196 KB |
| [1980_binary_search_dijkstra.java](1980_binary_search_dijkstra.java) | Java 1.8 | binary_search, dijkstra | O(B(n+m)log(n+m)) | AC | 0.109 s | 2008 KB |
| [1980_binary_search_dijkstra.py](1980_binary_search_dijkstra.py) | Python 3.12 x64 | binary_search, dijkstra | O(B(n+m)log(n+m)) | AC | 0.406 s | 8356 KB |
| [1980_binary_search_dijkstra.rs](1980_binary_search_dijkstra.rs) | Rust 1.75 x64 | binary_search, dijkstra | O(B(n+m)log(n+m)) | AC | 0.046 s | 1948 KB |
