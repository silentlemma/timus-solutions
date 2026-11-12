# 1941. Counting Windows with a Given Multiset

[Timus 1941](https://acm.timus.ru/problem.aspx?space=1&num=1941) · difficulty 432 · two_pointers

Original problem from Open Ural FU Personal Contest 2012 | by Andrey Demidov (prepared by Alex Samsonov).

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An alphabet letter is an ordered triplet of ASCII symbols, each with code
33 through 122 inclusive. Thus the alphabet has 90³=729000 letters.
Given a nonempty pattern of m≤8000 letters and nonempty text of n≤500000
letters, count contiguous text windows that are permutations of the pattern.
Repetitions matter, order within a triplet matters, and windows may overlap.
Limits: 1 second, 64 MB.

## Input

The first line is the pattern, the second the text. Each letter is exactly
three adjacent symbols; whitespace separates letters. The line boundary
determines the pattern length. Neither m nor n is supplied explicitly.

## Output

One integer, the number of matching windows. If m>n, output 0.

## Checking

Compare one integer token; whitespace is insignificant.

## Examples

```
aaa bbb ccc
aaa aaa bbb ccc aaa zzz aaa bbb ccc
```

```
3
```

## Solution

Encode a triplet (a,b,c) by ((a−33)·90+(b−33))·90+(c−33).
Each digit is in 0..89, so this is a bijection to 0..728999, not a hash.
Create a deficit table D of 729000 signed integers, initially the pattern
frequencies. Maintain a ring of m encoded text letters and a variable
missing, initially m.

For each incoming letter, first remove the oldest if the ring is full.
Removing x increases missing if D[x]≥0 before removal, then increments
D[x]. Insert the new y: if D[y]>0, decrement missing; then decrement D[y].
Replace the ring slot and advance it modulo m. Count the window when
missing=0. No valid answer is lost before the first full window, since
fewer than m inserted letters cannot fill m required occurrences.

The invariant is D[x]=pattern_count[x]−window_count[x] and
missing=Σ max(D[x],0). Removing x creates a missing copy precisely when
D[x]≥0; inserting y fills one precisely when D[y]>0. Thus both updates
preserve the invariant. In a full window the two total counts are equal,
so missing=0 implies all deficits are zero; conversely equal multisets
give zero missing. Each length-m window is visited exactly once.

For alphabet size U=729000, time O(U+m+n). The counting core uses O(U+m)
space. C++ and Java stream the text; Python, Go and Rust retain input,
giving O(U+m+n) total space in those complete programs. The answer is
at most max(0, n−m+1)≤500000, fitting a signed 32-bit integer.

Letters are triplets, not individual ASCII characters. Anagrams of the
three characters inside one letter are different letters. A set cannot
replace occurrence counts. Removal uses ≥0, insertion uses >0, both
before modifying the deficit. Include overlaps and the final window;
the fixed ring never requires an O(m) shift. Do not scan the entire
alphabet to compare each window. When m>n there are no windows (test 03),
so the upper bound must be clamped to zero.

## Optimized solutions

The new Go, Python and Rust sources keep the exact base-90 triplet encoding and missing-occurrence invariant. Since both pattern and current-window frequencies lie in 0..m and m≤8000, every deficit fits signed 16 bits, halving the 729000-entry table to 1458000 bytes. The ring stores exact triplet codes in 32 bits. Go and Rust stream triplets through bounded buffers, with O(U+m) total storage. Python retains the text bytes but parses triplets directly, avoiding a list of up to 500000 bytes objects; its total space remains O(U+m+n), with much smaller constants. Removal tests ≥0 and insertion >0 before updating the deficit. The first newline still separates the pattern from the text, including CRLF input. All simple sources remain; C++ and Java reuse admitted bases in the fast set.

The accepted Python 3.12 x64 run takes 0.89 s versus 0.734 s for the base and uses 8 604 KB versus 33664 KB.

The accepted base implementations [1941_two_pointers.cpp](1941_two_pointers.cpp), [1941_two_pointers.java](1941_two_pointers.java) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

These notes describe the simple implementations.

Signed deficits are necessary because a letter may occur in excess.
Python uses a packed signed-int array instead of 729000 boxed integers.
Go uses int32 deficits and byte fields; Java parses triplets directly
without allocating a String for every text letter. Rust stores input
once and iterates slices. No probabilistic fingerprint or map is needed.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1941_two_pointers.cpp](1941_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(U+m+n) | AC | 0.046 s | 2996 KB | 11291874 |
| [1941_two_pointers.go](1941_two_pointers.go) | Go 1.14 x64 | two_pointers | O(U+m+n) | AC | 0.062 s | 21096 KB | 11291875 |
| [1941_two_pointers.java](1941_two_pointers.java) \* | Java 1.8 | two_pointers | O(U+m+n) | AC | 0.187 s | 3336 KB | 11291879 |
| [1941_two_pointers.py](1941_two_pointers.py) | Python 3.12 x64 | two_pointers | O(U+m+n) | AC | 0.734 s | 33664 KB | 11291878 |
| [1941_two_pointers.rs](1941_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(U+m+n) | AC | 0.031 s | 6000 KB | 11291881 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1941_two_pointers_optimized.go](1941_two_pointers_optimized.go) \* | Go 1.14 x64 | two_pointers | O(U+m+n) | AC | 0.031 s | 1864 KB | 11315003 |
| [1941_two_pointers_optimized.py](1941_two_pointers_optimized.py) \* | Python 3.12 x64 | two_pointers | O(U+m+n) | AC | 0.89 s | 8604 KB | 11314998 |
| [1941_two_pointers_optimized.rs](1941_two_pointers_optimized.rs) \* | Rust 1.75 x64 | two_pointers | O(U+m+n) | AC | 0.015 s | 1364 KB | 11315010 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
