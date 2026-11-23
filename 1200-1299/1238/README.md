# 1238. Folding a string with repeat counts

[Timus 1238](https://acm.timus.ru/problem.aspx?space=1&num=1238) · difficulty 416 · dp

Original problem by Roman Elizarov, from the ACM ICPC Northeastern European Regional Contest 2002–2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A folded sequence is a letter, two folded sequences written one after the
other, or `X(S)` for a folded sequence S and an integer X > 1, which
stands for S repeated X times. Given a string of 1 to 100 capital
letters, print a shortest folded sequence that unfolds to it.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The string.

## Output

A shortest folded sequence; any of them will do.

## Checking

Several foldings can be equally short, so the checker unfolds the
answer, compares it with the input and compares its length with the
minimum length.

## Examples

### Example 1

Input:

```
AAAAAAAAAABABABCCD
```

Output:

```
9(A)3(AB)CCD
```

### Example 2

Input:

```
NEERCYESYESYESNEERCYESYESYES
```

Output:

```
2(NEERC3(YES))
```

## Solution

Let `best[i][j]` be the length of the shortest folding of `s[i..j]`. Its
top level is either a concatenation, so it splits into two shorter
foldings at some k, or a single `X(S)`, so the segment is S's unfolding
repeated X times. That gives the interval DP, by growing length:

- `best[i][j] = min(best[i][k−1] + best[k][j])` over the split points;
- for each divisor p < length of the segment's length such that the
  segment has period p, also `digits(length/p) + 2 + best[i][i+p−1]`.

The segment has period p exactly when it equals itself shifted by p,
`s[i..j−p] = s[i+p..j]`. Each interval remembers its choice, and the
folding is rebuilt from the top. For an interval of length L, each proper
divisor p requires comparing L−p characters in the worst case. Summed over
all intervals and divisors, this costs `O(n³ log n)` time; the DP uses
`O(n²)` space, with n ≤ 100.

Pitfalls:

- counts can have two or three digits, and their length counts:
  `100(A)` and `A99(A)` are equally short (test 04);
- the inner part of a repeat is itself folded, as in `2(NEERC3(YES))`;
- a substring comparison is not constant time: all-equal strings (test 04)
  require full comparisons for every proper divisor, giving the logarithmic
  factor in the worst-case time bound.

The teaching Python version memoizes the shortest folded string itself for each substring. Start with the literal text, then try each split and each unit whose repetitions rebuild the text. Keep the shortest encoded candidate, including the count and parentheses for a repetition. The memoized result for the input is already printable. With N input characters, copying, hashing and comparing strings give O(N⁴) time and the stored strings take O(N³) space in the worst case.

## Optimized solutions

The new C++ and Go versions keep interval DP but precompute the longest common prefix of each pair of suffixes. An interval of length L has period p precisely when p divides L and LCP[left][left+p]≥L−p, giving constant-time repetition checks. Try all splits and all possible periods; include the decimal digit count and two brackets in a repetition’s cost. Time is O(n³) and tables use O(n²) space. With n≤100, lengths and LCP values fit bytes; signed-byte decisions distinguish a positive split, a negative period and zero for literal text. Reconstruction produces at most 100 characters. The simple versions remain, and Java, Python and Rust reuse their admitted base implementations in the fast set.

The accepted base implementations [1238_dp.java](1238_dp.java), [1238_dp.py](1238_dp.py), [1238_dp.rs](1238_dp.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1238_dp_optimized.rs`. Precompute longest common prefixes, divisors of each length and decimal digit counts. A period check then uses one LCP comparison, and DP transitions no longer allocate temporary decimal strings. Time is O(n³) and storage O(n²); reconstruction is unchanged.

Accepted #11328694 (Rust 1.75 x64): **0.031 s / 348 KB**. Archived comparison: `1238_dp.rs` (Rust 1.75 x64) — 0.046 s / 316 KB (#11283818).

## Language notes

These notes describe the simple implementations.

- All languages compare the shifted substrings with one library call.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1238_dp.cpp](1238_dp.cpp) | G++ 13.2 x64 | dp | O(n³ log n) | AC | 0.031 s | 460 KB | 11283813 |
| [1238_dp.go](1238_dp.go) | Go 1.14 x64 | dp | O(n³ log n) | AC | 0.031 s | 1264 KB | 11283814 |
| [1238_dp.java](1238_dp.java) | Java 1.8 | dp | O(n³ log n) | AC | 0.125 s | 1108 KB | 11283817 |
| [1238_dp.py](1238_dp.py) | Python 3.12 x64 | dp | O(n³ log n) | AC | 0.125 s | 696 KB | 11283815 |
| [1238_dp.rs](1238_dp.rs) | Rust 1.75 x64 | dp | O(n³ log n) | AC | 0.046 s | 316 KB | 11283818 |
| [1238_strings.py](1238_strings.py) | Python 3.12 x64 | strings | O(N⁴) | AC | 0.203 s | 1312 KB | 11315944 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1238_dp_optimized.cpp](1238_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(n³) | AC | 0.015 s | 144 KB | 11314905 |
| [1238_dp_optimized.go](1238_dp_optimized.go) | Go 1.14 x64 | dp | O(n³) | AC | 0.031 s | 320 KB | 11314912 |
| [1238_dp_optimized.rs](1238_dp_optimized.rs) | Rust 1.75 x64 | dp | O(n³) time; O(n²) space | AC | 0.031 s | 348 KB | 11328694 |
