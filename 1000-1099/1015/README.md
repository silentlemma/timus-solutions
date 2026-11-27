# 1015. Grouping dice that are rotations of each other

[Timus 1015](https://acm.timus.ru/problem.aspx?space=1&num=1015) · difficulty 458 · hashing, implementation

Original problem from the Ural State University Internal Contest '99 #2.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `N` dice (`1 ≤ N ≤ 100 000`), numbered from 1 in the input order.
A die is given by the numbers on its left, right, top, front, bottom and back
faces, in this order — a permutation of `1..6`. Two dice are of the same kind
if some rotation of one gives the other (a mirror image is not a rotation).
Split the dice into kinds.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

`N`, then `N` lines of six numbers: left, right, top, front, bottom, back.

## Output

The number `Q` of kinds, then `Q` lines, one per kind: the numbers of its
dice in increasing order. The lines are ordered by their first number, so
the first line starts with 1.

## Checking

The output is compared line by line; within a line, token by token.

## Examples

### Example 1

Input:

```
4
1 6 2 3 5 4
2 5 6 3 1 4
1 6 2 4 5 3
3 4 1 2 6 5
```

Output:

```
2
1 2 4
3
```

### Example 2

Input:

```
1
4 3 1 6 2 5
```

Output:

```
1
1
```

## Solution

**The 24 rotations.** Write a rotation as a permutation of the six
positions. Two quarter turns generate all of them: around the vertical axis
(left ← front ← right ← back ← left, top and bottom stay) and around the
left-right axis (top ← back ← bottom ← front ← top). Starting from the
identity and applying the two turns until nothing new appears gives exactly
24 position permutations. Only rotations are produced, never reflections, so
a die and its mirror image stay apart.

**A key for every die.** Apply all 24 rotations to a die, read each result
as a 6-digit number (base 7 is enough) and take the smallest: dice of the
same kind get the same key, dice of different kinds different keys. There
are only `720 / 24 = 30` kinds.

**Grouping.** Go through the dice in order; a hash map from key to group
creates a new group the first time a key appears and appends the die
otherwise. Groups are thus created in the order of their smallest die, and
each group's list is increasing — exactly the required output.

`O(24 · 6 · N)` time. Alternatively, precompute the key of each of the 720
possible dice once and look it up, as the Python version does.

Base C++, Go, Python and Rust retain `O(N)` group indices; Java stores
them as group text. Retaining complete input or output adds `O(I + O)`
bytes, where `I` and `O` are their text lengths. Rotation and permutation
tables have fixed sizes, independent of `N`. Optimized C++ reserves
`C = 100000` membership bytes even for a smaller input, plus a 720-byte
class table and fixed I/O buffers (`O(C + 720)` array storage). Optimized
Python stores `O(N)` compact indices and writes bounded output chunks.

Pitfalls:

- reflections: the six faces can be permuted in 720 ways but only 24 of them
  are rotations — a key built from the multiset of opposite pairs alone
  merges mirror images;
- up to `10^5` die indices in the output: build it in a buffer.

## Optimized solutions

The new C++ version generates the same 24 proper rotations once, then assigns a rotation class to every one of the 720 face permutations. The inversion-based permutation rank indexes a 720-byte table, so every input die needs one rank calculation and lookup instead of testing all 24 rotations. Group numbers are assigned on first appearance. Store just that one-byte group per die, then scan the byte array once per group (at most 30) to print increasing indices in first-appearance group order. This trades extra linear scans for avoiding index vectors and a complete output string. Both versions are linear in N; the change reduces constants/storage, with all classes computed at runtime. All five ordinary files remain; the other four families reuse admitted bases.

The cached audit verifies the Go and Rust bases by exact-compiler
small-cohort comparisons, and Java by ordinary ranking. Rust uses 856 KB,
so only time is compared. The Python teaching base does not pass its
small-cohort memory limit; `1015_hashing_optimized.py` supplies qualifying
coverage instead. C++ uses its optimized lookup version. All follow the
shared [rating criteria](../../RATING_CRITERIA.md), and meaningful teaching
versions remain without identical duplicate files.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1015_hashing_optimized.py`. Encode the six face labels in an integer with three bits per face. Generate all 24 rotations at runtime to canonicalize each permutation, then group streamed dice with compact index arrays. No offline result table is embedded. The standalone program flushes both output streams before os._exit(0), avoiding interpreter teardown after the complete answer has been written. This changes process shutdown, not the mathematical algorithm; the simple version remains available.

Accepted #11328767 (Python 3.12 x64): **0.093 s / 1060 KB**. Archived comparison: `1015_hashing.py` (Python 3.12 x64) — 0.093 s / 2748 KB (#11278138).

The current `1015_hashing_optimized.py` revision names the face-bit width and
whitespace boundary explicitly. Substituting the named constants recovers the
previous executable AST.

## Language notes

Ordinary C++, Go, Java and Rust test 24 rotations per die. Ordinary Python already precomputes 720 keys. The new C++ lookup also precomputes every permutation, then stores one byte per die and streams output in group scans.

The source revisions discussed above have now received their own Accepted results. The solution tables list the final source-matched submission IDs and paired time/memory measurements; earlier observations describe previous revisions. All meaningful simple implementations remain available.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1015_hashing.cpp](1015_hashing.cpp) | G++ 13.2 x64 | hashing | O(24 · 6 · N) | AC | 0.031 s | 356 KB | 11278124 |
| [1015_hashing.go](1015_hashing.go) | Go 1.14 x64 | hashing | O(24 · 6 · N) | AC | 0.001 s | 1280 KB | 11278132 |
| [1015_hashing.java](1015_hashing.java) | Java 1.8 | hashing | O(24 · 6 · N) | AC | 0.093 s | 1524 KB | 11278141 |
| [1015_hashing.py](1015_hashing.py) | Python 3.12 x64 | hashing | O(N) after a 720-entry table | AC | 0.093 s | 2748 KB | 11278138 |
| [1015_hashing.rs](1015_hashing.rs) | Rust 1.75 x64 | hashing | O(24 · 6 · N) | AC | 0.015 s | 856 KB | 11278146 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1015_hashing_optimized.cpp](1015_hashing_optimized.cpp) | G++ 13.2 x64 | hashing | O(720 + 30N) | AC | 0.015 s | 104 KB | 11315195 |
| [1015_hashing_optimized.py](1015_hashing_optimized.py) | Python 3.12 x64 | hashing | O(N) after a 720-entry table | AC | 0.125 s | 1012 KB | 11331083 |
