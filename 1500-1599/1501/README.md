# 1501. Sense of Beauty

[Timus 1501](https://acm.timus.ru/problem.aspx?space=1&num=1501) · difficulty 268 · dp

Original problem by Leonid Volkov and Stanislav Vasiliev, from the Yekaterinburg quarterfinal of the 31st ACM ICPC, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two piles of N cards each (4 ≤ N ≤ 1000) hold N red and N black cards in
total. The croupier repeatedly takes the top card of either pile and
puts it on a red or a black pile, until all cards are moved. At every
moment the red and the black piles may differ by at most one card. Print
the piles the cards are taken from, as 2N digits 1 and 2, or
"Impossible".

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

N, then the two piles from top to bottom, 1 for red and 0 for black.

## Output

The 2N digits, or "Impossible". Any fitting order is accepted.

## Checking

Accept any interleaving that uses both source strings in order and respects the balance restriction at every prefix.

## Examples

### Example 1

Input:

```
4
0011
0110
```

Output:

```
22121112
```

### Example 2

Input:

```
4
1100
1100
```

Output:

```
Impossible
```

## Solution

A moment is described by the numbers i and j of cards taken from the
two piles. With d = 2 · (red cards) − (cards) counted over each pile's
taken part, the red and black piles differ by d1[i] + d2[j], so the
state is allowed when that is −1, 0 or 1. A state is reachable when it
is allowed and the state above or to the left of it is reachable;
(0, 0) starts. If (N, N) is reachable, walk back from it, taking any
reachable predecessor, and read the moves backwards. `O(N²)`.

Pitfalls:

- the condition applies after every single move, not only at the end
  (test 02, gen4);
- many orders can be right, so the tests use a checker (all tests);
- with the 0.5-second limit the table of N² states must be cheap; the
  Python solution keeps each row as one integer mask and spreads
  reachability along runs of allowed states with one addition.

## Optimized solutions

Keep the balance-grid DP, but reconstruct a valid path by divide and conquer. Compute forward and backward reachability on a middle row and recurse through a column belonging to both frontiers. Every reconstructed part therefore joins two reachable endpoints while respecting the balance bound. Reuse frontier buffers instead of retaining the full matrix. A single-row subproblem explicitly chooses the connecting vertical edge, ensuring that recursion always shrinks.

- `1501_dp_optimized.cpp`: 0.015 s / 116 KB; base `1501_dp.cpp`: 0.015 s / 856 KB; relative change: time -0.0%, memory -86.4%.
- `1501_dp_optimized.go`: 0.015 s / 916 KB; base `1501_dp.go`: 0.031 s / 2216 KB; relative change: time -51.6%, memory -58.7%.
- `1501_dp_optimized.java`: 0.125 s / 456 KB; base `1501_dp.java`: 0.109 s / 2704 KB; relative change: time +14.7%, memory -83.1%.
- `1501_dp_optimized.rs`: 0.046 s / 196 KB; base `1501_dp.rs`: 0.031 s / 1164 KB; relative change: time +48.4%, memory -83.2%.

## Language notes

The saved rating snapshot is from 1–2 November 2026. C++ requires the top 15% or the first 10 places in both time and memory; other families require first place in both. Equal results share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `1501_dp.cpp`; covering source `1501_dp_optimized.cpp`; time/memory places 1/1, other-author entries 61/61.

- Go: preferred teaching base `1501_dp.go`; covering source `1501_dp.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1501_dp.java`; covering source `1501_dp_optimized.java`; time/memory places 3/1, other-author entries 3/3.

- Python/PyPy: preferred teaching base `1501_dp.py`; covering source `1501_dp.py`; time/memory places 1/1, other-author entries 7/7.

- Rust: preferred teaching base `1501_dp.rs`; covering source `1501_dp.rs`; time/memory places 1/1, other-author entries 1/1.

## Solutions

The simple table includes the preferred teaching sources and preserved Accepted alternatives. The language notes identify the preferred base for each family.

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1501_dp.cpp](1501_dp.cpp) | G++ 13.2 x64 | dp | O(N^2) | AC | 0.015 s | 856 KB | 11287253 |
| [1501_dp.go](1501_dp.go) | Go 1.14 x64 | dp | O(N^2) | AC | 0.031 s | 2216 KB | 11287254 |
| [1501_dp.java](1501_dp.java) | Java 1.8 | dp | O(N^2) | AC | 0.109 s | 2704 KB | 11287256 |
| [1501_dp.py](1501_dp.py) | Python 3.12 x64 | dp | O(N^2) | AC | 0.093 s | 836 KB | 11287255 |
| [1501_dp.rs](1501_dp.rs) | Rust 1.75 x64 | dp | O(N^2) | AC | 0.031 s | 1164 KB | 11287257 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1501_dp_optimized.cpp](1501_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(N^2) | AC | 0.015 s | 116 KB | 11309287 |
| [1501_dp_optimized.go](1501_dp_optimized.go) | Go 1.14 x64 | dp | O(N^2) | AC | 0.015 s | 916 KB | 11309289 |
| [1501_dp_optimized.java](1501_dp_optimized.java) \* | Java 1.8 | dp | O(N^2) | AC | 0.125 s | 456 KB | 11309288 |
| [1501_dp_optimized.rs](1501_dp_optimized.rs) \* | Rust 1.75 x64 | dp | O(N^2) | AC | 0.046 s | 196 KB | 11309290 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
