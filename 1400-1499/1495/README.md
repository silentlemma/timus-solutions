# 1495. One-two, One-two 2

[Timus 1495](https://acm.timus.ru/problem.aspx?space=1&num=1495) · difficulty 340 · bfs

Original problem by Igor Chevdar, from the Thirteenth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 14, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Find the smallest number written only with the digits 1 and 2 that is
divisible by N (1 ≤ N ≤ 10⁶). Print "Impossible" if there is none or if
it is longer than 30 digits.

Time limit: 2 seconds. Memory limit: 256 MB.

## Input

N.

## Output

The number, or "Impossible".

## Examples

### Example 1

Input:

```
5
```

Output:

```
Impossible
```

### Example 2

Input:

```
8
```

Output:

```
112
```

## Solution

Only the remainder modulo N matters for what can follow a prefix, so
search over remainders breadth-first. Start from the numbers 1 and 2,
and from a number with remainder r go to r·10 + 1 and then r·10 + 2.
Shorter numbers are reached first, and within one length the queue
stays in numeric order, so the first number to reach a remainder is the
smallest one with that remainder; any later number with it, and all
its extensions, would be larger. Each of the N remainders is stored
once with its last digit and its parent, and the answer is read back
along the parents once remainder 0 appears. Numbers stop growing at 30
digits. `O(N)`.

Pitfalls:

- a number of 1s and 2s never ends in 0 or 5, so multiples of 5 are
  impossible (tests 01, 07, 09);
- the answer can be exactly 30 digits long, as for 999999, which is
  still allowed (test 05);
- r·10 + d stays below 10⁷, but the full answer can exceed 64-bit integer
  ranges; reconstruct it from its digits (tests 05, 08).

## Optimized solutions

`1495_bfs_optimized.py`. Keep remainder BFS with digit order 1 then 2, a packed 32-bit predecessor/digit code and a 32-bit queue. Expand the two edges explicitly: compute (10*r+1)%N once and obtain the digit-2 remainder by adding one with wrap, without another modulo. Layer boundaries enforce at most 30 digits; visited order still gives the shortest and then lexicographically smallest answer. Divisibility by five remains an exact impossibility shortcut. O(N) work/storage under the length cap. This PyPy run uses 11808 KB versus the earlier 11404 KB, while time falls from 0.921 to 0.14 s; the small memory increase is explicit. The teaching BFS remains. The quoted earlier 0.921 s / 11404 KB run used CPython 3.12; the selected run uses PyPy 3.10. Both code and interpreter differ, so this is a paired-run comparison, not an isolated benchmark of the edge rewrite.

Exact-source PyPy 3.10 Accepted #11326708: 0.14 s / 11808 KB. Comparison saved 2026-11-20 on the current language-family compiler cohort: time rank 1/19, memory rank 1/19. At least 1024 KB: both strict metrics are required and pass.

- `1495_bfs_optimized.py`: 0.14 s / 11808 KB; retained teaching base `1495_bfs.py` (Python 3.12 x64): 0.906 s / 62744 KB; time change -84.5%; memory change -81.2%.

The C++, Go and Python variants use the same breadth-first search. Each remainder has one 32-bit entry. Zero marks it unseen, and otherwise the upper bits hold its predecessor plus one and the low bit holds the digit minus one. The queue also uses 32-bit entries and its layer boundaries give the length, so no per-remainder depth is needed.

Retained accepted bases [1495_bfs.go](1495_bfs.go), [1495_bfs.java](1495_bfs.java), [1495_bfs.rs](1495_bfs.rs) also pass the strict top-ten or top-15% criterion for required metrics in the saved comparison. They are reused without duplicate source files. Other teaching sources remain; the asterisk denotes the separate language rating target.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1495_bfs.cpp](1495_bfs.cpp) | G++ 13.2 x64 | bfs | O(N) | AC | 0.046 s | 14636 KB | 11287220 |
| [1495_bfs.go](1495_bfs.go) | Go 1.14 x64 | bfs | O(N) | AC | 0.093 s | 32440 KB | 11287221 |
| [1495_bfs.java](1495_bfs.java) \* | Java 1.8 | bfs | O(N) | AC | 0.156 s | 17324 KB | 11287225 |
| [1495_bfs.py](1495_bfs.py) | Python 3.12 x64 | bfs | O(N) | AC | 0.906 s | 62744 KB | 11287224 |
| [1495_bfs.rs](1495_bfs.rs) | Rust 1.75 x64 | bfs | O(N) | AC | 0.062 s | 26080 KB | 11287226 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1495_bfs_optimized.cpp](1495_bfs_optimized.cpp) | G++ 13.2 x64 | bfs | O(N) | AC | 0.015 s | 7004 KB | 11310407 |
| [1495_bfs_optimized.go](1495_bfs_optimized.go) | Go 1.14 x64 | bfs | O(N) | AC | 0.046 s | 8964 KB | 11310363 |
| [1495_bfs_optimized.py](1495_bfs_optimized.py) | PyPy 3.10 x64 | bfs | O(N) | AC | 0.14 s | 11808 KB | 11326708 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
