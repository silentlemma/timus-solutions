# 2108. Closing a set of figures under wish rules

[Timus 2108](https://acm.timus.ru/problem.aspx?space=1&num=2108) · difficulty 461 · bitmask

Original problem by Kirill Borozdin, from the Ural FU Junior Championship 2016.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are n collectible figures. Each of m wishes says: once all figures
of a set A are owned, all figures of a set B are wanted too. Starting
from the figures already owned, find the smallest set that satisfies
every wish, that is, the set reached by granting wishes until nothing new
is wanted. The limits are 0.9 seconds and 64 MB.

## Input

n and m, 1 ≤ n ≤ 1000, 0 ≤ m ≤ 4000, then m lines with the sets A and B
as strings of n zeros and ones, and the owned set in the same format.

## Output

The final set in the same format.

## Examples

### Example 1

Input:

```
6 4
111000 101000
110000 111000
010000 100000
000010 000001
010100
```

Output:

```
111100
```

## Solution

A set that satisfies every wish and contains the owned figures has to
contain every figure that some chain of wishes leads to, and the set of
exactly those figures satisfies every wish. So repeat passes over the
wishes: a wish whose A is inside the owned set adds B. A pass that adds
nothing ends the process, and every other pass adds at least one figure,
so there are at most n + 1 passes.

The sets are bitsets of 64-bit words: "A inside the owned set" is
A AND NOT owned = 0, and adding B is an OR, both n / 64 word operations.
The total work is O(n · m · n / 64), about 6 · 10⁷ word operations.

In the example the owned figures 2 and 4 enable the third wish, which
adds 1; then the second wish adds 3, and the result is 111100.

## Optimized solutions

The new C++, Go and Rust versions transpose prerequisite sets into packed bitsets of rules per figure and keep a missing-prerequisite count per rule. Queue each newly acquired figure exactly once. Processing it decrements the rules containing it; a count reaching zero fires that rule once and queues its previously unowned consequences. Empty prerequisites fire after reading all input. This computes the least closure: only enabled rules add figures, and at termination every enabled rule has fired. No rule or figure is repeatedly rescanned in closure rounds. Including input, time is O(nm+n+m); packed storage is O(n⌈m/64⌉+m⌈n/64⌉+n+m). At the limits the two matrices hold 1016000 bytes, not millions of individual dependency edges. Go/C++ allocate bounded maximum arrays; Rust sizes vectors to input dimensions and uses bounded C-runtime I/O instead of retaining input text. All simple files remain; Java/Python reuse admitted bases.

The accepted G++ 13.2 x64 run takes 0.093 s versus 0.046 s for the base and uses 1 080 KB versus 1808 KB.

The accepted Go 1.14 x64 run takes 0.125 s versus 0.062 s for the base and uses 1 284 KB versus 18712 KB.

The accepted base implementations [2108_bitmask.java](2108_bitmask.java), [2108_bitmask.py](2108_bitmask.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

These notes describe the simple implementations.

The Python solution transposes the problem, because the passes are too
slow there when a chain of wishes is listed in reverse order. For every
figure it builds the set of wishes that need it as one big integer (a
column of the matrix of A strings). A segment tree over figures keeps the
union of these sets over the figures still missing, which is exactly the
set of wishes not yet enabled. Every round fires all newly enabled wishes
and clears the tree leaves of the newly owned figures. Each wish fires
at most once and each figure's leaf is cleared at most once.

Let w be the number of bits per Python integer digit, N = ceil(n / w),
M = ceil(m / w), and L = 1 + ceil(log2 n). For m > 0, the time is
O(nm + (nL + m)M + nN): reading and transposing cost O(nm), tree updates
and readiness checks cost O(nLM), enumerating enabled wishes costs
O(mM), and enumerating new figures costs O(nN). OR-ing the result sets
costs O(mN), already covered by O(nm). For m = 0, the time is O(n).

Pitfall (test 15, empty results): a wish that adds nothing still has to
be processed. Iterating set bits is not constant time per bit in Python:
`mask & -mask` and `mask ^= low` scan integer digits. With n = 1 and
m = 4000 wishes A = B = 0, the answer stays 0, but enumerating the
enabled wishes takes Θ(m² / w) digit operations. The repeated-pass
O(n^2 m / 64) bound therefore does not describe the Python solution.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2108_bitmask.cpp](2108_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(n^2 m / 64) | AC | 0.046 s | 1808 KB | 11294887 |
| [2108_bitmask.go](2108_bitmask.go) | Go 1.14 x64 | bitmask | O(n^2 m / 64) | AC | 0.062 s | 18712 KB | 11294892 |
| [2108_bitmask.java](2108_bitmask.java) | Java 1.8 | bitmask | O(n^2 m / 64) | AC | 0.234 s | 1792 KB | 11294899 |
| [2108_bitmask.py](2108_bitmask.py) \* | Python 3.12 x64 | bitmask | O(nm + (nL + m)M + nN) | AC | 0.171 s | 17336 KB | 11294894 |
| [2108_bitmask.rs](2108_bitmask.rs) | Rust 1.75 x64 | bitmask | O(n^2 m / 64) | AC | 0.062 s | 9312 KB | 11294901 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2108_graphs_bitmask.cpp](2108_graphs_bitmask.cpp) \* | G++ 13.2 x64 | graphs, bitmask | O(nm + n + m) | AC | 0.093 s | 1080 KB | 11315229 |
| [2108_graphs_bitmask.go](2108_graphs_bitmask.go) \* | Go 1.14 x64 | graphs, bitmask | O(nm + n + m) | AC | 0.125 s | 1284 KB | 11315237 |
| [2108_graphs_bitmask.rs](2108_graphs_bitmask.rs) \* | Rust 1.75 x64 | graphs, bitmask | O(nm + n + m) | AC | 0.046 s | 1072 KB | 11315242 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
