# 1413. Mars Jumper

[Timus 1413](https://acm.timus.ru/problem.aspx?space=1&num=1413) · difficulty 180 · simulation

Original problem by Stanislav Vasiliev, from the Ural State University Championship, October 29, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A rover is driven from a numeric keypad: every key from 1 to 9 except 5
makes a jump of exactly one metre in the direction of that key from the
centre 5 (8 is north, 6 east, 9 north-east and so on), 5 takes a soil
sample and 0 makes the rover destroy itself. Given up to 10⁶ key
presses, print where the rover ends: at the first 0, or after the last
key if there is no 0. The answer is the shift east and north, with an
absolute or relative error of at most 10⁻¹⁰.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

The digits of the key presses.

## Output

X and Y, the shift east and north.

## Checking

Repository tests compare numeric tokens with |actual-reference| <= 0.0000000002·max(1,|reference|), reject nonfinite values, and compare nonnumeric tokens exactly.

## Examples

### Example 1

Input:

```
1236987412369870234567890123456789
```

Output:

```
1.0000000000 0.0000000000
```

## Solution

Count how many times each key was pressed before the first 0. A
straight jump moves one axis by a whole metre and a diagonal one moves
both axes by 1/√2, so the end point is (straight sum) + (diagonal sum)
/ √2 on each axis, computed from integer sums. Counting avoids rounding
at every jump, but the final floating-point multiplication, addition
and ten-decimal output still round; the absolute error can slightly
exceed 10⁻¹⁰. `O(n)`.

Pitfalls:

- keys after the first 0 must be ignored (tests 01, 05, gen2);
- a diagonal jump is one metre long, not √2 (test 04);
- diagonal coordinates are irrational, so counting does not make the
  final coordinates exact (test 04);
- reading a million characters with a slow input call for each one can
  take a large part of the 0.5 seconds, so the solutions read whole
  tokens, lines or the whole input at once.

## Optimized solutions

`1413_simulation_optimized.java`. Java keeps integer counts of keypad directions and stops at the first zero, reading 4096-byte blocks. Each coordinate is straight+diagonal/sqrt(2). It represents the diagonal coefficient by C/10^18 with C=707106781186547524=floor(10^18/sqrt(2)), then emits eighteen fractional digits using integer arithmetic. Splitting C into 707106781*10^9+186547524 keeps products in long; floorDiv/floorMod preserve signs and borrows even near zero. With at most 10^6 moves, coefficient error contributes less than 1e-12, below the required 1e-10; no double conversion is used. The coefficient is a defined mathematical constant, not stored answers. Time O(I) for bytes read, fixed auxiliary storage. The short floating-point base remains.

Exact-source Java 1.8 Accepted #11327528: 0.093 s / 376 KB. Saved 2026-11-20 compiler-cohort comparison: time 3/49, memory 1/49. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11307336 was 0.109 s / 936 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1413_simulation_optimized.java`: 0.093 s / 376 KB; retained teaching base `1413_simulation.java`: 0.093 s / 5804 KB.

The optimized Go solution counts the keys in a reusable 4 KB buffer
instead of reading all the up to 10⁶ keys into memory at once:
{1413_simulation_optimized.go}.

The optimized Python solution reads the input in 8 KB chunks and counts
the digits of each chunk with `bytes.count`, instead of reading all the
up to 10⁶ keys into memory at once; after the first 0 the rest of the
input is read but not counted: {1413_simulation_optimized.py}.

The optimized Rust solution counts the keys in a reusable 4 KB buffer
instead of reading all the up to 10⁶ keys into a vector at once:
{1413_simulation_optimized.rs}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1413_simulation_optimized.go`: time reduction +0.00%; memory
  reduction +68.46%; base: `1413_simulation.go`.

- `1413_simulation_optimized.py`: time reduction +16.13%; memory
  reduction +82.94%; base: `1413_simulation.py`.

- `1413_simulation_optimized.rs`: time reduction +0.00%; memory
  reduction +88.58%; base: `1413_simulation.rs`.

`1413_simulation_optimized.cpp`. Count direction keys in reusable 8 KB blocks and stop counting at the first zero. Keep the nine counters and combine integer axis and diagonal contributions only once; the diagonal scale is sqrt(1/2). Time is O(n), auxiliary space O(1); no full input string is retained.

Compared with `1413_simulation.cpp`: time 0.015 s → 0.015 s; memory 1832 KB → 92 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1413_simulation.cpp](1413_simulation.cpp) | G++ 13.2 x64 | simulation | O(n) | AC | 0.015 s | 1832 KB | 11307301 |
| [1413_simulation.go](1413_simulation.go) | Go 1.14 x64 | simulation | O(n) | AC | 0.015 s | 3196 KB | 11286093 |
| [1413_simulation.java](1413_simulation.java) | Java 1.8 | simulation | O(n) | AC | 0.093 s | 5804 KB | 11307330 |
| [1413_simulation.py](1413_simulation.py) | Python 3.12 x64 | simulation | O(n) | AC | 0.093 s | 3072 KB | 11286094 |
| [1413_simulation.rs](1413_simulation.rs) | Rust 1.75 x64 | simulation | O(n) | AC | 0.015 s | 2136 KB | 11286097 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1413_simulation_optimized.go](1413_simulation_optimized.go) | Go 1.14 x64 | simulation | O(n) | AC | 0.015 s | 1008 KB | 11307331 |
| [1413_simulation_optimized.java](1413_simulation_optimized.java) | Java 1.8 | simulation | O(I) time; O(1) auxiliary space | AC | 0.093 s | 376 KB | 11327528 |
| [1413_simulation_optimized.py](1413_simulation_optimized.py) | Python 3.12 x64 | simulation | O(n) | AC | 0.078 s | 524 KB | 11307334 |
| [1413_simulation_optimized.rs](1413_simulation_optimized.rs) | Rust 1.75 x64 | simulation | O(n) | AC | 0.015 s | 244 KB | 11307332 |
| [1413_simulation_optimized.cpp](1413_simulation_optimized.cpp) | G++ 13.2 x64 | simulation | O(n) | AC | 0.015 s | 92 KB | 11326635 |
