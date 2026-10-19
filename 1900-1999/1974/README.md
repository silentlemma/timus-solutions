# 1974. Maximum Aligned Matches Between Note Sequences

[Timus 1974](https://acm.timus.ru/problem.aspx?space=1&num=1974) · difficulty 1157 · bitmask, bruteforce

Original problem by Denis Dublennykh, from the Ural Sport Programming Championship 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given one source melody and m target melodies, compare each target with
the source. For equal-length contiguous substrings, count positions
containing the same absolute pitch. The absolute similarity is the maximum
such count over every substring pair; mismatching positions are allowed
and incur no penalty. Relative similarity divides that maximum by the
target's length. Limits: 1 second, 64 MB.

## Input

The first line contains source length n and its n notes. Next is m,
1≤m≤100, followed by m lines, each containing a length and that many notes.
Every melody length is between 1 and 1000 inclusive.

A note is dN, dN+ or dN-, where octave d is 1…8 and N is A…G. Natural
semitone offsets in an octave are C=0, D=2, E=4, F=5, G=7, A=9, B=11;
+ and - add or subtract one semitone. Consequently C+=D-, D+=E-, E=F-,
F=E+, F+=G-, G+=A-, A+=B-. B+ is C of the next octave and C- is B of
the previous. The nonexistent 1C- and 8B+ are excluded.

## Output

m real numbers, one relative similarity per target in input order.
Absolute or relative error at most 10⁻⁶ is accepted. Results lie in [0,1].

## Checking

A checker compares every number with error at most 10⁻⁶ · max(1,
|answer|).

## Examples

```
4 5C+ 5D 5C 5G
3
2 5D- 5D
2 5D 4B+
4 5D 5C+ 5D 5F-
```

```
1.000000
1.000000
0.500000
```

## Solution

### Canonical pitches and complete overlaps

Convert a note to 12(d−1)+naturalOffset+accidental. This yields one of
96 absolute pitches and automatically handles octave-boundary aliases.
Octaves remain significant; there is no transposition of an entire melody.

Fix a shift between source indices i and target indices j. Every compared
substring pair using that shift can be extended to the complete overlap.
Adding positions cannot remove any equalities because mismatches cost
zero. Thus it suffices to count equal pitches for each of the n+L−1
nonempty overlaps, where L is the target length. Their largest count is
exactly the original substring maximum.

### Position-pair counting in the compiled versions

Store source positions separately for each pitch. A matching pair (i,j)
belongs to the unique shift i−j. Increment counter i−j+L−1 for every such
pair and take the maximum. Every equality in each overlap is counted once,
and no mismatching pair is counted, proving the result. Reuse source
position lists for all targets, but start with fresh counters for each.

For K matching pairs, comparison time is `O(n+L+K)`, worst case `O(nL)`.
Working space is `O(n+L+96)`, excluding input/output buffers. C++, Go,
Java and Rust use this method.

### Python: many independent counters in one integer

Use base 2¹⁰=1024. For pitch p, build M[p]=Σᵢ:pitch(i)=p 2^(10i).
For target positions j, sum

T = Σⱼ M[target[j]] · 2^(10(L−1−j)).

The base-1024 digit at position i−j+L−1 counts exactly the matching
pairs for that shift. Each digit is at most min(n,L)≤1000, below 1024,
so carries never mix neighboring counters. Extract ten-bit fields and
take their maximum. Once it reaches min(n,L), no larger result is possible.
Finally divide by L, not n.

The packed value has B=10(n+L−1) bits. Python performs L additions/shifts
and at most n+L−1 field extractions. In a w-bit word model a conservative
comparison bound is `O((n+L)·ceil(B/w))`; pitch masks occupy
`O(96·ceil(10n/w))` words. Arbitrary-precision integer operations execute
the dense arithmetic internally, avoiding a Python loop over nL pairs.

In the example, 5C+ equals 5D-, so the first target matches both source
notes at the beginning and scores 2/2=1. The second target matches source
positions 2 and 3 because 4B+=5C, again 2/2=1. For the last target, align
its second and third notes with the first two source notes: two matches
are possible, giving 2/4=0.5.

This is neither longest common substring nor longest common subsequence:
mismatches are allowed, but all comparisons must use one fixed shift.
Normalize enharmonic spellings before comparison, including B+ and C-
across octaves. Divide by the target length. Zero matches is valid.
Packed counters need ten bits, not nine, because a shift can have 1000
matches. Keep all shifts and clear compiled counters between targets.

## Language notes

Python uses exact big-integer field packing. The four compiled versions
enumerate matching position pairs with integer counters. Java reads pitches
directly from a byte buffer to avoid allocating 100,000 temporary note
strings. The source position structure is immutable during comparisons.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1974_bitmask.py](1974_bitmask.py) | Python 3.12 x64 | bitmask | O((n+L)*ceil(B/w)) | AC | 0.390 s | 7056 KB |
| [1974_bruteforce.cpp](1974_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(n*L) | AC | 0.093 s | 596 KB |
| [1974_bruteforce.go](1974_bruteforce.go) | Go 1.14 x64 | bruteforce | O(n*L) | AC | 0.140 s | 3988 KB |
| [1974_bruteforce.java](1974_bruteforce.java) | Java 1.8 | bruteforce | O(n*L) | AC | 0.140 s | 1884 KB |
| [1974_bruteforce.rs](1974_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(n*L) | AC | 0.078 s | 1280 KB |
