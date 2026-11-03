# 1537. Ents

[Timus 1537](https://acm.timus.ru/problem.aspx?space=1&num=1537) · difficulty 283 · dp

Original problem by Sergey Pupyrev, from the Eighth Ural State University Open Personal Contest, March 3, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The first ent learns two words. Every ent who has learned w words teaches
them to one old and one young ent who cannot speak yet; then the elves
teach the old one one more word, so it ends with w + 1 words, and the
young one w more, so it ends with 2w. This goes on forever. Count the
ents who know exactly K words, modulo P (K ≤ 10⁷, P ≤ 10⁹).

Time limit: 1 second. Memory limit: 64 MB.

## Input

K and P.

## Output

The number of ents who know exactly K words, modulo P.

## Checking

Compare the complete output exactly, including spaces and line breaks.

## Examples

### Example 1

Input:

```
4 10
```

Output:

```
2
```

## Solution

Let f(w) be the number of ents who know w words. Every ent but the first
was taught by one parent, as its old pupil (w − 1 words) or its young one
(w / 2 words, only for even w), so f(2) = 1 and
f(w) = f(w − 1) + f(w / 2) for even w, f(w) = f(w − 1) for odd w. An odd
w adds nothing, so g(m) = f(2m) = f(2m + 1) satisfies g(1) = 1 and
g(m) = g(m − 1) + g(⌊m / 2⌋), and the answer is g(⌊K / 2⌋), or 0 for
K = 1. If B(n) counts partitions of n into powers of two, then
g(m) = B(2m) / 2 for m ≥ 1. These counts grow too large to keep exactly,
so the recurrence is evaluated modulo P.

One pass over m up to K / 2 = 5·10⁶ does it; only the values up to K / 4
are looked up again, so only those are stored (an array of 2.5·10⁶
numbers). A sum of two residues is at most 2(P − 1) ≤ 1,999,999,998,
which fits a signed 32-bit integer; the compiled solutions use 64-bit sums.
`O(K)` time and `O(K)` space.

Pitfalls:

- K = 1: nobody knows one word (test 02);
- P = 1 makes every answer 0 (test 04);
- reduce each sum modulo P: the exact counts grow beyond fixed-width
  integers, although each sum of two residues fits 32 bits (tests 06, 07);
- g(m) is half of B(2m): for K = 4, the answer is 2, while B(4) = 4
  (test 01);
- Python runs under PyPy: K = 10⁷ takes about 0.8 s with CPython and
  about 0.17 s with PyPy.

## Optimized solutions

Use the same recurrence, but sum the final range algebraically rather than evaluating every remaining DP state. Only an earlier prefix must be computed, and only its smaller initial portion must remain stored. Packed 32-bit residues replace 64-bit cells; the modulus bound makes every residue fit. The derivation of the even and odd endpoints preserves all base cases. The accepted Python implementation uses CPython; compare its recorded result with the actual interpreter of the retained simple source.

```text
T = floor(K/2), H = floor(T/2), D = floor(H/2)
g(0) = 0, g(1) = 1
S = sum(g(j), D < j <= H)
For H >= 1:
  g(2H) = 2S + [H is even] * g(D)
  g(2H+1) = g(2H) + g(H)
answer = g(T) mod P
```

- `1537_dp_optimized.py`: 0.656 s / 5276 KB; base `1537_dp.py`: 0.203 s / 20812 KB; relative change: time +223.2%, memory -74.6%.

## Language notes

The saved rating snapshot is from 1–2 November 2026. C++ requires the top 15% or the first 10 places in both time and memory; other families require first place in both. Equal results share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `1537_dp.cpp`; covering source `1537_dp.cpp`; time/memory places 6/1, other-author entries 75/75.

- Go: preferred teaching base `1537_dp.go`; covering source `1537_dp.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1537_dp.java`; covering source `1537_dp.java`; time/memory places 1/1, other-author entries 10/10.

- Python/PyPy: preferred teaching base `1537_dp.py`; covering source `1537_dp_optimized.py`; time/memory places 2/1, other-author entries 1/1.

- Rust: preferred teaching base `1537_dp.rs`; covering source `1537_dp.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

The simple table includes the preferred teaching sources and preserved Accepted alternatives. The language notes identify the preferred base for each family.

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1537_dp.cpp](1537_dp.cpp) | G++ 13.2 x64 | dp | O(K) | AC | 0.046 s | 9684 KB | 11287481 |
| [1537_dp.go](1537_dp.go) | Go 1.14 x64 | dp | O(K) | AC | 0.109 s | 11700 KB | 11287482 |
| [1537_dp.java](1537_dp.java) | Java 1.8 | dp | O(K) | AC | 0.140 s | 11368 KB | 11287485 |
| [1537_dp.py](1537_dp.py) | PyPy 3.10 x64 | dp | O(K) | AC | 0.203 s | 20812 KB | 11287484 |
| [1537_dp.rs](1537_dp.rs) | Rust 1.75 x64 | dp | O(K) | AC | 0.046 s | 9836 KB | 11287488 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1537_dp_optimized.py](1537_dp_optimized.py) \* | Python 3.12 x64 | dp | O(K) | AC | 0.656 s | 5276 KB | 11309315 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
