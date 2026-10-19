# 2057. Minimum and maximum nonpalindromic factors

[Timus 2057](https://acm.timus.ru/problem.aspx?space=1&num=2057) · difficulty 3259 · strings

Original problem by Nikita Sivukhin, from the Palindromic Contest of July 11, 2015.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Split a string of English letters into contiguous nonempty pieces, none
of which is a palindrome; case matters, and a single piece is allowed.
Find the smallest and the largest possible numbers of pieces. The limits
are 1 second and 64 MB.

## Input

One string of 1 to 200 000 English letters.

## Output

`-1` if no split exists, otherwise the smallest and the largest number
of pieces.

## Checking

Outputs are compared token by token.

## Examples

```
a
```

```
-1
```

```
abba
```

```
2 2
```

```
babcbcb
```

```
1 2
```

The letter `a` cannot form a permitted piece. For `abba`, the whole word
is palindromic but `ab|ba` gives two; length four permits no more. For
`babcbcb`, one piece works, and `babcb|cb` gives two. Three would
require lengths 2, 2 and 3 in some order: the three possibilities each
contain a palindrome, so the maximum is two.

## Solution

### Exact palindrome queries

Compute odd and even Manacher radii. `odd[c]` counts the central letter
and `even[c]` is the radius about the gap before `c`. For half-open
interval `[l,r)` of length `L` and center `c=floor((l+r)/2)`, it is
palindrome exactly when `odd[c]≥floor(L/2)+1` for odd `L`, or
`even[c]≥L/2` for even `L`. Manacher copies the radius mirrored inside
the current rightmost palindrome, truncates at its boundary, then
expands; each newly reached boundary position is charged once per pass.
Thus preprocessing is linear and queries are exact `O(1)`.

### Maximum: two levels and two cuts per level

Let `d[i]` be the largest number of valid factors of prefix `s[0:i]`, or
`-1` if impossible; `d[0]=0`. Its direct recurrence is `d[i]=1+max d[j]`
over `j≤i−2` with a nonpalindromic suffix `s[j:i]`. At step `i` insert
the newly eligible cut `j=i−2`. Keep the first and last cut at every
feasible score, and the greatest inserted score `M`. Test levels `M` and
`M−1` in that order, testing their extreme cuts. A successful suffix
gives `d[i]=level+1`; if neither succeeds, set `-1`. The two lemmas
below prove this exact recurrence reduction.

For one fixed score `v`, the interval between any two cuts of score `v`
is palindrome: otherwise appending that interval would improve the later
score. Consecutive gap words are therefore palindromes, as are
concatenations of adjacent gaps. Such adjacent words commute, so all
gaps are powers of one primitive palindromic word `U`. Here the
elementary fact `XY=YX` follows by cancelling the shorter prefix
repeatedly, as in Euclid; it expresses both words as powers of a common
primitive root. If both extreme suffixes are palindromes, write the last
suffix as `T` and the first as `U^k T`. Reversal gives `U^k T=T U^k`, so
`T` is also a power of `U`. Every intermediate suffix is then
palindrome. Therefore a level yields a valid suffix if and only if an
extreme cut does.

It remains to prove that feasible `d[i]` is `M` or `M+1`. The upper
bound is the direct recurrence; `M≤1` is immediate. Suppose `M≥2` and a
feasible `d[i]<M`. Every cut with score at least `M−1` must then have a
palindromic suffix. Choose an optimal `M`-factor prefix ending at an
eligible cut, followed by tail `Y` of length at least two. Call its last
two factors `Q,P`. Both `Y` and `PY` are palindromes.

Let the final run of `PY` be `a^r` (including letters of `P` if `Y` is
constant). The palindrome `PY` starts with exactly `a^r b`, `b≠a`,
inside the nonpalindrome `P`. If `Qa^r` were nonpalindromic, moving the
cut before `b` would give `M` factors. Hence `Qa^r` is palindrome. If
`r≥2`, `Qa^(r−1)` is nonpalindromic: two consecutive palindromic
prefixes would force period one, contradicting nonpalindromic `Q`. The
remaining suffix has unequal first/last run lengths 1 and `r`, so is
also nonpalindromic, another contradiction. Thus `r=1`.

Now `Qa` is palindrome and begins with `a`, so `Qab` is nonpalindromic.
Its cut has score at least `M−1`, forcing `(PY)[2:]` to be palindrome.
Together with palindromic `PY` this gives period two. Since its first
letters differ, `PY` is an odd alternating word; `Y` is odd alternating
of length at least three and `P` is a power of `ab` of even length.

Propagate backwards. If all factors after `A_h` followed by `Y` form an
odd alternating tail of length at least `2(M−h)+3`, either `A_h a` or
`A_h aba` being nonpalindromic would finish a partition into `M`
factors: split the remaining even alternating tail into `M−h` positive
even lengths. Therefore both extensions are palindromes. Their length
difference two forces the same period-two pattern and even length for
`A_h`. All original factors are thus powers of `ab` of even length. The
entire string is odd alternating; all its nonpalindromic factors have
even length, so no valid partition exists. Contradiction. This proves
the bound and the two-level algorithm by induction.

### Minimum is one or two whenever feasible

If `AB`, `BC` and `ABC` are all palindromes, then `B` is palindrome.
Indeed `ABC` has periods `|A|` and `|C|`, from its palindromic
suffix/prefix. Its length exceeds their sum, so it has their greatest
common divisor as a period. To see this elementary period rule, for
`p<q` and length at least `p+q`, comparisons `i→i−p→i−p+q` when `i≥p`
and `i→i+q→i+q−p` otherwise give period `q−p`; repeat Euclid. Reflection
maps `B` to an equally long substring starting at `|C|` instead of
`|A|`; these starts are congruent modulo the common period, hence `B`
equals its reversal.

In any three consecutive nonpal factors, merge either adjacent pair if
their concatenation is nonpal. If both pairs are pal, the three-factor
concatenation must be nonpal by this lemma, so merge all three.
Repeating reduces every feasible partition to one or two pieces. Thus
after the DP proves feasibility, the minimum is one when the entire
string is nonpalindromic, otherwise two.

## Language notes

Manacher, DP and the final query take `O(n)` time and `O(n)` space.
There are at most `floor(n/2)` pieces, so score arrays need that many
levels plus zero. All implementations use exact integer indices and
iterative loops; Python uses CPython 3.12. The complete input is
retained in each port.

Insert cut `i−2`, not `i−1`; score zero belongs only to the empty
prefix. Ignore impossible prefixes. Preserve both extreme cuts, not just
the latest. A palindrome can still split, as `abba` shows; a nonconstant
string can be impossible, as `ababa` shows. Shortest-prefix greed and
restricting factor lengths to two or three are invalid. Mixed letter
case and both center parities must be handled. No probabilistic hash or
scan over all DP levels is used in the solutions.

Do not confuse even length with an even exponent of `ab`: test `edge_05`
(`ababa`) has palindromic `Y=aba` and `PY=ababa` with `P=(ab)^1`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2057_strings.cpp](2057_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.031 s | 3528 KB |
| [2057_strings.go](2057_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.046 s | 8564 KB |
| [2057_strings.java](2057_strings.java) | Java 1.8 | strings | O(n) | AC | 0.140 s | 6444 KB |
| [2057_strings.py](2057_strings.py) | Python 3.12 x64 | strings | O(n) | AC | 0.875 s | 19968 KB |
| [2057_strings.rs](2057_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.046 s | 6044 KB |
