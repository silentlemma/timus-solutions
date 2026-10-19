# 2037. Binary words with prescribed palindrome counts

[Timus 2037](https://acm.timus.ru/problem.aspx?space=1&num=2037) · difficulty 1225 · constructive

Original problem by Mikhail Rubinchik, from the Ural FU Dandelion contest, Petrozavodsk training camp, summer 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

For every `i` from `1` through `n`, construct a word of length `n` over
`a,b` containing exactly `i` distinct nonempty palindromic substrings.
Distinctness concerns the substring values, not their positions or
occurrence counts. Report when no such word exists. Time limit: 0.5
seconds; memory limit: 64 MB.

## Input

One integer `1 ≤ n ≤ 2000`, with one instance and no test-count prefix.

## Output

Exactly `n` lines in increasing index order. Line `i` has the form `i : word`,
or `i : NO` if that count is impossible. Any suitable word is accepted.
The word uses lowercase `a,b`; the absence marker is uppercase `NO`.

## Checking

A checker verifies the length and the letters of each word and counts
its distinct palindromes with an eertree; any valid words are accepted,
and the refusal only when no word exists.

## Examples

```
4
```

```
1 : NO
2 : NO
3 : NO
4 : aaaa
```

## Solution

The minimum possible number is `n` for `n≤7`, `7` for `n=8`, and `8`
for every `n≥9`. Every integer from that minimum through `n` is achievable.

### Certifying the impossible counts

Appending a character creates at most one new distinct palindrome.
Any new palindrome must be a suffix. If two suffix lengths were new, the
shorter palindrome would also be a proper prefix of the longer palindrome
and would already occur before the final character. Hence every length-`n`
word has at most `n` distinct palindromes.

The small lower bounds are checked exhaustively by
[tests/gen.py --proof](tests/gen.py). It enumerates every binary word of lengths
one through nine and stores every palindromic substring value using direct
substring comparison with its reversal. The resulting histograms are:

| Length | Distinct-palindrome count : number of words |
| --- | --- |
| 1–7 | `n : 2^n` |
| 8 | `7 : 4; 8 : 252` |
| 9 | `8 : 24; 9 : 488` |

This covers all `1022` words, not a random sample. A word of any length
at least nine contains a nine-character prefix, so at least its eight
distinct palindromes persist in the full word. This proves the lower
bound for arbitrary `n`. The constructions below attain every remaining count.

### A period with a bounded palindrome set

The infinite period `(aababb)…` has exactly
`{a,b,aa,bb,aba,bab,abba,baab}` as its palindromes.
To verify the claim, inspect all six starting residues at each length
from one through six. Lengths five and six have no palindrome.
Every longer palindrome has a central palindrome of length five or six,
so no longer one exists. The script also reproduces this finite check.

For a target `8≤i<n` set `k=i−6≥2`. Start with `k` copies of `a` and append
as many characters as necessary from `(babbaa)…`, taking a prefix so that
the total length is exactly `n`.

There are exactly `k` all-`a` palindromes: `a,a²,…,a^k`. A palindrome
crossing the boundary and containing `b` starts with some `t` copies of `a`.
Its symmetric end has `t` copies after a `b`. Periodic `a`-runs have length
at most two, so `t≤2`. Thus it is contained in the suffix starting at the
last two initial `a` characters, which is a prefix of `(aababb)…`.
Palindromes wholly in the periodic tail satisfy the same period bound.
The only extra values are therefore `b,bb,aba,bab,abba,baab`.
All six occur once the tail has at least seven characters.
Here the tail length is `n−k=n−i+6≥7`, so the total is exactly `k+6=i`.

For `i=n` use `a^n`. The only remaining feasible case is `n=8,i=7`:
use `aababbaa`. It has `a,aa` and the five extra values
`b,bb,aba,bab,abba`; `baab` does not occur yet.
All smaller impossible indices receive `NO`.

For the sample `n=4`, the exhaustive check makes counts one, two
and three impossible. The word `aaaa` has exactly `a,aa,aaa,aaaa`,
giving the fourth line.

Construct and print one row at a time. Time is `O(n²)`, matching the output
size for large `n`, and auxiliary memory is `O(n)`.

Pitfalls:

- Count distinct substring values, not occurrences and not the empty palindrome.
- Length eight is exceptional: seven palindromes are possible there.
- Never print `NO` for a feasible index merely because one pattern failed.
- For the periodic construction use `k=i−6`, with the tail starting at `b`.
- Keep all indices and colons, even on impossible rows.

## Language notes

C++, Go, Rust and Java use buffered output; Java fills one character array
per row. Python prints each row directly. No solver builds a palindrome
tree or stores the complete quadratic-size output.
Only small integer indices are used; no arithmetic overflow is possible.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2037_constructive.cpp](2037_constructive.cpp) | G++ 13.2 x64 | constructive | O(n^2) | AC | 0.046 s | 744 KB |
| [2037_constructive.go](2037_constructive.go) | Go 1.14 x64 | constructive | O(n^2) | AC | 0.031 s | 6220 KB |
| [2037_constructive.java](2037_constructive.java) | Java 1.8 | constructive | O(n^2) | AC | 0.156 s | 5076 KB |
| [2037_constructive.py](2037_constructive.py) | Python 3.12 x64 | constructive | O(n^2) | AC | 0.140 s | 592 KB |
| [2037_constructive.rs](2037_constructive.rs) | Rust 1.75 x64 | constructive | O(n^2) | AC | 0.046 s | 1020 KB |
