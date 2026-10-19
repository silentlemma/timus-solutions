# 1959. Restore Symbols with Overlapping Window Modes

[Timus 1959](https://acm.timus.ru/problem.aspx?space=1&num=1959) · difficulty 1062 · two_pointers

Original problem from Ural FU contest. Kontur Cup. Petrozavodsk training camp. Winter 2013 | by Mikhail Rubinchik (prepared by Bulat Zaynullin).

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

For a text s of length n and pattern p of length m<n, sum their Hamming
distances over every length-m contiguous text substring. A Hamming distance
counts unequal positions. Some symbols in at most one of the two sequences
are unknown. Restore them to minimize this total, preserving all known
symbols. Both sequences may already be intact. Limits: 1 second, 64 MB.

## Input

First n, 1≤n≤100000, then n integers for s. Next m, 1≤m<n, then m integers
for p. These constraints imply n≥2. Every entry is in 0…100000; positive
numbers are symbol IDs and zero is an unknown. The two sequences never
both contain zeros.

## Output

The restored text on the first line and restored pattern on the second.
Every ID must be in 1…100000, with known entries unchanged. Any restoration
achieving the minimum total distance is accepted; the distance is not printed.

## Checking

A checker verifies that the known symbols are kept and that every
restored symbol is one of the most frequent opponents in its
comparisons; by the argument below any such choice is optimal, so ties
are free.

## Examples

```
5
1 2 3 1 2
3
1 2 0
```

```
1 2 3 1 2
1 2 1
```

## Solution

### Independent choices

Because only one side can contain unknowns, each comparison involving a
hole has a fixed symbol on the other side. Known/known comparisons are a
constant. A hole compared with t fixed symbols incurs t−frequency(v)
mismatches when filled with v. Choose any most frequent symbol among those
comparisons. Holes do not interact, so these independent minima give the
global minimum. Every comparison window is nonempty and contains positive
known IDs, hence an optimal legal replacement always exists.

Put g=n−m and use zero-based positions. A pattern hole j compares with
s[j…j+g], a window of width g+1. Sweep j rightward, removing the old left
symbol and adding the new right symbol.

A text hole i compares with pattern indices j for which i=j+offset and
0≤offset≤g, 0≤j<m. Its opponent window is
p[max(0,i−g)…min(m−1,i)]. Both endpoints move right. For each i, add p[i]
if i<m; remove p[i−g−1] if i>g; then answer the mode query if s[i]=0.
The window first grows, may slide or stay fixed, and finally shrinks.
The intact opponent sequence is never modified.

### Constant-time window modes

Keep frequency[v] for each positive symbol. Symbols of frequency f>0 form
an intrusive doubly linked list: previous[v], following[v], and head[f].
Zero is only a null-link sentinel; zero-frequency symbols belong to no list.
Also keep the largest nonempty frequency maximum.

Adding/removing a symbol detaches it from its old list, changes its frequency
by one, and inserts it at the head of its new positive-frequency list.
If its new frequency is larger than maximum, raise maximum. Otherwise
decrease maximum while its list is empty. A valid single update can lower
the maximum by at most one: the removed occurrence leaves the same symbol
in frequency f−1, unless f was one. Thus every update and mode query is O(1).
Return head[maximum]; its frequency is maximal, so it is an optimal fill.

For pattern holes, allocate heads through width g+1. For text holes, use
capacity m: adding the new right endpoint before removing the left can
briefly make the window one larger than its final sliding width.

O(n+m+σ) time and memory, where σ is the maximum input ID, σ≤100000.
There are O(n+m) endpoint updates; all arrays are direct-indexed.
Do not use the global mode instead of the relevant window, forget the
inclusive width g+1, include zeros in the counter, or alter known entries.
The objective sums every alignment, not just the best alignment. The
independence argument requires the promised one-sided damage.

The programs never compute the numeric objective. Individual counters fit
32-bit integers, while a separately computed total can exceed 2³¹−1:
there can be 2,500,050,000 compared position pairs. Verification uses
wide integers for that total.

## Language notes

C++, Go 1.14, Java 8 and Rust 1.75 use primitive arrays/vectors for the
frequency lists; Java avoids per-symbol objects. Rust uses only the standard
library. Python uses indexed lists with the same updates, and CPython fits
the resource margin. If neither sequence contains zeros, every version
returns the input without constructing the counters.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1959_two_pointers.cpp](1959_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(n+m+sigma) | AC | 0.046 s | 2300 KB |
| [1959_two_pointers.go](1959_two_pointers.go) | Go 1.14 x64 | two_pointers | O(n+m+sigma) | AC | 0.171 s | 7228 KB |
| [1959_two_pointers.java](1959_two_pointers.java) | Java 1.8 | two_pointers | O(n+m+sigma) | AC | 0.171 s | 10212 KB |
| [1959_two_pointers.py](1959_two_pointers.py) | Python 3.12 x64 | two_pointers | O(n+m+sigma) | AC | 0.453 s | 17424 KB |
| [1959_two_pointers.rs](1959_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(n+m+sigma) | AC | 0.046 s | 6792 KB |
