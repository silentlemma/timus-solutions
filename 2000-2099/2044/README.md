# 2044. Palindrome-factor masks for every prefix

[Timus 2044](https://acm.timus.ru/problem.aspx?space=1&num=2044) · difficulty 2428 · strings

Original problem by Mikhail Rubinchik, from the Ural FU Dandelion contest, Petrozavodsk training camp, summer 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given a word of `1≤n≤300000` lowercase Latin letters, consider every
nonempty prefix. For each `j` from `1` through `31`, determine whether
that prefix is a concatenation of exactly `j` nonempty palindromes.
Different factors may be equal. Each position must belong to exactly one
factor, in order. A palindrome reads identically in both directions.

Encode the answers for one prefix in a nonnegative integer: bit `j-1` is
one precisely when `j` factors are possible. The answer lies between `0`
and `2^31-1`. Time limit: 0.5 seconds; memory limit: 64 MB.

## Input

One line containing the word. Its length is `n`; there is no separate
integer length.

## Output

Print `n` decimal integers, one per line, in increasing prefix-length
order. Integer tokens are compared exactly.

## Checking

Outputs are compared token by token.

## Examples

```
abaa
```

```
1
2
5
14
```

For `a`, only one factor is possible. For `ab`, only `a|b` works. For
`aba`, use either the whole palindrome or `a|b|a`, so the mask is
`1+4=5`. Finally, `abaa` has partitions `aba|a`, `a|b|aa` and `a|b|a|a`,
with two, three and four factors; its mask is `2+4+8=14`.

## Solution

### Prefix DP and a palindromic tree

Let `D[i]` have bit `j` set when the first `i` letters admit exactly `j`
factors. Unlike the printed answer, this internal mask reserves bit zero
for zero factors. Set `D[0]=1`. Removing the last factor gives the
recurrence `D[i]=OR(D[i-L]<<1)` over all palindromic suffix lengths `L`
of prefix `i`. Retain only bits `0..31`, and print `D[i]>>1`. Counts
above 31 can be discarded because adding a factor never decreases a
count.

An eertree stores one node for every distinct nonempty palindrome and
two roots of lengths `-1` and `0`. A transition labelled `c` wraps a
palindrome in the letter `c`. The suffix link `link[v]` points to its
longest proper palindromic suffix. After adding a letter, ordinary
suffix-link searches find the longest suffix that can be extended,
create at most one node, and determine its suffix link. A sentinel
preceding the word differs from every input letter.

Walking every suffix link for every prefix would be quadratic on a
uniform word. Define `diff[v]=len[v]-len[link[v]]`. Equal differences
form a series on a suffix-link path. Its jump is
`series[v]=series[link[v]]` when the differences agree, and `link[v]`
otherwise. Thus `series[v]` is the first node after the current
equal-difference group.

### One cached union per series

Keep a persistent mask `cache[v]`. At prefix end `i`, start at its
longest palindromic suffix and follow series jumps. For each visited
head `v`, put `d=diff[v]` and `B=len[series[v]]+d`, the shortest
palindrome in this series. First assign `cache[v]=D[i-B]`. If
`diff[v]=diff[link[v]]`, also OR in `cache[link[v]]`. OR `cache[v]<<1`
into the current answer, and move to `series[v]`.

The suffix cache used here normally belongs to an earlier prefix. This
is deliberate; clearing caches at each position breaks the algorithm.

### Why the old cache is exactly the needed union

For a palindrome, every border is also a palindrome: a suffix is the
reverse of the equal-length prefix. Consequently `diff[v]` is its
shortest period, since periods correspond to complementary border
lengths.

Consider a nontrivial series with `u=link[v]` and `diff[u]=diff[v]=d`.
Then `|v|=|u|+d` and `|u|≥d`. The prefix and suffix copies of `u` cover
`v`, their starts differing by `d`. No occurrence of `u` can start
strictly between them: an intermediate overlapping copy would give `u` a
positive period smaller than `d`. Therefore `u` cannot occur as a suffix
at any end strictly between `i-d` and `i`.

Moreover, `u` was a series head at end `i-d`. Otherwise the suffix chain
there contains an immediate same-difference predecessor `z` with
`link[z]=u` and `|z|=|v|`. Its two copies of `u` cover it, forcing
`z=v`. The copies of `v` ending at `i-d` and `i` then cover a longer
palindrome `W`: reflection in its midpoint interchanges the identical
palindromic copies. Its shortest period is `d`, as it has period `d` and
contains `v`. Hence `link[W]=v` with the same difference `d`,
contradicting that `v` is a series head at end `i`.

Thus `cache[u]` was last updated at `i-d`. Inductively it contains
exactly `D[i-d-L]` for the lengths `L=B,B+d,…,|v|-d` in the old series.
These are exactly the current cuts for the longer suffixes `B+d,…,|v|`.
Adding `D[i-B]` supplies the shortest suffix. A singleton series needs
only that one value.

Therefore each cache is the union over precisely its own current series
of cuts. The series partition all palindromic suffixes, and shifting
adds their final factor. Induction on the prefix length proves that all
reported masks are exact. This argument concerns actual cut indices, so
it justifies bitwise unions rather than relying on a minimum-factor
recurrence.

### Complexity

Every two series jumps at least halve the positive palindrome length. To
see this, let the successive lengths be `L,A,B` and suppose `B>L/2`. If
`d` is the shortest period at length `L` and `e` at length `A`, the
middle palindrome inherits period `d` but its difference is different,
so `e<d`. Also `e≤A-B`. The prefix and suffix copies of the length-`A`
palindrome cover the length-`L` palindrome and overlap in `2A-L>2e`
positions. Two `e`-periodic words overlapping in at least `e` positions
have an `e`-periodic union: every pair of positions at distance `e` is
covered by one copy. This contradicts minimality of `d`. Thus `B≤L/2`.

A single jump need not halve: `aabaaabaa` gives lengths `9→5`. The
two-jump bound suffices for `O(log n)` series per prefix. Standard
amortized suffix searches and a fixed alphabet complete the bound: `O(n
log n)` time and `O(n)` space. Python's packed-key transition dictionary
gives expected lookup time; the other ports use bounded-alphabet arrays.

The underlying series-link technique is discussed in [Rubinchik and
Shur, EERTREE, Section 4.1](https://arxiv.org/abs/1506.04862). The
cut-union argument above explains its use for exact factor-count masks.

Pitfalls:

- Factors are nonempty. Internal bit zero exists only for the empty prefix.
- Use OR, not addition: different cuts may produce the same factor count.
- Truncate the internal mask to 32 bits, then shift right once for
  output. Java needs unsigned right shift.
- Keep old series caches. Their time displacement is part of the proof.
- A zero mask can become nonzero later when a longer suffix reaches an
  earlier cut; do not stop processing.
- Keep node indices compact. Dense arrays of 64-bit transitions can
  exceed the memory limit.

## Language notes

C++ and Go use 26-element 32-bit transition arrays. Rust also uses
32-bit transitions and converts node indices for indexing. Java keeps
sparse outgoing edges in primitive arrays; a node's incoming edge has
the same index as that node, and at most 26 edges are scanned. Output is
buffered.

Python stores node fields and masks in compact `array` objects, uses one
dictionary keyed by `parent*26+letter` and writes output in chunks.

The Python solution runs under PyPy: under CPython 3.12 it exceeds the
time limit on the judge's test 32, while PyPy 3.10 is accepted in
0.375 s.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2044_strings.cpp](2044_strings.cpp) | G++ 13.2 x64 | strings | O(n log n) | AC | 0.062 s | 38264 KB |
| [2044_strings.go](2044_strings.go) | Go 1.14 x64 | strings | O(n log n) | AC | 0.062 s | 41724 KB |
| [2044_strings.java](2044_strings.java) | Java 1.8 | strings | O(n log n) | AC | 0.171 s | 12552 KB |
| [2044_strings.py](2044_strings.py) | PyPy 3.10 x64 | strings | O(n log n) | AC | 0.375 s | 34936 KB |
| [2044_strings.rs](2044_strings.rs) | Rust 1.75 x64 | strings | O(n log n) | AC | 0.046 s | 42084 KB |
