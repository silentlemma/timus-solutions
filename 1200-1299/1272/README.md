# 1272. Non-Yekaterinburg subway

[Timus 1272](https://acm.timus.ru/problem.aspx?space=1&num=1272) · difficulty 144 · dsu

Original problem by Magaz Asanov (prepared by Igor Goldberg), from the Ural State University Championship, October 25, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A town stands on 1 ≤ N ≤ 10 000 islands joined by 0 ≤ K ≤ 12 000
tunnels and 0 ≤ M ≤ 12 000 bridges, and all of them together connect
every island. A subway must connect all islands using some of these
links, with as few bridges as possible. How many bridges does it need?

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, K and M, then K tunnels and M bridges, each as two island numbers
from 1 to N.

## Output

The least number of bridges.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
6 3 4
1 2
2 3
4 5
1 3
3 4
4 6
5 6
```

Output:

```
2
```

## Solution

Tunnels cost nothing, so take all of them: they split the islands into
groups that are already connected. Each bridge can join at most two
groups into one, and since the whole network is connected, bridges can
always be chosen to join the groups one by one. So the answer is the
number of tunnel groups minus one, counted with a union–find structure
over the tunnels; bridge endpoints are ignored.
`O((N + K) log N)`.

Pitfalls:

- the bridges do not matter, only that they connect the groups, which
  the statement promises;
- tunnels may repeat or join an island to itself (test 05);
- with one island, or tunnels alone connecting everything, the answer
  is 0 (tests 02, 04).

## Optimized solutions

`1272_dsu_optimized.py`. Keep union by size with path halving. The promised complete network is connected, so the minimum paid bridges is the number of tunnel components minus one; bridge endpoints never change this count. With one vertex or no tunnels, return N−1 without allocating DSU. Stop when tunnel unions reach one component. Parse only needed tokens in 1024-byte chunks; the unused bridge suffix need not be read. O(N+K·α(N)) worst-case algorithmic time and O(N) DSU storage plus bounded parsing buffers; early exits can use less.

Exact-source Python 3.12 x64 Accepted #11327776: 0.078 s / 784 KB. Saved 2026-11-20 compiler-cohort comparison: time 3/99, memory 2/99. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11304489 was 0.109 s / 1076 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1272_dsu_optimized.py`: 0.078 s / 784 KB; retained teaching base `1272_dsu.py`: 0.093 s / 3328 KB.

`1272_dsu_optimized.java`. Keep the tunnel-component DSU: initialize N groups, decrement only on a union of distinct roots, then output groups-1. The promise that all links connect the town makes that many bridges sufficient. As in the base, only the tunnel endpoints are needed; bridge records need not be retained or consumed after the answer is known. The same unranked root linking and path halving remain, so this is an input-runtime change, not a new connectivity algorithm. Storage O(N); a direct conservative worst-case bound is O(N+K·N), charging at most N parent links to each find. Fixed byte input replaces StreamTokenizer.

Compared with `1272_dsu.java`: time 0.140 s → 0.109 s; memory 488 KB → 512 KB.

The optimized C++ solution parses the numbers by hand from a 4 KB buffer
instead of `scanf` and keeps the parents in a fixed global array of
10 001 cells, enough for `N ≤ 10 000`, instead of a `std::vector`. It
also reads the bridges to the end, which the simple solution leaves
unread: {1272_dsu_optimized.cpp}.

The optimized Go solution parses the numbers byte by byte from the
`bufio.Reader` instead of `fmt.Fscan` and keeps the parents as `uint16`,
which holds island numbers up to 10 000, instead of `int`. It also reads
the bridges to the end, which the simple solution leaves unread:
{1272_dsu_optimized.go}.

The optimized Rust solution parses the numbers by hand from a 4 KB
buffer refilled from standard input instead of reading the whole input
into a `String`, so only the parents and the buffer stay in memory:
{1272_dsu_optimized.rs}.

### Measured gains

Each optimized version has Accepted and meets a ranking or resource-improvement
admission criterion. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1272_dsu_optimized.cpp`: time reduction +51.61%; memory reduction
  +49.12%; base: `1272_dsu.cpp`.

- `1272_dsu_optimized.go`: time reduction -106.67%; memory reduction
  +35.85%; base: `1272_dsu.go`.

- `1272_dsu_optimized.rs`: time reduction +0.00%; memory reduction
  +63.93%; base: `1272_dsu.rs`.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1272_dsu_optimized.java`: time place 6/90, memory place 2/90 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1272_dsu.cpp](1272_dsu.cpp) | G++ 13.2 x64 | dsu | O((N + K) log N) | AC | 0.031 s | 228 KB | 11284262 |
| [1272_dsu.go](1272_dsu.go) | Go 1.14 x64 | dsu | O((N + K) log N) | AC | 0.015 s | 1428 KB | 11284264 |
| [1272_dsu.java](1272_dsu.java) | Java 1.8 | dsu | O((N + K) log N) | AC | 0.140 s | 488 KB | 11284270 |
| [1272_dsu.py](1272_dsu.py) | Python 3.12 x64 | dsu | O((N + K) log N + M) | AC | 0.093 s | 3328 KB | 11284266 |
| [1272_dsu.rs](1272_dsu.rs) | Rust 1.75 x64 | dsu | O((N + K) log N + M) | AC | 0.046 s | 732 KB | 11284276 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1272_dsu_optimized.cpp](1272_dsu_optimized.cpp) | G++ 13.2 x64 | dsu | O((N + K) log N + M) | AC | 0.015 s | 116 KB | 11304487 |
| [1272_dsu_optimized.go](1272_dsu_optimized.go) | Go 1.14 x64 | dsu | O((N + K) log N + M) | AC | 0.031 s | 916 KB | 11304488 |
| [1272_dsu_optimized.py](1272_dsu_optimized.py) | Python 3.12 x64 | dsu | O(N+K·α(N)) time; O(N) plus bounded token buffers | AC | 0.078 s | 784 KB | 11327776 |
| [1272_dsu_optimized.rs](1272_dsu_optimized.rs) | Rust 1.75 x64 | dsu | O((N + K) log N + M) | AC | 0.046 s | 264 KB | 11304490 |
| [1272_dsu_optimized.java](1272_dsu_optimized.java) | Java 1.8 | dsu | O(N+K·N) conservative worst case | AC | 0.109 s | 512 KB | 11325012 |
