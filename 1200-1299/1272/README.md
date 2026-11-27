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
7 4 4
1 2
2 3
4 5
6 7
1 3
2 4
5 6
6 7
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
`O((N+K)log(N+1))`.

Pitfalls:

- the bridges do not matter, only that they connect the groups, which
  the statement promises;
- tunnels may repeat or join an island to itself (test 05);
- with one island, or tunnels alone connecting everything, the answer
  is 0 (tests 02, 04).

All simple files and the native fast files link roots without rank and use path halving. The logarithmic DSU bound is amortized, including naive linking ([Tarjan–van Leeuwen, Lemmas 7–8](https://doi.org/10.1145/62.2160)); one find can be linear. It is not an inverse-Ackermann claim for those implementations. Let Iᶜ be input bytes actually consumed, including bounded reader prefetch. Time is O((N+K)log(N+1)+Iᶜ). Simple C++/Go/Java stop parsing after tunnels; Python/Rust simple read the full file. Fast C++/Go/Rust consume bridge records, while fast Java and Python need only a prefix. Thus M contributes through consumed input where applicable.

Simple C++/Go/Java keep N+1 parents plus bounded reader B: O(N+B). Simple Python retains split whole input, and Rust the entire String: O(N+I). Fast Go uses N+1 uint16 parents; Rust/Java N+1 native parents plus bounded buffers: O(N+B). Fast C++ reserves 10001 parent slots regardless of N, O(W+B) for W=10000. Fast Python uses N+1 negative size/root entries plus 1024-byte token chunks, O(N+B); n=1 or k=0 returns before DSU allocation. No bridge list is stored by the streamed versions.

## Optimized solutions

`1272_dsu_optimized.py` combines union by size with path splitting. It saves the old parent as next_vertex, rewires the current node toward its grandparent, then advances to the old parent; halving would advance to the new parent. Negative root entries store sizes. Connected full input guarantees answer components−1, so no bridge records are needed; finish at one component, or return N−1 without DSU if n=1 or k=0. Parse only needed tokens in 1024-byte chunks. DSU work is O(N+K·α(N)) amortized, plus consumed-byte input, and O(N+B) space. No algorithm was changed by this documentation correction.

Historical exact-source Python 3.12 #11327776 remains 0.078 s / 784 KB. Saved 2026-11-20 cohort time 3/99, memory 2/99: below 1024 KB only time is required, without a separate first-place target. Earlier #11304489 is the distinct historical pair 0.109 s / 1076 KB.

- `1272_dsu_optimized.py`: 0.078 s / 784 KB; retained teaching base `1272_dsu.py`: 0.093 s / 3328 KB.

`1272_dsu_optimized.java` keeps unranked root linking with path halving, replacing StreamTokenizer with fixed-byte input. It ignores bridge suffix records after processing tunnels. Its DSU term has the same amortized logarithmic bound as the simple native versions; O(N+K·N) is only a looser per-find bound, not a different algorithm. Storage O(N+B). Historical Java pairs remain 0.140 s / 488 KB for the base and 0.109 s / 512 KB for fast input.

Compared with `1272_dsu.java`: time 0.140 s → 0.109 s; memory 488 KB → 512 KB.

The optimized C++ solution parses the numbers by hand from a 4 KB buffer
instead of `scanf` and keeps the parents in a fixed global array of
10 001 cells, enough for `N ≤ 10 000`, instead of a `std::vector`. It
also reads the bridges to the end, which the simple solution leaves
unread: [1272_dsu_optimized.cpp](1272_dsu_optimized.cpp).

The optimized Go solution parses the numbers byte by byte from the
`bufio.Reader` instead of `fmt.Fscan` and keeps the parents as `uint16`,
which holds island numbers up to 10 000, instead of `int`. It also reads
the bridges to the end, which the simple solution leaves unread:
[1272_dsu_optimized.go](1272_dsu_optimized.go).

The optimized Rust solution parses the numbers by hand from a 4 KB
buffer refilled from standard input instead of reading the whole input
into a `String`, so only the parents and the buffer stay in memory:
[1272_dsu_optimized.rs](1272_dsu_optimized.rs).

### Measured gains

The paired gains below are historical observations. Admission uses the shared rating policy; no separate 30%-resource-gain rule or first-place requirement applies. Keep meaningful simple implementations even if they miss required metrics.

- `1272_dsu_optimized.cpp`: time reduction +51.61%; memory reduction
  +49.12%; base: `1272_dsu.cpp`.

- `1272_dsu_optimized.go`: time reduction -106.67%; memory reduction
  +35.85%; base: `1272_dsu.go`.

- `1272_dsu_optimized.rs`: time reduction +0.00%; memory reduction
  +63.93%; base: `1272_dsu.rs`.

## Language notes

Source-bound saved audit: fast C++/Java/Python qualify by ordinary time; both Rust pairs by ordinary time; both Go pairs by the sparse exact-compiler reference (base 1428 KB requires both metrics, fast 916 KB only time). Simple C++/Java/Python miss required comparisons and remain teaching files. The shared [rating criteria](../../RATING_CRITERIA.md) apply to every family, with time only below 1024 KB. Historical Java cohort 6/90 time and 2/90 memory is retained as an old snapshot, not a separate admission rule. All nine newly commented hashes still need fresh exact-source Accepted; fast Java is unchanged.

The statement “every bridge joins two tunnel components” was corrected in all nine files: bridges may be internal, but the promised connected full network supplies enough crossing bridges. Only these explanatory lines changed; executable code, simple versions and all other meaningful comments are preserved. Table IDs/time/memory remain historical paired Accepted measurements.

The source revisions discussed above have now received their own Accepted results. The solution tables list the final source-matched submission IDs and paired time/memory measurements; earlier observations describe previous revisions. All meaningful simple implementations remain available.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1272_dsu.cpp](1272_dsu.cpp) | G++ 13.2 x64 | dsu | O((N+K)log(N+1)+Iᶜ) amortized | AC | 0.015 s | 216 KB | 11331137 |
| [1272_dsu.go](1272_dsu.go) | Go 1.14 x64 | dsu | O((N+K)log(N+1)+Iᶜ) amortized | AC | 0.031 s | 1396 KB | 11331005 |
| [1272_dsu.java](1272_dsu.java) | Java 1.8 | dsu | O((N+K)log(N+1)+Iᶜ) amortized | AC | 0.109 s | 472 KB | 11331044 |
| [1272_dsu.py](1272_dsu.py) | Python 3.12 x64 | dsu | O((N+K)log(N+1)+Iᶜ) amortized | AC | 0.125 s | 3220 KB | 11331064 |
| [1272_dsu.rs](1272_dsu.rs) | Rust 1.75 x64 | dsu | O((N+K)log(N+1)+Iᶜ) amortized | AC | 0.015 s | 724 KB | 11331101 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1272_dsu_optimized.cpp](1272_dsu_optimized.cpp) | G++ 13.2 x64 | dsu | O((N+K)log(N+1)+Iᶜ) amortized | AC | 0.015 s | 128 KB | 11331138 |
| [1272_dsu_optimized.go](1272_dsu_optimized.go) | Go 1.14 x64 | dsu | O((N+K)log(N+1)+Iᶜ) amortized | AC | 0.031 s | 924 KB | 11331006 |
| [1272_dsu_optimized.py](1272_dsu_optimized.py) | Python 3.12 x64 | dsu | O(N+K·α(N)+Iᶜ) amortized | AC | 0.078 s | 888 KB | 11331065 |
| [1272_dsu_optimized.rs](1272_dsu_optimized.rs) | Rust 1.75 x64 | dsu | O((N+K)log(N+1)+Iᶜ) amortized | AC | 0.062 s | 268 KB | 11331102 |
| [1272_dsu_optimized.java](1272_dsu_optimized.java) | Java 1.8 | dsu | O((N+K)log(N+1)+Iᶜ) amortized | AC | 0.109 s | 512 KB | 11325012 |
