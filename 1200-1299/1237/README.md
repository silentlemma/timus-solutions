# 1237. Checking whether an evacuation plan is optimal

[Timus 1237](https://acm.timus.ru/problem.aspx?space=1&num=1237) · difficulty 985 · graphs

Original problem by Vladimir Kotov, from the ACM ICPC Northeastern European Regional Contest 2002–2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N buildings (N ≤ 100) hold B_i workers each, and M shelters (M ≤ 100)
hold at most C_j people each. Walking from building i to shelter j takes
`|X_i − P_j| + |Y_i − Q_j| + 1`. A plan says how many workers E_ij of each
building go to each shelter; it sends everyone and fits the capacities.
Decide whether the plan has the least total walking time, and if not,
show any valid plan with a smaller total.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and M; the buildings as `X Y B`; the shelters as `P Q C`; then the N
rows of the plan.

## Output

`OPTIMAL`, or `SUBOPTIMAL` followed by a better plan in the same format.

## Checking

Any better plan is accepted. The checker compares the first word with
the expected answer and checks that the plan sends every worker of each
building, fits every shelter and has a smaller total time than the given
one.

## Examples

### Example 1

Input:

```
3 4
-3 3 5
-2 -2 6
2 2 5
-1 1 3
1 1 4
-2 -2 7
0 -1 3
3 1 1 0
0 0 6 0
0 3 0 2
```

Output:

```
SUBOPTIMAL
3 0 1 1
0 0 6 0
0 4 0 1
```

### Example 2

Input:

```
3 4
-3 3 5
-2 -2 6
2 2 5
-1 1 3
1 1 4
-2 -2 7
0 -1 3
3 0 1 1
0 0 6 0
0 4 0 1
```

Output:

```
OPTIMAL
```

## Solution

The plan is a flow, and a flow has the least cost exactly when its
residual graph has no cycle of negative cost. Here that graph can be
built on the shelters alone, plus one extra node for spare room:

- **j → k** moves one worker of some building i from shelter j to
  shelter k, which needs `E_ij > 0` and costs `D_ik − D_ij`; the edge takes
  the cheapest such building;
- **j → spare**, cost 0, exists when shelter j has a free place;
- **spare → k**, cost 0, lets shelter k end up one worker short.

A cycle through shelters only moves a chain of workers and keeps every
shelter's load; a cycle through the spare node fills a free place at one
end and empties one at the other. Bellman–Ford from all nodes at once
either settles in at most M + 1 rounds (`OPTIMAL`), or still changes a
distance in the last round; then following predecessors M + 1 times lands
on a negative cycle, and moving one worker along each of its
shelter-to-shelter edges gives a cheaper valid plan. `O(N·M² + M³)`.

Pitfalls:

- leaving the given plan's spare room out of the graph misses
  improvements like test 05, where one worker should simply move to an
  empty nearer shelter;
- a simple cycle leaves each shelter once, so every move takes a worker
  that is really there.

The verdicts were compared with an exact min-cost flow on 399 random small
cities, and each better plan was run through the checker.

## Language notes

- Python relaxes all edges into one node at a time with `map`, and finds
  the building behind each cycle edge only for the edges of the cycle.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1237_graphs.cpp](1237_graphs.cpp) | G++ 13.2 x64 | graphs | O(N·M² + M³) | AC | 0.031 s | 372 KB |
| [1237_graphs.go](1237_graphs.go) | Go 1.14 x64 | graphs | O(N·M² + M³) | AC | 0.031 s | 1516 KB |
| [1237_graphs.java](1237_graphs.java) | Java 1.8 | graphs | O(N·M² + M³) | AC | 0.125 s | 952 KB |
| [1237_graphs.py](1237_graphs.py) | Python 3.12 x64 | graphs | O(N·M² + M³) | AC | 0.187 s | 1744 KB |
| [1237_graphs.rs](1237_graphs.rs) | Rust 1.75 x64 | graphs | O(N·M² + M³) | AC | 0.031 s | 564 KB |
