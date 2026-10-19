# 1949. Priority Film Schedules

[Timus 1949](https://acm.timus.ru/problem.aspx?space=1&num=1949) · difficulty 1401 · matching

Original problem from Open Ural FU Personal Contest 2012 | by Vitaliy Belokobilskiy, Sergey Madzhuga.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are n films and k viewers. Film i occupies [a_i,b_i) and has a count
c_i. A viewer must watch each chosen film completely, cannot watch overlapping
films, and may follow one film only with a film whose count is no smaller.
An end exactly equal to the next start is allowed, as are equal counts.
Unused viewers and gaps between films are allowed; no travel time is needed.

Choose a feasible film set with lexicographically largest n-bit membership
string in input order, where 1 is preferred to 0. Thus any earlier film
outweighs all later films combined. Limits: 1 second, 64 MB.

## Input

n and k, 1≤k≤n≤100. Then n triples a_i,b_i,c_i in priority order, with
0≤a_i<b_i≤86399 and 1≤c_i≤10000. The order need not be chronological.

## Output

One string of n digits: bit i is 1 exactly when film i belongs to the
preferred feasible set. No viewer assignment is requested.

## Checking

Outputs are compared token by token; the optimal string is unique.

## Examples

```
4 2
1 5 10
3 6 20
5 10 9
5 10 10
```

```
1101
```

```
4 1
1 5 10
3 6 20
5 10 9
5 10 10
```

```
1001
```

## Solution

Make a directed edge i→j when b_i≤a_j and c_i≤c_j. Time strictly increases
along every edge, so the graph is acyclic. A viewer's schedule is a path.
For a selected set of s films, duplicate each vertex into a left and right
copy and retain these edges between copies. If the maximum bipartite
matching has M edges, the minimum number of viewers is s−M.

Proof: p disjoint schedule paths yield a matching of their consecutive
edges, s−p in total. Conversely matching edges give every film at most one
predecessor and successor. Acyclicity excludes cycles, so these edges form
s−M disjoint paths, each a valid schedule. Hence the set is feasible iff
s−M≤k.

Scan films in priority order, tentatively adding each one. If the selected
set is feasible, keep it: all remaining bits can at least be zero. Otherwise
reject it. Feasibility is hereditary: removing films from any viewer's
timeline preserves time order and nondecreasing counts. Therefore no later
additions can repair an infeasible selected subset. At every step the greedy
choice fixes the best achievable earliest bit, proving lexicographic optimality.

Maintain the maximum matching with two ordered searches per candidate:

1. Add only its left copy. Search a forward augmenting path from that copy
   using old active right targets, updating both matched-partner arrays.
2. Activate its right copy. Search a reverse augmenting path from this new
   right copy through predecessor edges to an unmatched left copy.

In the first phase, a newly created augmenting path must start at the new
unmatched left vertex; maximum matching size can increase by at most one.
One successful search reaches that bound, and a failed search proves the
old matching remains maximum. The same argument with sides reversed applies
to the second phase. The matching is thus maximum after both phases. Searching
only from the new left would miss improvements through the new right.

Use separate visited marks for the two searches. Save both matched arrays
and M before insertion; if s+1−M>k, deactivate the candidate and restore
all saved matching state. Accepted films remain active. Print the kept bits.

O(n³) time and O(n²) space. Building the graph costs O(n²); each of n
candidates performs two O(n²) alternating-path searches and O(n) snapshots.
Each search visits every opposite-side vertex at most once. Recursion depth
is at most n≤100.

Do not maximize film count or sum of c_i, and do not sort away priority order.
Time and count tests are non-strict. Matching requires both left and right
copies; a new film can improve either direction. Keep the new right inactive
during the first search. Previously rejected films must remain inactive.

## Language notes

Native versions use boolean adjacency matrices, active/visited arrays and
integer partner arrays. A generic augmenting-path function handles both
directions by swapping the graph and partner arrays. Python stores forward
and reverse neighbors as at most 100-bit integers. Do not use one 64-bit
mask for all films. Clear visited marks between phases and restore both maps
after rejection. All versions need only the standard library.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1949_matching.cpp](1949_matching.cpp) | G++ 13.2 x64 | matching | O(n^3) | AC | 0.031 s | 440 KB |
| [1949_matching.go](1949_matching.go) | Go 1.14 x64 | matching | O(n^3) | AC | 0.031 s | 1328 KB |
| [1949_matching.java](1949_matching.java) | Java 1.8 | matching | O(n^3) | AC | 0.125 s | 628 KB |
| [1949_matching.py](1949_matching.py) | Python 3.12 x64 | matching | O(n^3) | AC | 0.093 s | 740 KB |
| [1949_matching.rs](1949_matching.rs) | Rust 1.75 x64 | matching | O(n^3) | AC | 0.031 s | 264 KB |
