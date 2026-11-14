# 1448. Lighting in Hogwarts

[Timus 1448](https://acm.timus.ru/problem.aspx?space=1&num=1448) · difficulty 580 · constructive

Original problem by Alexander Mironenko (idea) and Stanislav Vasiliev (text and programming), from the Tenth Ural Collegiate Team Programming Championship, March 24–25, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A corridor has N lamps in a row (1 ≤ N ≤ 10⁶), each fully on or off.
Argus Filch wants brightness b percent (0 ≤ b ≤ 100) spread as evenly as
possible: print a row of N digits 0 and 1 such that on every stretch of
L consecutive lamps the number of lamps on differs from L b / 100 by at
most 2.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

N, then b.

## Output

The row of lamps. Any fitting row is accepted.

## Examples

### Example 1

Input:

```
10
33
```

Output:

```
0100100100
```

## Solution

Turn lamp i (counting from 0) on exactly when ⌊(i + 1) b / 100⌋ is
larger than ⌊i b / 100⌋. Then the lamps on among the first k number
⌊k b / 100⌋, so a stretch from l to r holds ⌊r b / 100⌋ − ⌊l b / 100⌋
lamps, which differs from (r − l) b / 100 by less than 1, well within
the allowed 2. The pattern repeats every 100 lamps, since adding 100 to
i adds exactly b to both floors. `O(N)`.

Pitfalls:

- b = 0 and b = 100 give rows of identical digits (tests 02, 03, 05, gen1,
  gen2);
- buffer output for up to a million digits to avoid per-digit calls
  (gen1 to gen7);
- the row of the example is only one of many valid answers.

## Optimized solutions

The C++ variant generates one period using a running remainder modulo 100. It copies that
period into a fixed buffer whose length is a multiple of 100, then writes as many full
blocks as needed and a final prefix. This gives the same sequence in O(N) time with O(1)
extra memory. Submission 11316954 used 112 KB versus 1164 KB for the base, both at 0.0151144 KB for the base, both at 0.015 s.

Go fills the fixed output block by doubling the already generated prefix with `copy`. Submission 11317198 took 0.015 s and used 924 KB, versus 0.031 s and 2056 KB for the base.

Java repeats the period with `System.arraycopy` and writes fixed-size blocks directly to the output stream. Submission 11317199 used 364 KB versus 3036 KB for the base, both at 0.1253076 KB for the base, both at 0.109 s.

Python repeats a 100-lamp period to form a fixed-size byte block, then writes the complete blocks and the final prefix. Submission 11317212 used 432 KB versus 2244 KB for the base, both at 0.0782276 KB for the base, both at 0.078 s.

Rust fills a fixed-size block by doubling the 100-lamp period and writes the full blocks and final prefix. Submission 11317214 used 204 KB and took 0.046 s, versus 2048 KB and 0.031 s for the base.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11322145 · Go 1.14 x64 №11322146 · Java 1.8 №11322147 · Python 3.12 x64 №11322148 · Rust 1.75 x64 №11322149.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1448_constructive.cpp](1448_constructive.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 1144 KB | 11322145 |
| [1448_constructive.go](1448_constructive.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.031 s | 2056 KB | 11322146 |
| [1448_constructive.java](1448_constructive.java) | Java 1.8 | constructive | O(N) | AC | 0.125 s | 3076 KB | 11322147 |
| [1448_constructive.py](1448_constructive.py) | Python 3.12 x64 | constructive | O(N) | AC | 0.078 s | 2276 KB | 11322148 |
| [1448_constructive.rs](1448_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.031 s | 2048 KB | 11322149 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1448_constructive_optimized.cpp](1448_constructive_optimized.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 112 KB | 11316954 |
| [1448_constructive_optimized.go](1448_constructive_optimized.go) \* | Go 1.14 x64 | constructive | O(N) | AC | 0.015 s | 924 KB | 11317198 |
| [1448_constructive_optimized.java](1448_constructive_optimized.java) | Java 1.8 | constructive | O(N) | AC | 0.109 s | 364 KB | 11317199 |
| [1448_constructive_optimized.py](1448_constructive_optimized.py) | Python 3.12 x64 | constructive | O(N) | AC | 0.078 s | 432 KB | 11317212 |
| [1448_constructive_optimized.rs](1448_constructive_optimized.rs) \* | Rust 1.75 x64 | constructive | O(N) | AC | 0.046 s | 204 KB | 11317214 |

\* The saved rating has no comparable Go submissions from other authors. Rust ranks second by time and first by memory in the saved rating. It meets the memory improvement criterion.
