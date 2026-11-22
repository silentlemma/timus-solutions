# 1650. Billionaires

[Timus 1650](https://acm.timus.ru/problem.aspx?space=1&num=1650) · difficulty 174 · segment_tree

Original problem by Pavel Atnashev, from the NEERC 2008 Eastern Subregional Quarterfinal.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n billionaires with known fortunes start in given cities. Over m days
they travel: a trip on day d leaves in the evening and arrives the next
morning, so it counts from day d + 1. For each city, count the days on
which its billionaires together were strictly the richest of all
cities, and list the cities with at least one such day, sorted by name.

## Input

n (1 ≤ n ≤ 10000), then n lines "name city fortune" (fortunes from 1 to
10¹¹). Then m and k (1 ≤ m ≤ 50000, 0 ≤ k ≤ 50000) and k lines "day name
destination" (1 ≤ day ≤ m − 1) in increasing order of day; nobody
travels more than once a day. Names and cities are up to 20 Latin
letters, case-sensitive.

## Output

"city days" for every city that led on at least one day, in plain
character order (ABC…Zabc…z).

## Examples

### Example 1

Input:

```
5
Abramovich London 15000000000
Deripaska Moscow 10000000000
Potanin Moscow 5000000000
Berezovsky London 2500000000
Khodorkovsky Chita 1000000000
25 9
1 Abramovich Anadyr
5 Potanin Courchevel
10 Abramovich Moscow
11 Abramovich London
11 Deripaska StPetersburg
15 Potanin Norilsk
20 Berezovsky Tbilisi
21 Potanin StPetersburg
22 Berezovsky London
```

Output:

```
Anadyr 5
London 14
Moscow 1
```

## Solution

Give every city that ever appears an index and keep a segment tree over
the city totals. Each node stores the largest total below it, how many
leaves reach it, and one of those leaves, so the root tells at once
whether one city is strictly ahead and which. A trip is two point
updates: the fortune leaves one city and joins another.

Between two travel days the leader does not change, so the days are
counted in blocks: before applying the trips of day d, the current
leader (if it is unique) gets the days from the last counted day to d;
after the last trip it gets the days up to m. Totals reach 10¹⁵, so
they are 64-bit. `O((n + k) log C)` for C cities.

Pitfalls:

- a tie at the top means nobody leads that day (test 03), so the input
  may produce no output at all;
- trips on day d still leave day d to the old city;
- the order is by character codes, so uppercase names come before all
  lowercase ones (test 05).

The answers match a day-by-day count on 60 random histories and an
independent accepted implementation on generated tests. That
implementation goes wrong when someone "travels" to the city they are
already in, which the judge's tests evidently never contain; the
program here treats such a trip as staying put.

## Optimized solutions

`1650_greedy.py`. Replace the segment tree by a lazy maximum heap and a separate wealth-frequency map counting cities, not stale heap entries. Pack (-wealth,city) in one integer: city<60000 fits sixteen low bits. Discard obsolete maxima; a unique current maximum earns the elapsed days, with moves effective next morning. Rebuild when stale entries exceed 3C+1024, and skip zero-length credits. C is number of cities; expected/amortized O((N+K)log C+C log C) time including final name sorting, O(N+C) records plus stored name/output bytes. Preserve the segment-tree alternative and teaching sources.

Exact-source Python 3.12 x64 Accepted #11327774: 0.39 s / 14828 KB. Saved 2026-11-20 compiler-cohort ranks, time then memory: 6/49; 1/49. Strict admission uses both time and memory at 1024 KB or above: top ten or top 15%, ties share rank and percentage cutoff rounds up. An asterisk remains for the separate first-place-in-both language target. The preserved previous variant has its own paired receipt #11307267 (Python 3.12 x64): 1.046 s / 16232 KB; do not mix measurements or runtimes. All teaching sources remain unchanged.

- `1650_greedy.py`: 0.39 s / 14828 KB; retained teaching base `1650_segment_tree.py` (Python 3.12 x64): 1.062 s / 27776 KB.

The C++ revision keeps streamed trips, the map of people and fortunes, and the segment-tree maximum/unique-leader state with early-stopping updates. Names of at most twenty letters are stored directly in fixed 21-byte keys in the maps and name list, removing separate string allocations. Hash matches still require full strcmp equality, and sorting uses the same lexicographic comparison; collisions cannot change an answer.

Exact-source Accepted (G++ 13.2 x64, #11326653: 0.187 s / 8912 KB); teaching base `1650_segment_tree.cpp`: 0.125 s / 20700 KB. The previous optimized measurement was 0.187 s / 10156 KB. In the saved 20 November 2026 comparison, time place is 22/434, memory place 51/434; below 1 MiB the policy evaluates the time rank only.

The optimized Go solution reads the trips one at a time and applies each
as soon as it is read, instead of storing them all first: a trip brings
at most one new city, so the tree is sized from the start for the
starting cities plus k. One map from a name to the city and fortune
replaces two, a node keeps the index of its single leading city, or a
tie mark, instead of a count of leaves, the tree is built bottom-up from
the starting totals, and an update stops climbing as soon as a node
keeps its maximum and its leader, since nothing above it can change
then. The words come from a `bufio.Scanner` instead of `fmt.Fscan`:
{1650_segment_tree_optimized.go}.

The optimized Java solution reads the trips one at a time and applies
each as soon as it is read, instead of storing them all first: a trip
brings at most one new city, so the tree is sized from the start for the
starting cities plus k. One map from a name to the city and fortune
replaces two, a node keeps the index of its single leading city, or a
tie mark, instead of a count of leaves, the tree is built bottom-up from
the starting totals, and an update stops climbing as soon as a node
keeps its maximum and its leader, since nothing above it can change
then. The tokens are read line by line instead of collecting the whole
input in a `StringBuilder` first: {1650_segment_tree_optimized.java}.

The optimized Python solution reads the trips one at a time and applies
each as soon as it is read, instead of storing them all first: a trip
brings at most one new city, so the tree is sized from the start for the
starting cities plus k. One map from a name to the city and fortune
replaces two, a node keeps the index of its single leading city, or a
tie mark, instead of a count of leaves, the tree is built bottom-up from
the starting totals, and an update stops climbing as soon as a node
keeps its maximum and its leader, since nothing above it can change
then. The input is read line by line, one record per line, instead of
all at once: {1650_segment_tree_optimized.py}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1650_segment_tree_optimized.cpp`: time reduction -49.60%; memory reduction +56.95%; base: `1650_segment_tree.cpp`.

- `1650_segment_tree_optimized.go`: time reduction +45.61%; memory
  reduction +1.04%; base: `1650_segment_tree.go`.

- `1650_segment_tree_optimized.java`: time reduction -15.27%; memory
  reduction +46.58%; base: `1650_segment_tree.java`.

- `1650_segment_tree_optimized.py`: time reduction +1.51%; memory
  reduction +41.56%; base: `1650_segment_tree.py`.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1650_segment_tree.cpp](1650_segment_tree.cpp) | G++ 13.2 x64 | segment_tree | O((n + k) log C) | AC | 0.125 s | 20700 KB | 11304018 |
| [1650_segment_tree.go](1650_segment_tree.go) | Go 1.14 x64 | segment_tree | O((n + k) log C) | AC | 0.171 s | 18416 KB | 11288517 |
| [1650_segment_tree.java](1650_segment_tree.java) | Java 1.8 | segment_tree | O((n + k) log C) | AC | 0.203 s | 27324 KB | 11288519 |
| [1650_segment_tree.py](1650_segment_tree.py) | Python 3.12 x64 | segment_tree | O((n + k) log C) | AC | 1.062 s | 27776 KB | 11288518 |
| [1650_segment_tree.rs](1650_segment_tree.rs) | Rust 1.75 x64 | segment_tree | O((n + k) log C) | AC | 0.046 s | 13036 KB | 11304019 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1650_segment_tree_optimized.cpp](1650_segment_tree_optimized.cpp) | G++ 13.2 x64 | segment_tree | O((n + k) log C) | AC | 0.187 s | 8912 KB | 11326653 |
| [1650_segment_tree_optimized.go](1650_segment_tree_optimized.go) \* | Go 1.14 x64 | segment_tree | O((n + k) log C) | AC | 0.093 s | 18224 KB | 11307269 |
| [1650_segment_tree_optimized.java](1650_segment_tree_optimized.java) \* | Java 1.8 | segment_tree | O((n + k) log C) | AC | 0.234 s | 14596 KB | 11307271 |
| [1650_segment_tree_optimized.py](1650_segment_tree_optimized.py) \* | Python 3.12 x64 | segment_tree | O((n + k) log C) | AC | 1.046 s | 16232 KB | 11307267 |
| [1650_greedy.py](1650_greedy.py) \* | Python 3.12 x64 | greedy | Expected/amortized O((N+K)log C+C log C); O(N+C) records plus names/output | AC | 0.39 s | 14828 KB | 11327774 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
