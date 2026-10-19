# 2058. Odd and even palindromic partitions

[Timus 2058](https://acm.timus.ru/problem.aspx?space=1&num=2058) · difficulty 1671 · strings, dp

Original problem by Mikhail Rubinchik, from the Palindromic Contest of July 11, 2015.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

For every prefix of a string, split it into contiguous palindromes and
find the smallest odd and the smallest even number of pieces. The limits
are 1 second and 64 MB.

## Input

One string of 1 to 300 000 lowercase English letters.

## Output

n lines, one per prefix: the smallest odd number of pieces or `-1` if
there is none, and the smallest even number or `-2` if there is none.

## Checking

Outputs are compared token by token.

## Examples

```
abaa
```

```
1 -2
-1 2
1 -2
3 2
```

For the four prefixes, `a` has only one piece; `ab` has only `a|b`;
`aba` itself is palindrome and also has three pieces; `abaa` has `aba|a`
and `a|b|aa`, giving even minimum two and odd minimum three.

## Solution

### Prefix recurrence and palindrome tree

Let `O[i],E[i]` be the minimum odd/even piece counts. Use infinity
`n+1`, `O[0]=∞`, `E[0]=0`. Every partition ends in a palindromic suffix
of length `L`, so `O[i]=min(E[i−L]+1)` and `E[i]=min(O[i−L]+1)` over all
such suffixes. This includes every possible last cut and changes parity
exactly once.

An eertree stores each distinct palindrome once. Roots have lengths `−1`
and `0`; `link[v]` is the longest proper palindromic suffix. To append a
letter, follow suffix links from the previous longest suffix until the
letter just before that suffix matches the appended letter.
Follow/create its transition to the extended palindrome. A new node's
suffix link is found by the same search starting from its parent's
suffix link. Only the new longest suffix can be a previously unseen
palindrome: any shorter new suffix already occurs as a prefix of that
palindrome. Thus there are at most `n+2` nodes. Zero before the input is
a safe sentinel because input letters are lowercase.

### Compressing a suffix chain into series

Set `d[v]=len[v]−len[link[v]]`. Let `sl[v]` be the first suffix node
with a different difference: use `sl[link[v]]` when the two differences
agree, otherwise `link[v]`. A series consists of `v,link[v],…` stopping
before `sl[v]`. Its lengths are an arithmetic progression with step
`d[v]`. Visit only the leading nodes `last,sl[last],…`.

Store two predecessor minima `C_O[v],C_E[v]` per node. At prefix end `i`
initialize them from `O[b],E[b]` where `b=i−len[sl[v]]−d[v]`, the cut
before the shortest series member. If `d[v]=d[link[v]]`, minimize each
component with the saved component of `link[v]`. Use `C_E[v]+1` to
update `O[i]`, and `C_O[v]+1` for `E[i]`. Crucially, the inherited cache
is from an earlier prefix; never clear all caches or treat it as a
current-prefix suffix value.

### Why the old cache is exactly the needed one

For a leading node `v` with same-difference suffix `u=link[v]`, put
`d=d[v]` and `m=len[u]`. The least period of a palindrome is its length
minus its longest palindromic border, so `u` has least period `d` and
`m≥d`. Within `v`, the prefix and suffix occurrences of `u` start
distance `d` apart. There is no intermediate occurrence: it and the
final occurrence would be equal palindromic ends covering their union,
making a proper palindromic suffix of `v` longer than `u`. The covering
fact follows by reflection: equal palindromic ends of length at least
half a word force every mirrored pair in that word to agree.

At end `i−d`, `u` is leading. Otherwise its suffix-chain predecessor `z`
of the same difference has length `m+d`. Its overlapping prefix and
suffix `u` determine `z=v`. The previous and current copies of `v` then
cover a palindrome `w`. A proper suffix of `w` longer than `v` would
place a prefix copy of `u` strictly between the two end copies inside
`z`, contradicting the preceding argument. Hence `link[w]=v` and
`d[w]=d`, contradicting that `v` is leading now. No occurrence of `u`
ends strictly between `i−d` and `i`, and its current occurrence is not
leading. Its saved cache was therefore last written exactly at `i−d`.

At that earlier end, the series of `u` contains the current lengths
except the longest. Subtracting those lengths from `i−d` gives precisely
the present cut positions for every member except the shortest. The
initialization at `b` supplies that missing cut. Thus both caches equal
the minima over the entire present series. The prefix recurrence now
proves all printed minima by induction, including impossible parities.

### Why there are logarithmically many series

Every border of a palindrome is palindrome, so `d[v]` is indeed its
least period. At the last node `x` of a series write `L=len[x]`,
`B=len[link[x]]`, `p=L−B`. Suppose `B≥2L/3`. Then `B≥2p`; the border has
period `p` and least period `q≤p`. If `q<p`, its length is at least
`p+q`, so its period is also `gcd(p,q)`. The elementary period rule
follows by replacing periods `p<q` by `p,q−p` and repeating Euclid:
comparisons through positions shifted by `p` or `q` prove the difference
period when length is at least their sum. Since the common period
divides `p`, extending the border by the remaining `p` symbols preserves
it, contradicting the least period `p` of `x`. Hence `q=p`,
contradicting the change of difference. Therefore `B<2L/3`, and every
series jump shrinks the length by a constant factor.

## Language notes

The DP takes `O(n log n)` time and `O(n)` space. The tree's suffix
searches have linear total length decreases: a one-letter extension
increases the relevant suffix lengths by at most two. Compiled ports
store sparse child lists and scan at most 26 letters per lookup, giving
deterministic constant lookup cost for this alphabet. Python uses an
integer-key dictionary with expected constant lookup cost, packed 32-bit
metadata/DP arrays, shared infinity objects and byte output; its time
bound is expected. Java writes digits directly to one byte buffer,
avoiding large copied character strings. Other ports also buffer output.
Node IDs, counts and packed lengths fit signed 32-bit integers.

Keep the two parity components separate, initialize only `E[0]=0`, and
swap them when adding a factor. Walk series links for the DP, suffix
links for tree extension. Reinitializing all caches breaks their
time-shift meaning. Unary strings have many suffix palindromes but one
series; ruler words exercise many series. Output every prefix and
preserve the distinct `-1/-2` markers. The infinite value cannot become
a feasible count.

The pair of minima also characterizes all larger feasible counts of the
same parity: when `k+2≤i`, split a factor of length at least three into
its first letter, palindromic middle and last letter; if all factors
have length at most two, split two length-two factors. Each operation
adds two pieces.

The Python solution runs under PyPy: under CPython 3.12 it exceeds the
time limit on the judge's test 48, while PyPy 3.10 is accepted in
0.515 s.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2058_strings.cpp](2058_strings.cpp) | G++ 13.2 x64 | strings | O(n log n) | AC | 0.078 s | 17832 KB |
| [2058_strings.go](2058_strings.go) | Go 1.14 x64 | strings | O(n log n) | AC | 0.078 s | 25560 KB |
| [2058_strings.java](2058_strings.java) | Java 1.8 | strings | O(n log n) | AC | 0.187 s | 21784 KB |
| [2058_strings.py](2058_strings.py) | PyPy 3.10 x64 | strings | O(n log n) | AC | 0.515 s | 54644 KB |
| [2058_strings.rs](2058_strings.rs) | Rust 1.75 x64 | strings | O(n log n) | AC | 0.093 s | 21376 KB |
