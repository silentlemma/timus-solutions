# 1932. Pair Counts by Four-Digit Distance

[Timus 1932](https://acm.timus.ru/problem.aspx?space=1&num=1932) · difficulty 963 · combinatorics

Original problem from Open Ural FU Championship 2012 | by Victor Vinogradov (prepared by Egor Shchelkonogov).

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given distinct four-character hexadecimal identifiers, count unordered
pairs that differ in exactly one, two, three and four character positions.
Leading zeros occupy real positions. Limits: 1 second, 64 MB.

## Input

First n, 2≤n≤65536, followed by n distinct strings of length four.
Allowed symbols are 0..9 and lowercase a..f. The identifier 0000 is valid.

## Output

Four integers, in increasing order of differing-position count.
Every unordered pair belongs to exactly one of the four output classes.

## Checking

Exact comparison of four integer tokens.

## Examples

```
3
dead
beef
f00d
```

```
0 0 2 1
```

## Solution

For k=1,2,3, let S_k sum the pair counts agreeing on each chosen subset
of k positions. This counts with multiplicity: a pair agreeing in r
positions contributes C(r,k), once for each eligible subset.
There are no pairs agreeing in all four positions because identifiers
are distinct. Let d_j denote pairs differing in j positions. Then
S_3=d_1, S_2=3d_1+d_2 and S_1=3d_1+2d_2+d_3. Thus compute
d_1=S_3, d_2=S_2−3d_1, d_3=S_1−3d_1−2d_2, and finally
d_4=n(n−1)/2−d_1−d_2−d_3. These identities prove the inversion.

Compute the statistics online. For every selected position subset, keep
a frequency table of its projected digits. When a new identifier arrives,
add the old frequency of its key to the corresponding S_k, then increment
that frequency. Each matching unordered pair is counted once, at its
later endpoint, so these are exactly the required statistics.

Use four tables of size 16 for single positions, six of size 256 for pairs,
and four of size 4096 for triples: 17,984 counters. Separate tables keep
different position subsets distinct. Parse each identifier as an integer,
then extract exactly four nibbles; this retains all leading-zero positions.
The selected-position keys are packed in position order.

O(14n+17984) time and 17,984 frequency counters plus buffered input.
For fixed four digits and alphabet 16 this is O(n) time, O(1) working
frequency space and O(n) total space with the submitted input buffers.

Count differing digits, not bits: 0000 and 000f differ in one position.
Do not share frequency tables between different position subsets.
S_k includes binomial multiplicities, so it is not simply the number
of pairs with at least k matches. Distinctness is needed for S_3=d_1.
Add a prior frequency before incrementing it, and keep output distances
in the order 1,2,3,4. Do not lose the fixed width when parsing leading zeros.

## Language notes

Use signed 64-bit totals and promote before n(n−1): at n=65536 the
product is 4,294,901,760, exceeding signed32 before division. The pair
total is 2,147,450,880. Bucket counters fit 32 bits: at most 4096,256,16
for one-, two- and three-position projections. C++, Go, Java and Rust
use wide accumulators; Python integers are exact. Java has buffered
decimal/hexadecimal input. C++ changes only its input stream to hex
after reading n; output stays decimal. Python uses CPython.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1932_combinatorics.cpp](1932_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(n) | AC | 0.046 s | 720 KB |
| [1932_combinatorics.go](1932_combinatorics.go) | Go 1.14 x64 | combinatorics | O(n) | AC | 0.046 s | 3184 KB |
| [1932_combinatorics.java](1932_combinatorics.java) | Java 1.8 | combinatorics | O(n) | AC | 0.140 s | 4948 KB |
| [1932_combinatorics.py](1932_combinatorics.py) | Python 3.12 x64 | combinatorics | O(n) | AC | 0.359 s | 4844 KB |
| [1932_combinatorics.rs](1932_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(n) | AC | 0.046 s | 1332 KB |
