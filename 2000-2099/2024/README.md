# 2024. Selecting whole color groups

[Timus 2024](https://acm.timus.ru/problem.aspx?space=1&num=2024) · difficulty 340 · sorting, combinatorics

Original problem by Nikita Sivukhin, from the Ural Regional School Programming Contest 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `n` distinct objects, identified by their positions in a
string. The lowercase letter at a position gives that object's color.
Select a subset using at most `k` distinct colors. Find its maximum
possible size and the number of different subsets of that size. Two
subsets differ when at least one object index belongs to only one of
them; selecting colors or ordering the chosen objects does not itself
create another subset.

Constraints: `1 ≤ n ≤ 100000`, `1 ≤ k ≤ 26`, colors `a` through `z`.
Time limit: 1 second. Memory limit: 64 MB. The count is an exact
integer, with no modulus.

## Input

The first line contains the color string of length `n`; `n` is not given
separately. The second line contains `k`.

## Output

Print two integers separated by a space: the maximum subset size and the
number of subsets attaining that size.

## Checking

Outputs are compared token by token.

## Examples

```
abcde
1
```

```
1 5
```

```
ababac
2
```

```
5 1
```

## Solution

Count all 26 color frequencies and sort them in descending order,
including zeros. The maximum size is the sum of the first `k`
frequencies. Let `b` be the frequency in position `k` of that order.

If `b = 0`, fewer than `k` colors occur. All objects can be taken, and
there is exactly one such subset. Different choices of absent colors
must not be counted as different sets of object indices.

Otherwise let `g` be the number of frequencies strictly greater than
`b`, and let `t` be the number equal to `b`. Every optimal subset
contains all `g` larger groups and exactly `r = k-g` of the `t` tied
groups. Thus the answer count is `C(t,r)`.

Why are complete groups enough? If a chosen color has an omitted object,
adding that object increases the size without increasing the number of
colors. Such a subset cannot be optimal. If more colors may still be
used, adding any remaining positive group improves the size.
Consequently an optimum uses the `k` most frequent positive groups, or
every positive group if fewer than `k` exist.

For the boundary characterization, replacing a selected smaller group by
an unselected larger group strictly increases the size. Hence every
group above `b` is mandatory, every group below `b` is excluded, and
only choices among equal positive groups remain. Conversely, any `r`
boundary groups have the same total size. Distinct choices differ in
actual object indices because these groups are nonempty. Once colors are
fixed, all their objects must be included, so there are no further
choices within a group.

Compute the binomial coefficient with `q = min(r,t-r)`, starting from
`ways = 1` and applying `ways = ways * (t-i+1) / i` for `i = 1..q`. Each
division is exact because the intermediate result is `C(t,i)`. Use wide
integer multiplication, not factorials: the final maximum is `C(26,13) =
10400600`, but `26!` does not fit in 64 bits.

In the first example, all five frequencies are one, so one object can be
selected in five ways. In the second, the frequencies are 3, 2 and 1:
the groups of sizes 3 and 2 give size 5 and are uniquely determined.

For alphabet size `σ`, time is `O(n + σ log σ)` and frequency storage is
`O(σ)`. Here `σ = 26`, so time is `O(n)`. The submitted programs buffer
the input string, making total additional storage `O(n + σ)`, or `O(n)`
for this fixed alphabet. A cardinality-constrained knapsack over whole
groups is another approach, using `O(σk)` work after counting; it is
useful as an independent check.

Pitfalls:

- The restriction concerns the number of distinct colors, not the number
  of objects.
- Equal-colored objects still have distinct indices, but an optimal
  chosen group is whole.
- Count subsets, not permutations. Absent colors produce no extra choices.
- Resolve ties at the cutoff, including `k = 1` and `k = 26`.
- Do not use factorials or floating point for the exact count.

## Language notes

C++, Go and Rust use 64-bit integers for the binomial coefficient; Java
uses `long`. Python integers are exact. Frequency sums fit ordinary
integers. Java sorts ascending and takes the last `k` entries; the other
ports sort descending and take the first `k`. Go reads through
`fmt.Fscan` with a buffered reader, so a 100000-character token is
supported without the default Scanner token limit. CPython uses the same
linear scan.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2024_sorting_combinatorics.cpp](2024_sorting_combinatorics.cpp) | G++ 13.2 x64 | sorting, combinatorics | O(n) | AC | 0.015 s | 668 KB |
| [2024_sorting_combinatorics.go](2024_sorting_combinatorics.go) | Go 1.14 x64 | sorting, combinatorics | O(n) | AC | 0.046 s | 1772 KB |
| [2024_sorting_combinatorics.java](2024_sorting_combinatorics.java) | Java 1.8 | sorting, combinatorics | O(n) | AC | 0.109 s | 1232 KB |
| [2024_sorting_combinatorics.py](2024_sorting_combinatorics.py) | Python 3.12 x64 | sorting, combinatorics | O(n) | AC | 0.109 s | 776 KB |
| [2024_sorting_combinatorics.rs](2024_sorting_combinatorics.rs) | Rust 1.75 x64 | sorting, combinatorics | O(n) | AC | 0.046 s | 472 KB |
