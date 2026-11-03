# 2115. Sort a line with at most one swap

[Timus 2115](https://acm.timus.ru/problem.aspx?space=1&num=2115) · difficulty 228 · sorting

Original problem by Ivan Smirnov, from the University Academic School Olympiad in Informatics 2019.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given a sequence of `1≤n≤100000` heights `0≤a[i]≤10⁹`, determine
whether it is already nondecreasing or nonincreasing. Otherwise, find one
swap of two distinct positions that makes either order, or prove that
one swap is insufficient. Equal heights are allowed. Time limit: 1 second.
Memory limit: 256 MB.

## Input

The first line contains n. The second line contains the n heights in
their current order.

## Output

If already monotone in either direction, print `Nothing to do here`.
Otherwise print `Yes` and, on the next line, two distinct 1-based positions
whose swap makes either order. Any valid swap is allowed. If none exists,
print `No hope`.

## Checking

Check the required verdict, or apply the returned distinct 1-based
swap and verify either monotone order; different valid swaps are allowed.
Each of the five selected actual target programs passed 15 repository
inputs and 100 additional inputs. All 500 extra outputs and exit codes
were re-read against an independent sorted-target checker, without the
inversion-boundary rule. The exact selected Python program additionally
ran on 10876 host inputs: all 9840 arrays of lengths 1..8 over
`{0,1,10⁹}`, 1000 random inputs, duplicate-boundary cases and size-99999/100000
constructions, including long single lines, multiline tokens and EOF.
These host executions are not attributed to the native programs. All five
fast files and all three formatting revisions have their own exact-byte Accepted.

## Examples

### Example 1

Input:

```
3
150 160 170
```

Output:

```
Nothing to do here
```

### Example 2

Input:

```
4
140 160 150 170
```

Output:

```
Yes
2 3
```

## Solution

The simple versions sort a copy to obtain the nondecreasing target;
its reverse is the nonincreasing target. If the input equals either,
it already needs no change. Otherwise, for each target collect mismatching
positions. A swap changes only two positions, so there must be exactly
two mismatches i,j and their values must cross-match the target:
`a[i]=target[j]` and `a[j]=target[i]`. These conditions are also sufficient,
because the other positions already agree. Trying both targets is complete.
Time is `O(n log n)`, with `O(n)` arrays and any retained input storage.

The five sorting algorithms remain available. Go and Python source bytes
are unchanged; C++, Java and Rust receive only the exact repository
formatter output, each with its own new Accepted. Original pre-format
bytes are retained in the local publication backups. Every displayed
metric belongs to the actual source bytes.

## Optimized solutions

The `two_pointers` files remove sorting and target copies. Consider
nondecreasing order first. Find the first inversion `a[p]>a[p+1]`, then
move p left across its equal-value run to get l. Find the last inversion
`a[q-1]>a[q]`, then move q right across its equal-value run to get r.
Swap l,r and validate the complete order. If this direction fails, restore
the input and do the same for nonincreasing order by comparing
`direction*a[i]`, with direction −1. Values stay in `[-10⁹,10⁹]`, within
signed 32-bit range. An initially monotone input returns the required
no-change phrase before considering a swap.

Why are these endpoints necessary? If swapping i<j fixes an increasing
order, the original values there are H>L. Every unchanged middle value
lies between L and H. The first inversion is at the right end of the
H-run starting at i; that run cannot extend before i, since the preceding
unchanged value would then exceed the final L. Thus extending left from
the first inversion recovers i. Symmetrically, the last inversion is at
the left end of the L-run ending at j; it cannot extend after j because
the final H would then exceed its successor. Extending right recovers j.
Therefore any possible swap must be the one tested. Full validation
proves sufficiency; failure in both directions proves impossibility.
Equal-run expansion is essential, for example for `1,2,2,1`.

There are only a constant number of full scans: `O(n)` time and `O(1)`
search state beyond the stored sequence. The sequence uses `O(n)` cells;
Go and Rust also retain the full input, and Python's line splitting can
temporarily retain a whole long line of tokens. Total input storage must
be counted, not called constant. C++ uses buffered byte parsing and one
32-bit vector; Java uses one int array; Python uses `array('i')` instead
of boxed integer lists. No sorted or reversed target is built.

Against the current same-language Accepted sorting bases, C++ improves
time 0.109→0.015 s (86.2%) and memory 2532→520 KB (79.5%). Go improves
time 0.140→0.046 s (67.1%); its 5696→4052 KB memory reduction is only
28.9%, so admission is by time. Java memory falls 3644→848 KB (76.7%).
Rust memory falls 3504→2140 KB (38.9%); 0.062→0.046 s is one timing
tick and is not used as speed evidence. Python memory falls 15740→8564 KB
(45.6%), but time increases 0.140→0.203 s (45.0% worse). Python qualifies
by memory, not speed, and keeps its below-target star.

## Language notes

This is a distinct linear algorithm, so the files are named
`two_pointers` alongside the simple `sorting` versions. The stronger
Accepted C++ and Python revisions from batch009 are selected; earlier
batch002 variants with the same proposed filenames remain only in local
snapshots and reports. No duplicate public source is created.

C++, Java, Go and Rust meet the current filtered rating profile; Go and
Rust have no eligible competing authors, which gives formal coverage
rather than proof of superiority. CPython 3.12 is first by memory but
17th by time in this snapshot and carries a star. Native comparisons use
the newly Accepted formatted sorting bases where applicable; old metrics
are not attached to changed bytes. The limits and algorithm support the
entire legal domain, including n=1, all equal values, zero and 10⁹.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2115_sorting.cpp](2115_sorting.cpp) | G++ 13.2 x64 | sorting | O(n log n) | AC | 0.109 s | 2532 KB | 11308132 |
| [2115_sorting.go](2115_sorting.go) | Go 1.14 x64 | sorting | O(n log n) | AC | 0.140 s | 5696 KB | 11294785 |
| [2115_sorting.java](2115_sorting.java) | Java 1.8 | sorting | O(n log n) | AC | 0.140 s | 3644 KB | 11308139 |
| [2115_sorting.py](2115_sorting.py) | Python 3.12 x64 | sorting | O(n log n) | AC | 0.140 s | 15740 KB | 11294788 |
| [2115_sorting.rs](2115_sorting.rs) | Rust 1.75 x64 | sorting | O(n log n) | AC | 0.062 s | 3504 KB | 11308149 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2115_two_pointers.cpp](2115_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(n) | AC | 0.015 s | 520 KB | 11308152 |
| [2115_two_pointers.go](2115_two_pointers.go) | Go 1.14 x64 | two_pointers | O(n) | AC | 0.046 s | 4052 KB | 11307992 |
| [2115_two_pointers.java](2115_two_pointers.java) | Java 1.8 | two_pointers | O(n) | AC | 0.125 s | 848 KB | 11307994 |
| [2115_two_pointers.py](2115_two_pointers.py) \* | Python 3.12 x64 | two_pointers | O(n) | AC | 0.203 s | 8564 KB | 11308151 |
| [2115_two_pointers.rs](2115_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(n) | AC | 0.046 s | 2140 KB | 11307999 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
