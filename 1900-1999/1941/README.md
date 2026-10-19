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

## Language notes

Signed deficits are necessary because a letter may occur in excess.
Python uses a packed signed-int array instead of 729000 boxed integers.
Go uses int32 deficits and byte fields; Java parses triplets directly
without allocating a String for every text letter. Rust stores input
once and iterates slices. No probabilistic fingerprint or map is needed.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1941_two_pointers.cpp](1941_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(U+m+n) | AC | 0.046 s | 2996 KB |
| [1941_two_pointers.go](1941_two_pointers.go) | Go 1.14 x64 | two_pointers | O(U+m+n) | AC | 0.062 s | 21096 KB |
| [1941_two_pointers.java](1941_two_pointers.java) | Java 1.8 | two_pointers | O(U+m+n) | AC | 0.187 s | 3336 KB |
| [1941_two_pointers.py](1941_two_pointers.py) | Python 3.12 x64 | two_pointers | O(U+m+n) | AC | 0.734 s | 33664 KB |
| [1941_two_pointers.rs](1941_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(U+m+n) | AC | 0.031 s | 6000 KB |
