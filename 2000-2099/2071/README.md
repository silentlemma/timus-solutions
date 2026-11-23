# 2071. Order the cocktails for the fewest pourings

[Timus 2071](https://acm.timus.ru/problem.aspx?space=1&num=2071) · difficulty 641 · bitmask, dp

Original problem by Mikhail Rubinchik, prepared by Nickolai Permyakov and Alexey Danilyuk, from the Ural Regional Team Programming Contest 2015.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n guests each order a cocktail: a non-empty set of the juices A, B and P.
The glasses are put in a row in some order, and one pouring fills a
segment of consecutive glasses with one juice (apple first, then banana,
then pineapple, so the order of pourings is never a problem). Each glass
must get exactly the juices of its cocktail. Arrange the glasses to need
the fewest pourings. The limits are 1 second and 64 MB.

## Input

n, 1 ≤ n ≤ 10⁵, then n lines, each one of A, B, P, AB, AP, BP, ABP.

## Output

The smallest number of pourings, then the numbers of the glasses in the
row order. Any optimal arrangement is accepted.

## Checking

A checker compares the number of pourings and recounts the pourings that
the printed arrangement needs.

## Examples

### Example 1

Input:

```
3
A
B
ABP
```

Output:

```
3
1 3 2
```

## Solution

For a fixed row, each juice needs one pouring per maximal run of glasses
that contain it, so the cost is the number of places where a juice
appears in a glass but not in the glass before it (the first glass
counts all its juices). Removing a glass cannot create a new run. Inserting it beside an
identical glass only extends runs that are already there. We can therefore
group each cocktail type together and order at most seven groups.

These are ordered by a DP over subsets: best[S][last] is the fewest
pourings for a row made of the cocktails in S that ends with last.
Appending cocktail k costs the number of juices of k missing in last,
that is popcount(k & ~last). The answer is the minimum over last for the
full set, and the stored predecessors give the order. With seven
cocktails this is 2⁷ · 7 · 7 steps, so the work is O(n) for reading and
printing.

In the example the order B, ABP, A needs three pourings: one run for
each juice.

## Optimized solutions

The C++ version enumerates the orders of the at most seven cocktail types. For each type, a linked list in a single array stores the glass indices. This takes O(n) time for input and output plus O(k! · k) for k types, and O(n) memory. Submission 11317118 took 0.046 s and 560 KB, compared with 0.078 s and 420 KB for the base.

Java parses the input byte by byte, stores DP costs and predecessors in byte arrays, and links the glass indices through one integer array. Submission 11317279 took 0.125 s and used 832 KB, versus 0.14 s and 8836 KB for the base.

Go reads one token at a time and uses a single array of 32-bit links for glass indices. The subset DP stores costs and predecessors in byte arrays. Submission 11317277 took 0.031 s and used 1288 KB, versus 0.031 s and 8040 KB for the base.

Python stores costs and predecessors in byte arrays, reads orders line by line, and writes packed glass indices in batches. Submission 11317276 took 0.109 s and used 1408 KB, versus 0.171 s and 16872 KB for the base.

Rust stores each dynamic-programming cost and predecessor in a byte. Glass indices of each type are linked through a single 32-bit array. Submission 11317274 took 0.046 s and used 584 KB, versus 0.046 s and 7676 KB for the base.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11318364 · Java 1.8 №11318369 · Rust 1.75 x64 №11318371.

The buffered C++ subset DP reads and writes in blocks and links glass indices by cocktail type in one array. G++ 13.2 x64, submission 11321988. Time 0.078 → 0.015 s, memory 420 → 516 KB.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`2071_bitmask_dp_implementation_optimized.py`. Cache all small-mask population counts and use list-backed DP costs and predecessors to reduce conversion/indexing overhead. The mask transitions and reconstructed answer are unchanged; lists trade memory for cheaper access. The standalone program flushes both output streams before os._exit(0), avoiding interpreter teardown after the complete answer has been written. This changes process shutdown, not the mathematical algorithm; the simple version remains available.

Accepted #11328669 (Python 3.12 x64): **0.093 s / 1428 KB**. Archived comparison: `2071_bitmask_dp_optimized.py` (Python 3.12 x64) — 0.109 s / 1408 KB (#11317276).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [2071_bitmask_dp.cpp](2071_bitmask_dp.cpp) | G++ 13.2 x64 | bitmask, dp | O(n) | AC | 0.078 s | 420 KB | 11318364 |
| [2071_bitmask_dp.go](2071_bitmask_dp.go) | Go 1.14 x64 | bitmask, dp | O(n) | AC | 0.031 s | 8040 KB | 11322036 |
| [2071_bitmask_dp.java](2071_bitmask_dp.java) | Java 1.8 | bitmask, dp | O(n) | AC | 0.14 s | 8836 KB | 11318369 |
| [2071_bitmask_dp.py](2071_bitmask_dp.py) | Python 3.12 x64 | bitmask, dp | O(n) | AC | 0.171 s | 16872 KB | 11322037 |
| [2071_bitmask_dp.rs](2071_bitmask_dp.rs) | Rust 1.75 x64 | bitmask, dp | O(n) | AC | 0.046 s | 7676 KB | 11318371 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [2071_bruteforce.cpp](2071_bruteforce.cpp) \* | G++ 13.2 x64 | bruteforce | O(n) | AC | 0.046 s | 560 KB | 11317118 |
| [2071_bitmask_dp_optimized.go](2071_bitmask_dp_optimized.go) | Go 1.14 x64 | bitmask, dp | O(n) | AC | 0.031 s | 1288 KB | 11317277 |
| [2071_bitmask_dp_optimized.java](2071_bitmask_dp_optimized.java) | Java 1.8 | bitmask, dp | O(n) | AC | 0.125 s | 832 KB | 11317279 |
| [2071_bitmask_dp_optimized.py](2071_bitmask_dp_optimized.py) \* | Python 3.12 x64 | bitmask, dp | O(n) | AC | 0.109 s | 1408 KB | 11317276 |
| [2071_bitmask_dp_optimized.rs](2071_bitmask_dp_optimized.rs) | Rust 1.75 x64 | bitmask, dp | O(n) | AC | 0.046 s | 584 KB | 11317274 |
| [2071_bitmask_dp_optimized.cpp](2071_bitmask_dp_optimized.cpp) | G++ 13.2 x64 | bitmask, dp | O(n) | AC | 0.015 s | 516 KB | 11321988 |
| [2071_bitmask_dp_implementation_optimized.py](2071_bitmask_dp_implementation_optimized.py) | Python 3.12 x64 | bitmask, dp, implementation | O(n) | AC | 0.093 s | 1428 KB | 11328669 |

\* Accepted; the rating target under [RATING_CRITERIA.md](../../RATING_CRITERIA.md) is not yet met. This version may be optimized further.
