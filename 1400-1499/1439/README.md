# 1439. Battle with You-Know-Who

[Timus 1439](https://acm.timus.ru/problem.aspx?space=1&num=1439) · difficulty 428 · binary_search

Original problem by Alexander Klepinin and Stanislav Vasiliev, from the Tenth Ural Collegiate Team Programming Championship, March 24–25, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The rooms of the Ministry of Magic are numbered 1, 2, …, N
(1 ≤ N ≤ 10⁹), and the numbering always stays without gaps: when a room
is destroyed, every room with a larger number moves one number down.
There are M ≤ 10⁵ events in order, each "D x" (the room that now has
number x is destroyed) or "L x" (Harry looks at the door that now shows
number x). At most 10⁴ rooms are destroyed. For every "L" event print
the number that room had at the very beginning.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and M, then the M events.

## Output

The original numbers, one per line.

## Examples

### Example 1

Input:

```
20 7
L 5
D 5
L 4
L 5
D 5
L 4
L 5
```

Output:

```
5
4
6
4
7
```

## Solution

Keep the original numbers of the destroyed rooms in a sorted array g.
The room now numbered x has original number x + k, where k counts the
destroyed rooms below it. Walking up the array, room g[j] lies below
exactly when g[j] ≤ x + j, that is g[j] − j ≤ x; and g[j] − j never
decreases because the numbers in g are distinct, so the rooms below
form a prefix and its length k comes from a binary search.

For "L" print x + k. For "D" the new original number x + k fits right
at position k of the array: everything before it is smaller and
everything after it is larger, so an insertion keeps the array sorted.
`O(M log D + D²)` for D destroyed rooms, where the insertions shift at
most 10⁴ numbers each.

Pitfalls:

- the same door number destroyed again and again hides a new room each
  time (tests 03, 07, gen3);
- numbers go up to a billion, beyond any per-room array (tests 05,
  gen1).

## Optimized solutions

The C++ revision retains binary search in the sorted destroyed-label vector, including entry shifts on insertion. Fixed 16 KB input/output buffers replace formatted calls. The bound remains O(M log D + D²), with O(D) storage; this is not an order-statistics-tree algorithm.

Exact-source Accepted (G++ 13.2 x64, #11326643: 0.031 s / 188 KB); teaching base `1439_binary_search.cpp`: 0.156 s / 424 KB. The previous optimized measurement was 0.156 s / 216 KB. In the saved 20 November 2026 comparison, time place is 1/80, memory place 1/80; below 1 MiB the policy evaluates the time rank only.

These implementations retain the sorted destroyed-room array and its prefix binary search; insertion still shifts entries, so time remains O(M log D + D²). The change is compact storage and streaming I/O. C++ stores 32-bit original labels, sufficient because N ≤ 10⁹, and reserves the maximum 10000 destroyed entries. Go and Rust use bounded input/output buffers; Rust also uses 32-bit entries and a C-runtime entry point. Python discards each input line after processing and stores output bytes instead of retaining all input tokens and output integers. It needs O(D + output bytes) storage; the other new versions need O(D) storage plus fixed buffers. The existing straightforward implementations remain available.

The accepted Python 3.12 x64 run takes 0.437 s versus 0.421 s for the base and uses 2 376 KB versus 21004 KB.

The accepted Rust 1.75 x64 run takes 0.046 s versus 0.031 s for the base and uses 96 KB versus 4664 KB.

The accepted base implementations [1439_binary_search.java](1439_binary_search.java) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1439_binary_search.cpp](1439_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(M log D + D^2) | AC | 0.156 s | 424 KB | 11286248 |
| [1439_binary_search.go](1439_binary_search.go) | Go 1.14 x64 | binary_search | O(M log D + D^2) | AC | 0.171 s | 5708 KB | 11286251 |
| [1439_binary_search.java](1439_binary_search.java) \* | Java 1.8 | binary_search | O(M log D + D^2) | AC | 0.171 s | 10132 KB | 11286253 |
| [1439_binary_search.py](1439_binary_search.py) | Python 3.12 x64 | binary_search | O(M log D + D^2) | AC | 0.421 s | 21004 KB | 11286252 |
| [1439_binary_search.rs](1439_binary_search.rs) | Rust 1.75 x64 | binary_search | O(M log D + D^2) | AC | 0.031 s | 4664 KB | 11286256 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1439_binary_search_optimized.cpp](1439_binary_search_optimized.cpp) | G++ 13.2 x64 | binary_search | O(M log D + D²) | AC | 0.031 s | 188 KB | 11326643 |
| [1439_binary_search_optimized.go](1439_binary_search_optimized.go) \* | Go 1.14 x64 | binary_search | O(M log D + D²) | AC | 0.031 s | 404 KB | 11314850 |
| [1439_binary_search_optimized.py](1439_binary_search_optimized.py) \* | Python 3.12 x64 | binary_search | O(M log D + D²) | AC | 0.437 s | 2376 KB | 11314854 |
| [1439_binary_search_optimized.rs](1439_binary_search_optimized.rs) \* | Rust 1.75 x64 | binary_search | O(M log D + D²) | AC | 0.046 s | 96 KB | 11314853 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
