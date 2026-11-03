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

The optimized programs store only existing transitions in flat arrays:
each state has a head index; an edge stores its letter, destination and
next-edge index. A lookup scans at most 26 edges. A clone receives its
own copied edge list, because later redirections must not mutate the
original state. State/edge indices and lengths fit 32-bit integers for
`N ≤ 100000`; Python uses packed integer arrays and a bytearray for letters.

This removes dense 26-column rows and Python dictionary objects without
changing the suffix-automaton invariant. Time remains `O(N)` for the fixed
alphabet (with a larger lookup constant), and storage remains `O(N)` with
a much smaller constant. It is chiefly a memory optimization.

Measured memory reductions against the unchanged Accepted base: C++ 82.9%, Go 70.6%, Java 81.1%, Python 82.7%, Rust 81.0%. All five qualify by memory. Python is slower: 1.312 s versus 0.500 s, while memory falls from 56240 to 9736 KB. Go is also slower, 0.078 s versus 0.046 s. These are accepted space/time tradeoffs, not claims of universal acceleration. Ranking snapshot: 2 November 2026; starred rows remain below the target.

## Language notes

Python was compared with an independent quadratic longest-common-substring
DP on 5,760 pairs. The sparse graph was also checked on 100,000-character
strings over alphabets of sizes 1, 2 and 26. Each of the five actual
programs passed 13 repository test inputs through Docker before submission.
These local checks supplement their own Accepted receipts.

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
| [1517_suffix_structures_optimized.py](1517_suffix_structures_optimized.py) \* | Python 3.12 x64 | suffix_structures | O(N) | AC | 1.312 s | 9736 KB | 11308173 |
| [1517_suffix_structures_optimized.rs](1517_suffix_structures_optimized.rs) | Rust 1.75 x64 | suffix_structures | O(N) | AC | 0.062 s | 5408 KB | 11308179 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
