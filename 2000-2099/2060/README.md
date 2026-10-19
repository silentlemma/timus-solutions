# 2060. Count adjacent palindromic occurrences

[Timus 2060](https://acm.timus.ru/problem.aspx?space=1&num=2060) · difficulty 650 · strings

Original problem by Mikhail Rubinchik, from the Palindromic Contest of July 11, 2015.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Count the pairs of adjacent nonempty palindromes in a string: triples 0
≤ i ≤ j < k < n with both s[i..j] and s[j+1..k] palindromes. Equal texts
at different positions count separately. The limits are 1 second and 64
MB.

## Input

One string of 1 to 300 000 lowercase Latin letters.

## Output

The exact count.

## Checking

Outputs are compared token by token.

## Examples

```
abaa
```

```
5
```

For `abaa`, the numbers of palindromes ending at successive positions
are `E=[1,1,2,2]`, and the numbers starting there are `S=[2,1,2,1]`. The
three internal boundaries contribute `1·1`, `1·2` and `2·1`, for a total
of five. For example, the first boundary counts `a|b` although the pair
does not cover the whole word; the last counts `a|a` and `aba|a`.

## Solution

### Count choices independently at each boundary

Let `E[j]` count all nonempty palindromic occurrences ending at `j`, and
`S[j]` all starting at `j`. At boundary `j|j+1`, choose any left
occurrence from `E[j]` and any right occurrence from `S[j+1]`. Their
positions determine exactly one valid triple. Conversely, every valid
triple has one such boundary and one pair of choices. Thus the answer is
`sum(E[j]·S[j+1])` for `0≤j<n−1`. This counts positions, not distinct
palindrome strings.

### Manacher radii give ranges of endpoints

For odd center `c`, radius `r≥1` includes the center and describes
palindromes of lengths `1,3,…,2r−1`. Their ending positions run once
each through `[c,c+r−1]`, and their starting positions through
`[c−r+1,c]`. For an even center at the gap before `c`, radius `r≥0`
gives ending positions `[c,c+r−1]` and starting positions `[c−r,c−1]`.
An even radius zero contributes nothing.

Find both radius families with Manacher. Keep the palindrome window
reaching farthest right. Inside it, copy the already known mirrored
radius, clipped at the right boundary, then compare outward while both
positions exist and their letters match. Outside the window begin with
radius one for odd centers and zero for even centers. Reflection proves
the copied interior, and the comparisons prove the maximal remaining
extension. Each center incurs at most one failing comparison; successful
new comparisons advance the rightmost boundary. Each pass is therefore
`O(n)`.

Add each endpoint interval to a difference array in `O(1)`: for
inclusive `[l,r]`, add one at `l` and subtract one at `r+1`. After all
centers, prefix sums of the two arrays are exactly `E` and `S`. Each
palindrome has a unique center, parity and radius, so it contributes
once to its own start and end; no occurrence is lost or duplicated. The
boundary formula then proves the answer.

### Memory and integer sizes

The odd and even passes share one radius array. Reset the window between
passes. During the even pass, the active window was created at an
earlier center `q<c`, so the mirrored index is `2q−c<c`. It therefore
reads an already overwritten even radius, never a stale odd value. The
endpoint difference arrays have `n+1` cells, allowing subtraction at
`n`; only positions `0..n−1` become actual counts.

Every endpoint count is at most `n`, so signed 32-bit arrays suffice.
The product of two counts can exceed 32 bits, and the final answer can
reach `n(n−1)(n+1)/6`. Indeed, there are `C(n+1,3)` possible index
triples, and every one is valid in a constant string. At `n=300000` the
answer is `4499999999950000`. C++, Go, Java and Rust convert to signed
64-bit before multiplying; Python integers are exact.

## Language notes

Two Manacher passes, range updates, prefix sums and the boundary sum
take `O(n)` time and `O(n)` space. All implementations are iterative and
compare letters exactly. Python uses CPython 3.12 and three packed
signed 32-bit arrays; the other languages use integer vectors/arrays.
Input is one word and output one number.

Do not count only the longest palindrome at an endpoint. Include single
letters and both center parities. Do not let an empty even palindrome
contribute. The right interval for an even center ends at `c−1`, unlike
the odd case. Pair `E[j]` with `S[j+1]`, not `S[j]`, and skip the outer
boundaries. Do not deduplicate equal text or restrict to pairs covering
the whole word. A one-letter input has answer zero. Perform the cast
before multiplication, not after an overflowing 32-bit product.

The Python solution runs under PyPy: under CPython 3.12 it exceeds the
time limit on the judge's test 49, while PyPy 3.10 is accepted in
0.234 s.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2060_strings.cpp](2060_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.031 s | 4268 KB |
| [2060_strings.go](2060_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 9932 KB |
| [2060_strings.java](2060_strings.java) | Java 1.8 | strings | O(n) | AC | 0.109 s | 5140 KB |
| [2060_strings.py](2060_strings.py) | PyPy 3.10 x64 | strings | O(n) | AC | 0.234 s | 6988 KB |
| [2060_strings.rs](2060_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.046 s | 4596 KB |
