# 1889. Airport Announcements

[Timus 1889](https://acm.timus.ru/problem.aspx?space=1&num=1889) · difficulty 308 · bruteforce

Original problem by Denis Dublennykh, from the NEERC 2011 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Igor heard n phrases of an announcement and knows the language of some
of them; the others are "unknown". The announcement was read in several
languages, each at most once and with the same number of phrases in
each. In how many languages could it have been read? List every
possibility in increasing order, or print "Igor is wrong." if there is
none.

## Input

n (2 ≤ n ≤ 1000), then n lines with a language name (4 to 20 lowercase
letters) or "unknown"; at least one phrase is known.

## Output

All possible numbers of languages in increasing order, or
"Igor is wrong.".

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
6
english
unknown
unknown
unknown
german
unknown
```

Output:

```
2 3 6
```

### Example 2

Input:

```
4
english
french
unknown
english
```

Output:

```
Igor is wrong.
```

### Example 3

Input:

```
3
zulu
zulu
zulu
```

Output:

```
1
```

## Solution

If the announcement was read in k languages, k divides n and the
phrases fall into k consecutive blocks of n/k, one block per language.
For every divisor k check two things. The known phrases of a block must
all be in one language. No language may appear in two different blocks.
Blocks without known phrases can take any new language. Hash sets give
expected `O(n·d(n))`; C++'s ordered set gives `O(n·d(n)·log n)`.

In the first example one block would hold both English and German, so 1
fails. For 2 the blocks are "english ? ?" and "? german ?", for 3 they
are pairs with English first and German in the third, and 6 is always
possible here: the answer is 2 3 6.

Pitfalls:

- the same language in two blocks breaks k, as in the third example
  for 3 languages;
- a block of only unknown phrases is fine;
- the output line is "Igor is wrong." with the dot.

The answers agree with an independent accepted implementation on 125
random announcements.

## Optimized solutions

`1889_bruteforce_optimized.java`. Keep testing only divisors k of n and scanning each block for consistency. Intern known language names to positive integer IDs once, with zero for unknown. A generation-stamped int array checks that a known language does not occur in two blocks, replacing a fresh HashSet and repeated string comparisons for every candidate divisor. Each block must still have at most one known ID; unknown blocks can be assigned distinct unused languages. Iterate k in increasing order and retain the exact failure sentence. With tau(n) divisors, expected time O(n·tau(n)) for bounded 20-character names and O(n) storage; hashing is an expected-cost assumption, not a new worst-case guarantee. This is the same brute-force algorithm with smaller data and 256-byte buffered input.

Compared with `1889_bruteforce.java`: time 0.125 s → 0.109 s; memory 684 KB → 708 KB.

Go compresses the known phrases into consecutive language groups, retaining each name and its first and last phrase indices. An open-addressed table rejects a language that reappears after a different known language. For each divisor of n, every group must lie in one block and different groups must use different blocks. Here d(n) counts the divisors of n. Hash collisions can make group construction quadratic in the worst case. Fixed byte buffers handle input and output; names are compared exactly in 20-byte arrays even when hashes collide.

The accepted base implementations [1889_bruteforce.cpp](1889_bruteforce.cpp), [1889_bruteforce.java](1889_bruteforce.java), [1889_bruteforce.py](1889_bruteforce.py), [1889_bruteforce.rs](1889_bruteforce.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1889_trees_parsing_optimized.rs`. Intern language names with an exact ordered tree instead of randomized hashing, retaining divisor enumeration and epoch-marked block validation.

Accepted #11329230 (Rust 1.75 x64): **0.015 s / 136 KB**. Archived comparison: `1889_bruteforce.rs` (Rust 1.75 x64) — 0.046 s / 448 KB (#11325666).

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. Teaching algorithms are retained. Revalidated basic-source rows use their own new exact-source Accepted metrics and IDs; those checks do not count as optimizations.

`1889_bruteforce_optimized.java`: time place 6/22, memory place 1/22 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1889_bruteforce.cpp](1889_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(n d(n) log n) | AC | 0.001 s | 512 KB | 11325660 |
| [1889_bruteforce.go](1889_bruteforce.go) | Go 1.14 x64 | bruteforce | O(n d(n)) | AC | 0.031 s | 1236 KB | 11291120 |
| [1889_bruteforce.java](1889_bruteforce.java) | Java 1.8 | bruteforce | O(n d(n)) | AC | 0.125 s | 684 KB | 11291124 |
| [1889_bruteforce.py](1889_bruteforce.py) | Python 3.12 x64 | bruteforce | O(n d(n)) | AC | 0.078 s | 528 KB | 11325663 |
| [1889_bruteforce.rs](1889_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(n d(n)) | AC | 0.046 s | 448 KB | 11325666 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1889_bruteforce_optimized.go](1889_bruteforce_optimized.go) | Go 1.14 x64 | bruteforce | O(n² + n d(n)) worst case | AC | 0.031 s | 792 KB | 11311147 |
| [1889_bruteforce_optimized.java](1889_bruteforce_optimized.java) | Java 1.8 | bruteforce | O(n tau(n)) expected | AC | 0.109 s | 708 KB | 11325437 |
| [1889_trees_parsing_optimized.rs](1889_trees_parsing_optimized.rs) | Rust 1.75 x64 | trees, parsing | O(n log n + n d(n)) time; O(n) space | AC | 0.015 s | 136 KB | 11329230 |
