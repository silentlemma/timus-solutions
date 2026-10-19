# 1916. Short Fragments of Exponentially Long Words

[Timus 1916](https://acm.timus.ru/problem.aspx?space=1&num=1916) · difficulty 3024 · strings

Original problem by Ivan Burmistrov (prepared by Dmitry Ivankov), from NEERC 2012, Eastern subregional contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Each of n symbol types is either stable or has one fixed replacement
word of other types, in bottom-to-top order. Repeatedly replace unstable
symbols until only stable ones remain. Every type is guaranteed to finish
expanding. Starting from any one type, consider all contiguous fragments
of exactly k stable symbols in its final word. Count the different
fragments over all starting types. Repeated occurrences count once.
Limits: 1 second, 64 MB.

## Input

n,k, both between 2 and 100. Then one description for each type 1..n.
A stable type is written as −1. Otherwise the line contains a length
1≤kᵢ≤100 followed by kᵢ type indices in [1,n]. Their order is preserved.
The sum E of all replacement lengths is at most 100.

## Output

The number of distinct length-k fragments modulo 1 000 000 007.
If no final word is long enough, output zero.

## Checking

Compare one integer token exactly.

## Examples

```
7 3
3 3 2 2
3 4 5 5
1 7
-1
-1
3 7 7 7
-1
```

```
5
```

## Solution

The dependency graph is acyclic: a cycle of nonempty replacements would
never finish. Process types with memoized depth-first search. Do not
construct final words, since even 50 doubling rules produce length 2⁵⁰.
For each type retain just its prefix and suffix of length at most k−1.
A stable type contributes its own one-symbol word.

Build an unstable type by concatenating its children from left to right.
When appending B to the already processed prefix A of the replacement,
form the short window suffix(A,k−1)+prefix(B,k−1). Insert every length-k
substring of this window into one global set. Both window halves are
shorter than k, so every such substring crosses the real join.
Update the retained prefix by taking the first k−1 symbols of the two
prefixes, and the retained suffix by taking the last k−1 symbols of the
two suffixes. Use the child's suffix for the latter update, not its prefix.

### Correctness

Every length-k substring of A+B is either inside A, inside B, or crosses
their join. Internal fragments have already been inserted while processing
the previous children or recursively processing B. A crossing fragment
uses at most k−1 symbols on each side, so it occurs in the short window.
Conversely every length-k window substring is a real crossing fragment.
The prefix/suffix updates preserve the exact summaries for the next join.
Induction over the acyclic dependencies and each left-to-right concatenation
therefore collects precisely all valid fragments. Visiting every type
includes every possible starting symbol, and the global set removes duplicates.

### Bounds and representation

A join introduces at most k−1 candidates. There are at most E nonempty
child attachments, so there are at most E(k−1)≤9900 candidate insertions.
Copying and hashing a word costs `O(k)`; expected total time is `O(Ek² + nk)` and
memory `O(Ek² + nk)`. This counts actual word contents, not constant-time
hash assumptions. Under these limits the answer is already smaller than
the modulus; the implementations still apply the required remainder.

Stable type IDs fit in one byte because n≤100. Use byte strings or
character strings as exact set keys. Hash collisions never merge different
words, since the containers compare complete keys for equality.
Forward references and shared descendants are handled by memoization.

The example's length-three words are 777,455,745,554,545. The second
occurrence of 455 does not add a new fragment.

Count distinct words, not occurrences or derivation paths. Include all
initial types. Process full accumulated left summaries: a fragment can
cross several child boundaries, not only two adjacent short children.
Preserve order, distinguish stable IDs, handle unary aliases and k larger
than every word, and do not confuse the child's prefix with its suffix.

## Language notes

Python uses `bytes`, C++/Go use byte strings, Java uses character strings,
and Rust uses byte vectors. Each has an exact hash set/map of words.
Memoized recursion is at most n≤100 levels deep. Go string keys are
immutable and may share a short window's storage; Rust copies each key.
No port stores the exponentially long expansions or relies on a rolling
hash as the identity of a word.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1916_strings.cpp](1916_strings.cpp) | G++ 13.2 x64 | strings | O(E k^2 + n k) | AC | 0.015 s | 672 KB |
| [1916_strings.go](1916_strings.go) | Go 1.14 x64 | strings | O(E k^2 + n k) | AC | 0.031 s | 1332 KB |
| [1916_strings.java](1916_strings.java) | Java 1.8 | strings | O(E k^2 + n k) | AC | 0.093 s | 2160 KB |
| [1916_strings.py](1916_strings.py) | Python 3.12 x64 | strings | O(E k^2 + n k) | AC | 0.078 s | 976 KB |
| [1916_strings.rs](1916_strings.rs) | Rust 1.75 x64 | strings | O(E k^2 + n k) | AC | 0.015 s | 724 KB |
