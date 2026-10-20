# 2189. The value missing from the fewest subarrays under point updates

[Timus 2189](https://acm.timus.ru/problem.aspx?space=1&num=2189) · difficulty 1061 · fenwick, bitmask

Original problem by Artyom Abaturov and Artyom Stepanov, from the Ural School Programming Contest 2024.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An array of n roles gets q point assignments. After each one, report the
smallest number of subarrays that avoid some value x, over all x. The
limits are 2 seconds and 256 MB.

## Input

n and q, 1 ≤ n, q ≤ 10⁵, then a₁ … a_n with 1 ≤ aᵢ ≤ 10⁹, then q
updates s r that set a_s = r with 1 ≤ r ≤ 10⁹.

## Output

The minimum after each update.

## Examples

### Example 1

Input:

```
6 5
1 2 3 1 1 2
3 4
5 4
2 1
3 1
6 1
```

Output:

```
4
5
4
3
1
```

### Example 2

Input:

```
7 4
2 3 2 3 4 2 3
1 4
4 2
6 5
2 1
```

Output:

```
5
5
9
9
```

## Solution

The subarrays without x are exactly those inside the gaps between
consecutive occurrences of x and the two ends, so a gap of length g
contributes g(g + 1) / 2. A value that does not occur gives
n(n + 1) / 2, the most possible, so only present values matter.

Removing an occurrence at p merges its two neighboring gaps, and with
the nearest occurrences ℓ < p < r (or the ends 0 and n + 1) the count
grows by exactly (p − ℓ)(r − p); adding an occurrence shrinks it by the
same product. So an update changes the scores of two values by one such
product each, once the neighbors of p among their occurrences are
known.

All positions a value will ever occupy are known after reading the
input, so each value keeps its candidate positions sorted, with a
structure marking the current ones: a Fenwick tree with a k-th one
search in the compiled languages, and in Python a bitset of 64-bit
words with a summary of nonempty words. The minimum over values is a
heap of (score, value) pairs where stale entries are skipped when they
reach the top.

In the first example after the first update the array is
[1, 2, 4, 1, 1, 2], and the value 1 leaves gaps of length 2 (positions 2 and 3)
and 1 (position 6), giving 3 + 1 = 4.

Each assignment inserts at most two heap entries. The heap can hold
O(n + q) entries, and each entry is removed at most once, so all heap
operations together cost O((n + q) log(n + q)). Including sorting and
Fenwick searches, the compiled solutions take O((n + q) log(n + q))
total time and O(n + q) space. The heap bound is amortized over updates.

Python's summary is an arbitrary-precision integer with at most
B = ceil(n / 64) bits. Its operations are not asymptotically constant:
allowing O(B) fixed-size digit work per operation, including summary
construction, gives the safe total bound O((n + q)(log(n + q) + B))
with O(n + q) space.

Pitfall (test 06): roles can disappear and return, leaving obsolete
scores in the heap. Check entries against current scores, and do not
claim O(log n) time for every update: one cleanup can remove many
accumulated stale entries.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2189_bitmask.py](2189_bitmask.py) | Python 3.12 x64 | bitmask | O((n + q)(log(n + q) + B)) | AC | 1.109 s | 53288 KB |
| [2189_fenwick.cpp](2189_fenwick.cpp) | G++ 13.2 x64 | fenwick | O((n + q) log(n + q)) | AC | 0.125 s | 12016 KB |
| [2189_fenwick.go](2189_fenwick.go) | Go 1.14 x64 | fenwick | O((n + q) log(n + q)) | AC | 0.203 s | 43852 KB |
| [2189_fenwick.java](2189_fenwick.java) | Java 1.8 | fenwick | O((n + q) log(n + q)) | AC | 0.296 s | 18440 KB |
| [2189_fenwick.rs](2189_fenwick.rs) | Rust 1.75 x64 | fenwick | O((n + q) log(n + q)) | AC | 0.125 s | 16668 KB |
