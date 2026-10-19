# 1989. Palindromes under letter replacement

[Timus 1989](https://acm.timus.ru/problem.aspx?space=1&num=1989) · difficulty 338 · strings, fenwick, hashing

Original problem by Mikhail Rubinchik, from the Open Ural FU Championship 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Maintain a word of `n` lowercase English letters. Each operation either
replaces one letter or asks whether an inclusive substring reads
identically from left to right and from right to left. There are `m`
operations, with `5≤n,m≤100000`. Positions are 1-based. Time limit: 0.5
seconds; memory limit: 64 MB.

## Input

The word, then `m`, then `m` operations. `change i a` assigns letter `a`
to position `i`, where `1≤i≤n`. `palindrome? l r` asks about positions
`l` through `r`, where `1≤l≤r≤n`. An assignment may leave the letter
unchanged.

## Output

For every query, in input order, print `Yes` for a palindrome and `No`
otherwise. Replacements produce no output.

## Checking

Outputs are compared token by token.

## Examples

Input:

```
abcda
5
palindrome? 1 5
palindrome? 1 1
change 4 b
palindrome? 1 5
palindrome? 2 4
```

Output:

```
No
Yes
Yes
Yes
```

The first whole word is not a palindrome, while a single letter always
is. Replacing position 4 by `b` produces `abcba`; both the whole word
and `bcb` then are palindromes.

## Solution

### Exact mirrored buffers: C++, Go, Python, Rust

Store the word `s` and its reverse `t`, maintaining `t[n−1−i]=s[i]`. A
replacement writes to both positions. Convert a query to the zero-based
half-open interval `[l,r)`. Its reverse is exactly `t[n−r:n−l]`, so
compare that range with `s[l:r]`.

Initially the invariant holds by construction. Both assignments preserve
it, including assigning the existing value. For each offset `j` in the
interval, `t[n−r+j]=s[r−1−j]`. Therefore the ranges are equal exactly
when every pair of mirrored letters in the requested substring is equal.
This proves every answer, without hash collisions. Singletons and both
ends of the word require no special case.

Let `L` be the sum of all queried substring lengths. Initialization
costs `O(n)`, a replacement `O(1)`, and a query at most its length.
Total processing time is `O(n+m+L)`, with worst case `O(nm)`, not
logarithmic. Contiguous comparisons run in native library code: C++
`memcmp`, Go `bytes.Equal`, Rust slice equality, and CPython
`bytearray.startswith` with a `memoryview` of the mirrored buffer. The
Python view observes point assignments; no buffer is resized or copied
for a query.

For the actual comparison it is enough to use only `h=floor((r−l)/2)`
characters: compare `s[l:l+h]` with `t[n−r:n−r+h]`. These cover every
mirrored pair once; an odd middle character matches itself. For a
singleton both ranges are empty and the result is true.

### Four-field Fenwick hashes: Java

Java uses two Fenwick trees per prime, independently for
`p=1000000007,1000000009,998244353,1000000033`. Choose an independent
uniform base `B` from `2..p−2` at startup. Precompute powers, and store
the forward weight `s[i]Bⁱ` and backward weight `s[i]Bⁿ⁻¹⁻ⁱ`, modulo
`p`. Construct the trees in linear time by adding each node to its
Fenwick parent. A letter difference changes both weights at one
position, so each replacement takes `O(log n)`.

For `[l,r)`, obtain range sums `F,G` from prefix differences and check
`F·Bⁿ⁻ʳ ≡ G·Bˡ (mod p)` in every field. The common scale aligns the
first forward character with the last backward one. A genuine palindrome
always passes. For a nonpalindrome, subtracting the two aligned
polynomials and removing their common power gives a nonzero polynomial
of degree at most `n−1`: at least one coefficient is a nonzero letter
difference between −25 and 25, hence nonzero modulo every prime.

A nonzero polynomial over a field has at most its degree many roots. For
fixed inputs independent of the random choices, the probability that any
of at most `m` queries is falsely accepted is bounded by
`m·∏((n−1)/(p−3)) < 1.1·10⁻¹¹`. Independent bases are selected with
`java.util.Random`; this is a Monte Carlo algorithm, not a deterministic
equality certificate. The bound models uniform independent draws and
excludes adaptive queries based on the secret bases. Four fields take
`O(n+m log n)` total time and `O(n+m)` memory including buffered
answers. An unequal hash safely rejects immediately.

### Implementation and limits

All letter arithmetic is on ASCII values. Java uses `long` for products
below `p²<1.01·10¹⁸`, reduces signed differences before multiplication,
and keeps each Fenwick node below `p`; two nodes sum below the signed
`int` limit. A prefix accumulates at most 17 nodes in a `long`. No
modular inverses are needed. Java has a byte-buffer reader; Go is
compatible with 1.14.

The exact variants store `O(n)` word buffers and up to `O(m)` answers.
Go and Rust additionally retain `I` input bytes, making their actual
storage `O(n+m+I)`. Python uses CPython 3.12; PyPy 3.10 was measured and
exceeded both the time and memory limits on long true queries. Exact
comparisons still have a quadratic worst case, so the 0.5-second limit
is tight for them.
Static Manacher radii alone do not survive point changes; rebuilding
after every change also has a quadratic bound.

Test-generation pitfall: the numbered generator cases 26–29
(`generated_exhaustive5` through `generated_exhaustive8`) use only sizes
`5..8`. Binary mode `exhaustiveN` emits
`m=N·2^N·(1+N(N+1)/2)` operations. Thus `exhaustive4` violates `n≥5`,
and `exhaustive9` emits 211968 operations, exceeding `m≤100000`.
The generator rejects sizes outside `5..8` before constructing a trace.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1989_strings.cpp](1989_strings.cpp) | G++ 13.2 x64 | strings | O(n+m+L) | AC | 0.375 s | 1560 KB |
| [1989_strings.go](1989_strings.go) | Go 1.14 x64 | strings | O(n+m+L) | AC | 0.265 s | 10216 KB |
| [1989_strings.java](1989_strings.java) | Java 1.8 | strings | O(n+m log n) | AC | 0.156 s | 10448 KB |
| [1989_strings.py](1989_strings.py) | Python 3.12 x64 | strings | O(n+m+L) | AC | 0.500 s | 9896 KB |
| [1989_strings.rs](1989_strings.rs) | Rust 1.75 x64 | strings | O(n+m+L) | AC | 0.281 s | 5200 KB |
