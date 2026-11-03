# 1002. Spelling a number with the fewest words

[Timus 1002](https://acm.timus.ru/problem.aspx?space=1&num=1002) · difficulty 225 · dp, hashing, strings

Original problem from the Central European Olympiad in Informatics 1999.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Each lowercase Latin letter represents one digit according to the table below. Given a digit string of length at most 100 and a dictionary of at most 50000 words, each 1–50 letters long, concatenate dictionary words to obtain the string using as few words as possible. Words may be reused. There are multiple cases; total input is at most 300 KB. Preserve leading zeroes. Time limit: 2 seconds. Memory limit: 64 MB.

| Digit | Letters |
|---|---|
| 0 | o q z |
| 1 | i j |
| 2 | a b c |
| 3 | d e f |
| 4 | g h |
| 5 | k l |
| 6 | m n |
| 7 | p r s |
| 8 | t u v |
| 9 | w x y |

## Input

Each case has a line with the digit string, a line with the dictionary size, then one word per line. A line `-1` terminates input.

## Output

For each case, print one minimum-word sequence separated by single spaces, or exactly `No solution.` if none exists.

## Checking

Any shortest sequence is accepted: the checker verifies that the words are in
the dictionary, that they spell the number, and that no shorter sequence
exists.

## Examples

### Example 1

Input:

```
8733
3
use
e
tree
12
2
ab
cd
-1
```

Output:

```
tree
No solution.
```

### Example 2

Input:

```
22
4
ac
ba
b
c
-1
```

Output:

```
ac
```

## Solution

Let `best[i]` be the minimum words spelling the first `i` digits.
Initially only `best[0] = 0` is reachable. From each reachable position,
every dictionary spelling matching the next substring gives a transition
to the substring's end with cost one. Positions strictly increase,
so prefix order computes shortest paths in this DAG. Remembering the
chosen last word reconstructs a minimum sequence backwards. Equal-cost
choices are interchangeable; any optimum is accepted.

The readable versions map each dictionary spelling to one representative
word in a hash table. Multiple words with the same spelling need only
one representative. At each reachable position, look up substrings of
lengths 1 through `W = 50`; longer words cannot occur. With phone length
`P` and total dictionary length `T`, expected time is `O(T + P W²)` when
substring construction/hashing is counted; storage depends on dictionary
payload. These five Accepted hashing versions are retained unchanged.

## Optimized solutions

Build a trie of all substrings of the PHONE of length at most `W`,
before reading the dictionary. It has at most `1 + P W` nodes. Traverse
each dictionary word's digit spelling through that trie; if an edge is
missing, discard the word. Retain one representative at each reached
terminal node. An unusable word never allocates a trie node or a retained
dictionary entry. This matters when a large dictionary has little overlap
with a short phone.

During DP, walk the phone's digits from each reachable position, following
trie edges rather than allocating/hashing substrings. Every usable word
is present because its spelling is a phone substring; every retained
terminal corresponds to an actual dictionary word. Thus the DP edges and
minimum answer are unchanged. The selected word's length gives the
predecessor position during reconstruction.

With a fixed ten-digit alphabet, total time is `O(T + P W)` and working
storage is `O(P W + R)`, where `R` is retained representative-word storage,
plus input/output buffers. C++ provisions a bounded static pool and
clears the nodes used by the previous case; reset work is charged across
cases. Go and Rust stream words; Java reuses a token buffer but accumulates
output lines. Python uses a flat integer transition array. The trie has
different algorithm tags, `dp, strings`, rather than an `_optimized` suffix.

All five qualify by measured memory reduction against the corresponding
unchanged hashing version. Timing differences near one timer tick are
not treated as reliable evidence of a speedup.

Measured memory reductions: C++ 83.1%, Go 57.0%, Java 89.9%, Python 82.5%, Rust 76.7%. Every source has its own Accepted ID in the table.

## Language notes

The Python candidate was checked on 1802 cases against independent BFS
over positions that tries every whole dictionary word. The checker also
validates membership, spelling and minimum word count, allowing ties.
Cases cover spelling collisions, reuse, impossible strings, leading
zeroes, 50-character words, large irrelevant dictionaries and alternating
large/tiny cases. The concatenated fuzz stream intentionally exceeds the
normal total-file bound; it is an additional reset/semantics test, not a
claimed legal 300 KB input. Each of the five actual programs also passed
14 repository test inputs in Docker.

The following filtered rating snapshot is from 2 November 2026. Stars
mark a remaining ranking target despite a genuine admitted improvement.
An empty comparison sample provides no competitive ranking evidence.

| Language | Time place | Memory place | Other-author entries (time / memory) |
|---|---|---|---|
| C++ | 1 | 3 | 198 / 198 |
| Go | 1 | 1 | 4 / 4 |
| Java | 2 | 1 | 8 / 8 |
| Python | 1 | 1 | 49 / 49 |
| Rust | 4 | 1 | 3 / 3 |

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1002_dp_hashing.cpp](1002_dp_hashing.cpp) | G++ 13.2 x64 | dp, hashing | O(T + P W^2) expected | AC | 0.015 s | 2764 KB | 11277423 |
| [1002_dp_hashing.go](1002_dp_hashing.go) | Go 1.14 x64 | dp, hashing | O(T + P W^2) expected | AC | 0.031 s | 3016 KB | 11277424 |
| [1002_dp_hashing.java](1002_dp_hashing.java) | Java 1.8 | dp, hashing | O(T + P W^2) expected | AC | 0.109 s | 7032 KB | 11277426 |
| [1002_dp_hashing.py](1002_dp_hashing.py) | Python 3.12 x64 | dp, hashing | O(T + P W^2) expected | AC | 0.093 s | 5424 KB | 11277425 |
| [1002_dp_hashing.rs](1002_dp_hashing.rs) | Rust 1.75 x64 | dp, hashing | O(T + P W^2) expected | AC | 0.031 s | 2540 KB | 11277427 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1002_dp_strings.cpp](1002_dp_strings.cpp) | G++ 13.2 x64 | dp, strings | O(T + P W) | AC | 0.015 s | 468 KB | 11308088 |
| [1002_dp_strings.go](1002_dp_strings.go) | Go 1.14 x64 | dp, strings | O(T + P W) | AC | 0.031 s | 1296 KB | 11308089 |
| [1002_dp_strings.java](1002_dp_strings.java) \* | Java 1.8 | dp, strings | O(T + P W) | AC | 0.093 s | 712 KB | 11308092 |
| [1002_dp_strings.py](1002_dp_strings.py) | Python 3.12 x64 | dp, strings | O(T + P W) | AC | 0.078 s | 948 KB | 11308086 |
| [1002_dp_strings.rs](1002_dp_strings.rs) \* | Rust 1.75 x64 | dp, strings | O(T + P W) | AC | 0.031 s | 592 KB | 11308095 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
