# 1160. Connecting all hubs so that the longest cable is as short as possible

[Timus 1160](https://acm.timus.ru/problem.aspx?space=1&num=1160) · difficulty 140 · dsu

Original problem by Andrew Stankevich, from the Northern Subregion of the ACM ICPC Northeastern European Regional Contest 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`2 ≤ N ≤ 1000` hubs can be joined by `1 ≤ M ≤ 15000` possible cables of
given lengths. Choose cables that connect every hub to every other,
directly or through others, so that the longest chosen cable is as short
as possible. Print that length, then the number of cables and the cables
themselves.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N` and `M`, then `M` lines with two hubs, numbered from 1 to `N`,
and a length, an integer from 1 to 10⁶.

## Output

The longest cable, the number of cables `P`, then `P` pairs of hubs.

## Checking

Any plan is accepted if it connects all hubs with possible cables and its
longest cable is the smallest possible. The checker finds that smallest
length on its own, by binary search over the lengths with a connectivity
test, and verifies the printed length and plan.

## Examples

### Example 1

Input:

```
4 6
1 2 1
1 3 1
1 4 2
2 3 1
3 4 1
2 4 1
```

Output:

```
1
3
1 2
1 3
3 4
```

## Solution

Kruskal's algorithm builds a spanning tree from the shortest cables up,
skipping a cable whose ends are already connected, with a disjoint-set
union to tell. The tree it builds is a minimum spanning tree, and a
minimum spanning tree also minimises its longest edge: when Kruskal's
algorithm adds its last, longest edge `e`, the cables shorter than `e`
leave the hubs in at least two separate groups, so every connecting plan
needs a cable at least as long as `e`. The answer is the length of the last
edge taken, and the tree's `N − 1` cables are a valid plan.
`O(M log M)` (`O(M log² M)` in Go).

Pitfalls:

- the plan does not have to be a tree, and any plan with the smallest
  longest cable is accepted;
- every hub must be reached, so the last edge Kruskal takes, not the last
  one considered, gives the answer;
- equal lengths need no special care.

The answers were checked by the checker on every test and on 60 random
networks.

## Optimized solutions

The optimized C++ solution parses the numbers by hand from a 4 KB buffer
instead of `scanf` and keeps the cables in a fixed array of 8-byte
records: the length in an `int` and the two hubs in `uint16_t`, which
holds hub numbers up to 1000. It sorts them in place with `std::sort`
instead of `std::stable_sort`, which needs a temporary copy, stops
Kruskal's algorithm after `N − 1` cables and prints with `printf`
instead of building the output in a string: {1160_dsu_optimized.cpp}.

The optimized Java solution parses the numbers by hand from a 4 KB
buffer instead of `StreamTokenizer` and packs each cable into one
`long`: two hubs of 10 bits each, enough for numbers up to 1000, and the
length, up to 10⁶, above them. Sorting the plain `long` array orders the
cables by length with no array per cable and no comparator, and
Kruskal's algorithm stops after `N − 1` cables:
{1160_dsu_optimized.java}.

The optimized Python solution reads the input in 8 KB chunks and
converts the tokens chunk by chunk instead of splitting the whole input
at once. It packs each cable into one integer, the length above two
10-bit hub numbers (hubs are at most 1000), so that a plain `sort`
orders the cables by length without tuples or a key function, and
Kruskal's algorithm stops after `N − 1` cables: {1160_dsu_optimized.py}.

The optimized Rust solution parses the numbers by hand from a 4 KB
buffer instead of reading the whole input into a `String`. Each cable is
an 8-byte tuple of a `u32` length and two `u16` hubs instead of three
`usize` values, the sorting is `sort_unstable`, which needs no extra
buffer, Kruskal's algorithm stops after `N − 1` cables, and the output
goes through a `BufWriter`: {1160_dsu_optimized.rs}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1160_dsu_optimized.cpp`: time reduction +51.61%; memory reduction
  +52.29%; base: `1160_dsu.cpp`.

- `1160_dsu_optimized.java`: time reduction +54.39%; memory reduction
  +78.51%; base: `1160_dsu.java`.

- `1160_dsu_optimized.py`: time reduction -19.23%; memory reduction
  +72.78%; base: `1160_dsu.py`.

- `1160_dsu_optimized.rs`: time reduction -106.67%; memory reduction
  +69.20%; base: `1160_dsu.rs`.

## Language notes

- All languages sort the cables and run the same union with path
  halving.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1160_dsu.cpp](1160_dsu.cpp) | G++ 13.2 x64 | dsu | O(M log M) | AC | 0.031 s | 436 KB | 11281720 |
| [1160_dsu.go](1160_dsu.go) | Go 1.14 x64 | dsu | O(M log² M) | AC | 0.062 s | 1808 KB | 11304467 |
| [1160_dsu.java](1160_dsu.java) | Java 1.8 | dsu | O(M log M) | AC | 0.171 s | 3500 KB | 11281766 |
| [1160_dsu.py](1160_dsu.py) | Python 3.12 x64 | dsu | O(M log M) | AC | 0.078 s | 5864 KB | 11281753 |
| [1160_dsu.rs](1160_dsu.rs) | Rust 1.75 x64 | dsu | O(M log M) | AC | 0.015 s | 1104 KB | 11281779 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1160_dsu_optimized.cpp](1160_dsu_optimized.cpp) | G++ 13.2 x64 | dsu | O(M log M) | AC | 0.015 s | 208 KB | 11304463 |
| [1160_dsu_optimized.java](1160_dsu_optimized.java) | Java 1.8 | dsu | O(M log M) | AC | 0.078 s | 752 KB | 11304464 |
| [1160_dsu_optimized.py](1160_dsu_optimized.py) \* | Python 3.12 x64 | dsu | O(M log M) | AC | 0.093 s | 1596 KB | 11304465 |
| [1160_dsu_optimized.rs](1160_dsu_optimized.rs) \* | Rust 1.75 x64 | dsu | O(M log M) | AC | 0.031 s | 340 KB | 11304466 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
