# 1635. Mnemonics and Palindromes

[Timus 1635](https://acm.timus.ru/problem.aspx?space=1&num=1635) · difficulty 202 · dp

Original problem by Igor Chevdar, from the Thirteenth Ural State University Open Team Programming Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Split a string of lowercase letters into the fewest palindromes and
print their number and the pieces in order. Any optimal split is
accepted.

## Input

One non-empty string of lowercase Latin letters, at most 4000 long.

## Output

The least number of palindromes, then the pieces of an optimal split
separated by spaces.

## Examples

### Example 1

Input:

```
pasoib
```

Output:

```
6
p a s o i b
```

### Example 2

Input:

```
zzzqxx
```

Output:

```
3
zzz q xx
```

### Example 3

Input:

```
wasitacatisaw
```

Output:

```
1
wasitacatisaw
```

## Solution

Let `d[j]` be the minimum pieces for the first `j` letters, with
`d[0]=0`. Every palindrome `s[l..r]` gives the transition
`d[r+1] = min(d[r+1], d[l]+1)`. Remember its start `l` to reconstruct
an optimal partition backwards; reverse the recovered pieces for output.
Every partition has a last palindrome, so these transitions are complete.

The C++, Go, Java and Rust bases enumerate odd and even palindromes by
expanding the `2n−1` centres in increasing order. The dependency is safe:
every piece ending before `l` has its centre strictly before `l`, whereas
the current palindrome's centre is at least `l`. Thus `d[l]` is already
final when used. Enumeration costs `O(n²)` worst-case time and `O(n)`
storage, including reconstruction. No quadratic palindrome matrix is needed.

The existing Python base instead stores palindrome starts as integer
bitsets. At right endpoint `i`, shift the previous starts right by one,
intersect with the positions of `s[i]`, then add the singleton `i` and,
when the last two letters match, the length-two start `i−1`. This is exactly
the inside-palindrome recurrence, with both short bases supplied.

Appending one letter changes the minimum by at most one. The upper bound
comes from a singleton. For the lower bound, remove the last letter of an
optimal final palindrome: its remaining prefix is a first letter followed
by its palindromic interior, at most two pieces instead of one. Therefore
`d[i+1]` is one of `d[i]−1,d[i],d[i]+1`. A bitset `level[v]` stores earlier
prefix positions with minimum `v`; test levels `d[i]−2,d[i]−1` against the
current starts, in that order. Otherwise appending the singleton is optimal.
The lowest set intersection bit supplies a valid predecessor.

With `w` bits per arbitrary-precision limb, Python needs
`O(n²/w+n)` limb operations. Its level masks can occupy `O(n²)` bits in
total, plus `O(n)` indices/objects: a mask's highest position determines
its storage even if it contains only one set bit. This is not the native
DP's linear-storage implementation, and `w` is not assumed to be 64.

## Optimized solutions

The new C++ file keeps the same centre-expansion DP, hence the
`_optimized` suffix. First check whether the whole string is a palindrome:
one piece is then a proven optimum, so return in `O(n)` time. Otherwise
retain the `O(n²)` worst-case DP. With `n≤4000`, counts, the `n+1` sentinel,
prefix indices and reconstructed endpoints fit unsigned 16-bit cells.
Static arrays hold the input, counts, predecessors and endpoints.
Reconstruction prints slices directly with `fwrite`, without creating
substring objects or a vector of strings; stdio replaces iostreams.
The complete program's Accepted memory is 140 KB versus the unchanged
base's 676 KB, a 79.3% reduction. Time is 0.015 s for both; no measured
speedup is claimed. Both C++ versions remain available.

## Checking

An answer checker must validate the count, that all pieces are
palindromes and concatenate to the original string, and that the count
is minimal; different optimal partitions are allowed. The actual new C++
program passed 693 independent extra inputs: all 510 nonempty binary
strings through length eight, 180 random strings, and three length-4000
cases with proved optima 1, 2 and 4000. Small optima came from an independent
suffix-by-suffix reversal DP, not centre expansion. Large cases were one
repeated letter, alternating `ab`, and repeated `abcd` (no palindrome of
length two or three, hence none longer). It also passed all 15 repository
inputs in Docker and obtained an exact-source Accepted. These 693 are
actual C++ runs, not executions of a new Python candidate.

## Language notes

All five existing Accepted sources are preserved byte for byte.
The new C++ comparison is against its own C++ base. The snapshot uses
the agreed C++ top-15%-or-first-ten rule in both metrics; other families
require first place in both. An empty filtered competitor sample gives
formal coverage, not evidence of superiority. A below-target admitted
version would retain a star and the translated explanation.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1635_dp.cpp](1635_dp.cpp) | G++ 13.2 x64 | dp | O(n²) | AC | 0.015 s | 676 KB | 11288441 |
| [1635_dp.go](1635_dp.go) | Go 1.14 x64 | dp | O(n²) | AC | 0.046 s | 1456 KB | 11288442 |
| [1635_dp.java](1635_dp.java) | Java 1.8 | dp | O(n²) | AC | 0.125 s | 796 KB | 11288444 |
| [1635_dp.py](1635_dp.py) | Python 3.12 x64 | dp | O(n²/w + n) | AC | 0.093 s | 2064 KB | 11288443 |
| [1635_dp.rs](1635_dp.rs) | Rust 1.75 x64 | dp | O(n²) | AC | 0.062 s | 304 KB | 11288445 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1635_dp_optimized.cpp](1635_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(n²) | AC | 0.015 s | 140 KB | 11308417 |
