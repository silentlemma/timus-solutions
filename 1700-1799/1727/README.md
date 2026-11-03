# 1727. Znaika's Magic Numbers

[Timus 1727](https://acm.timus.ru/problem.aspx?space=1&num=1727) · difficulty 202 · greedy

Original problem by Ivan Burmistrov, from the Ural Regional Team Programming Contest 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Find a set of distinct positive integers below 10⁵ whose digits add up
to n in total, or print −1 if there is none.

## Input

n (0 < n < 10⁵).

## Output

The size of the set and then its numbers, or −1. Any fitting set is
accepted.

## Checking

Use the constructive checker, not equality to one sample output.
Check the declared count, positive values below 100000, no duplicates,
and the exact total of all decimal digits. Each of the five new sources
passed 13 repository cases in Docker and obtained its own exact-SHA
Accepted. The C++ formatting revision separately passed all 13 cases.
The actual new Python program was also checked on 265 inputs. A separate
prefix/remainder model was verified for all 99999 legal targets; these
are model checks, not 99999 runs of each language. Include targets
1, 9, 45, 46, and 99999 to exercise the small finish and both phases.

## Examples

### Example 1

Input:

```
17
```

Output:

```
3
7 12 43
```

## Solution

Let `s(x)` be the decimal digit sum and `L=100000`. The readable
greedy bases first build `s(i)=s(i//10)+i%10` for every `i<L`, then scan
downward from `L−1`, taking each number if its digit sum fits the remaining
target. Each number is visited once, so chosen values are distinct and
in range. Time and auxiliary digit-table storage are `O(L)`; output is
stored separately in `O(q)` space for `q` chosen numbers.

Why does this greedy always finish? Every number in `[90000,99999]` has
digit sum at most 45, and the sum over that entire block is
`9·10000+4·45·1000=270000`. If the remainder were still at least 45 after
that block, every number in it would have fitted: subtracting 270000 from
the initial `n<100000` is impossible. Thus the remainder becomes less
than 45 before leaving the block. It never increases afterwards.
When the scan finally reaches the still-unused digits `9,8,…,1`, they
can greedily form every remainder from 0 to 45. At digit `d`, maintain
`remainder≤d(d+1)/2`; taking `d` when it fits preserves the corresponding
bound for `d−1`. The remainder ends at zero. Therefore −1 is never needed.

All five simple algorithms remain available. C++ only receives exact
repository formatting, with its own new Accepted and metrics; the other
four source files remain byte-exact, and original C++ bytes are backed up.

## Optimized solutions

The new construction avoids the full digit-sum table and long scan.
While the remainder exceeds 45, take consecutive numbers starting at
99999 and subtract their digit sums, computed on demand. A five-digit
number contributes at most 45, so each selection fits. The 270000 block
bound proves this phase stops before reaching 90000, far from the small
digits. Finish the remaining value greedily using distinct digits 9 to 1.
The two phases have disjoint ranges; the preceding remainder invariant
proves the exact target sum. Any such set is accepted; minimizing its
size is not required.

For `D` decimal digits per large value and `q` output values, work is
`O(qD+D)`, storage `O(q)` for the output; here `D=5`, hence `O(q)` work.
There is no `O(L)` preprocessing table. This is a different construction,
named `constructive` rather than an `_optimized` clone of the greedy scan.
All five versions meet the 30% rule by measured memory savings against
their current same-language bases. Python's recorded time rises from
0.093 s to 0.109 s; its admission is by memory, not speed. Rust's
0.046→0.031 s change is one timer tick and is not used as speed evidence.

Measured memory reductions: C++ 66.4%, Go 43.9%, Java 61.9%, Python 43.0%, Rust 76.6%.

## Language notes

Accepted metrics below belong to exact source bytes. All comparisons
use current simple bases, including the newly accepted C++ formatting.
The 2 November 2026 ranking snapshot uses the agreed current-compiler and
other-author filters: C++ targets top15% or the first ten places in both
metrics; the other families target first in both. A starred admitted
source remains useful despite missing that ranking goal. Empty competitor
samples provide formal coverage, not evidence of competitive superiority.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1727_greedy.cpp](1727_greedy.cpp) | G++ 13.2 x64 | greedy | O(L) | AC | 0.015 s | 596 KB | 11308491 |
| [1727_greedy.go](1727_greedy.go) | Go 1.14 x64 | greedy | O(L) | AC | 0.031 s | 2268 KB | 11289382 |
| [1727_greedy.java](1727_greedy.java) | Java 1.8 | greedy | O(L) | AC | 0.125 s | 2196 KB | 11289385 |
| [1727_greedy.py](1727_greedy.py) | Python 3.12 x64 | greedy | O(L) | AC | 0.093 s | 1636 KB | 11289384 |
| [1727_greedy.rs](1727_greedy.rs) | Rust 1.75 x64 | greedy | O(L) | AC | 0.046 s | 1096 KB | 11289388 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1727_constructive.cpp](1727_constructive.cpp) | G++ 13.2 x64 | constructive | O(qD + D) | AC | 0.015 s | 200 KB | 11308058 |
| [1727_constructive.go](1727_constructive.go) | Go 1.14 x64 | constructive | O(qD + D) | AC | 0.031 s | 1272 KB | 11308060 |
| [1727_constructive.java](1727_constructive.java) | Java 1.8 | constructive | O(qD + D) | AC | 0.109 s | 836 KB | 11308061 |
| [1727_constructive.py](1727_constructive.py) | Python 3.12 x64 | constructive | O(qD + D) | AC | 0.109 s | 932 KB | 11308057 |
| [1727_constructive.rs](1727_constructive.rs) | Rust 1.75 x64 | constructive | O(qD + D) | AC | 0.031 s | 256 KB | 11308062 |
