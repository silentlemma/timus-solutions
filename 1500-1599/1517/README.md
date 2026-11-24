# 1517. Longest shared substring

[Timus 1517](https://acm.timus.ru/problem.aspx?space=1&num=1517) · difficulty 240 · suffix_structures

Original problem by Ilya Grebnov, Nikita Rybak and Dmitry Kovalioff, from Timus Top Coders: Third Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two strings of uppercase Latin letters, each of length `N`, `1 ≤ N ≤ 100000`, are given. Output any longest string occurring contiguously in both. If no letter is shared, output an empty line. Time limit: 2 seconds. Memory limit: 64 MB.

## Input

The integer `N`, followed by the first and second strings on separate lines.

## Output

One longest common substring, or an empty line if its length is zero.

## Checking

Any longest common substring is accepted. The checker verifies that the output occurs in both strings and that its length equals the optimum; ties need not match the example.

## Examples

### Example 1

Input:

```
28
VOTEFORTHEGREATALBANIAFORYOU
CHOOSETHEGREATALBANIANFUTURE
```

Output:

```
THEGREATALBANIA
```

## Solution

Build a suffix automaton of the first string. A state groups substrings
with the same end positions and stores its maximum length, suffix link
and letter transitions. Extending the automaton creates a new state;
when a transition would jump to a state of excessive length, split that
class with a clone and redirect the affected transitions.

Scan the second string while keeping the longest suffix of the scanned
prefix that occurs in the first string. On a missing transition, follow
suffix links and shorten the current match until the transition exists
or the root is reached. Take that transition when possible. The largest
match length and its ending position identify the answer. Every shared
substring is a suffix of some scanned prefix, so the largest such match
is optimal. Following suffix links decreases the length, whereas reading
a letter increases it by at most one, giving a linear total scan.

There are `O(N)` states and transitions. For the fixed 26-letter alphabet,
construction and scanning take `O(N)` time and `O(N)` space. The simple
native sources use full transition rows; simple Python uses dictionaries.
All five readable implementations remain unchanged.

## Optimized solutions

`1517_suffix_structures_optimized.py`. Keep the suffix automaton, but allocate a dense row of 26 signed 32-bit transition indices for each of at most 2N+1 states. Lengths and suffix links are packed integer arrays. A clone copies its transition row before redirecting links. This removes linked-edge scans and Python dictionaries at the cost of reserving all 26 entries per state. Scan the second string with suffix-link fallback and return one longest common substring. For lengths N and M, time O(26N+M), state O(26N) plus the two input strings. The dictionary-based teaching source remains.

Exact-source PyPy 3.10 Accepted #11326700: 0.234 s / 25000 KB. Saved current-compiler comparison, 2026-11-20: time rank 1/32, memory rank 9/32. Both required metrics pass the strict top-ten or top-15% rule, with percentage cutoffs rounded up. The asterisk tracks Python's separate first-place target in both metrics.

The previously documented optimized run #11308173 (Python 3.12 x64) recorded 1.312 s / 9736 KB. The current PyPy 3.10 run has lower recorded time and higher memory. These are separate paired judge measurements; interpreter choice and judge variability are part of the comparison.

- `1517_suffix_structures_optimized.py`: 0.234 s / 25000 KB; retained teaching base `1517_suffix_structures.py` (Python 3.12 x64): 0.5 s / 56240 KB.

The optimized C++, Go, Java and Rust sources keep sparse transition arrays: a head per state and letter, destination and next-edge index per edge. A lookup scans at most 26 edges. Each clone copies its own edge list before redirections. Indices and lengths fit 32 bits for N<=100000. These four implementations retain O(N) work/storage for the fixed alphabet with smaller memory constants. Their previous Accepted measurements and 2 November 2026 comparison remain in the table; Go recorded 0.078 s versus its 0.046 s base, illustrating the time/space tradeoff.

Recorded memory reductions from the table bases: C++ 82.9%, Go 70.6%, Java 81.1%, Python 55.5%, Rust 81.0%.

## Language notes

The current Python program passed 58 local inputs on each of CPython 3.12 and PyPy 3.10 before its own Accepted. Its dense transition representation is described above; the table records the accepted PyPy run.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1517_suffix_structures.cpp](1517_suffix_structures.cpp) | G++ 13.2 x64 | suffix_structures | O(N) | AC | 0.093 s | 29044 KB | 11287349 |
| [1517_suffix_structures.go](1517_suffix_structures.go) | Go 1.14 x64 | suffix_structures | O(N) | AC | 0.046 s | 25012 KB | 11287350 |
| [1517_suffix_structures.java](1517_suffix_structures.java) | Java 1.8 | suffix_structures | O(N) | AC | 0.203 s | 35156 KB | 11287352 |
| [1517_suffix_structures.py](1517_suffix_structures.py) | Python 3.12 x64 | suffix_structures | O(N) | AC | 0.500 s | 56240 KB | 11287351 |
| [1517_suffix_structures.rs](1517_suffix_structures.rs) | Rust 1.75 x64 | suffix_structures | O(N) | AC | 0.062 s | 28496 KB | 11287353 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1517_suffix_structures_optimized.cpp](1517_suffix_structures_optimized.cpp) | G++ 13.2 x64 | suffix_structures | O(N) | AC | 0.062 s | 4968 KB | 11308174 |
| [1517_suffix_structures_optimized.go](1517_suffix_structures_optimized.go) | Go 1.14 x64 | suffix_structures | O(N) | AC | 0.078 s | 7356 KB | 11308176 |
| [1517_suffix_structures_optimized.java](1517_suffix_structures_optimized.java) | Java 1.8 | suffix_structures | O(N) | AC | 0.156 s | 6652 KB | 11308178 |
| [1517_suffix_structures_optimized.py](1517_suffix_structures_optimized.py) | PyPy 3.10 x64 | suffix_structures | O(26N+M) time; O(26N+M) space | AC | 0.234 s | 25000 KB | 11326700 |
| [1517_suffix_structures_optimized.rs](1517_suffix_structures_optimized.rs) | Rust 1.75 x64 | suffix_structures | O(N) | AC | 0.062 s | 5408 KB | 11308179 |
