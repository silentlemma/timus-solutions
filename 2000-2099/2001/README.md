# 2001. Mathematicians and Berries

[Timus 2001](https://acm.timus.ru/problem.aspx?space=1&num=2001) · difficulty 22 · math

Original problem by Oleg Merkurev. (Prepared by Kirill Devyatkin), from the Ural Regional School Programming Contest 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two baskets are weighed three times. Initially each contains its own
berries. Next all berries from the second basket are transferred into
the first, and both baskets are weighed. Finally all berries in the
first are moved into the second, and both are weighed again. Recover the
original berry mass in each basket; the baskets themselves keep their
mass throughout.

## Input

Three pairs `a1 b1`, `a2 b2`, `a3 b3`, in chronological order. Each
reading is an integer from 0 to 10000. The readings describe the stated
transfers. Time 0.5 seconds, memory 64 MB.

## Output

The original mass of berries in the first and second basket, in that order.

## Checking

Outputs are compared token by token.

## Examples

```
1 2
2 1
0 3
```

```
1 1
```

The first basket is empty at the last weighing, so its own mass is 0.
The second is empty at the middle weighing, so its own mass is 1.
Subtracting these from the initial readings 1 and 2 gives 1 and 1.

## Solution

Let the empty baskets weigh c and d and the berries x and y. The first
weighing gives a1 = c + x and b1 = d + y. After the second basket is
emptied into the first, b2 = d; after the first is emptied into the
second, a3 = c. So x = a1 − a3 and y = b1 − b2; the readings a2 and b3
are not needed. `O(1)`.

## Optimized solutions

`2001_math_optimized.java`. Keep the two exact differences a1−a3 and b1−b2 after reading all six values. O(1) arithmetic and fixed buffers. All numeric fields used by the computation are consumed before output. Reuse one 256-byte array for input and then output, reserving twelve bytes per signed int; reverse only its newly written digits. This removes separate input/output/digit arrays without overwriting any value still needed by the algorithm. Time for parsing/output is linear in consumed bytes; buffer storage is fixed.

Exact-source Java 1.8 Accepted #11327769: 0.078 s / 364 KB. Saved 2026-11-20 compiler-cohort comparison: time 3/1109, memory 7/1109. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11303655 was 0.125 s / 344 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `2001_math_optimized.java`: 0.078 s / 364 KB; retained teaching base `2001_math.java`: 0.156 s / 1608 KB.

Historical previous-revision description and measurements: The optimized solutions (C++, Java) compute the same two differences.
C++ skips the readings a2 and b3 with `%*d` in `scanf` instead of using
`iostream`: 124 KB instead of 396 KB, with the same time. Java parses
the numbers by hand from `System.in` instead of using `Scanner`: 0.125 s
instead of 0.156 s and 344 KB instead of 1608 KB.

Read the six values with a byte buffer and write the two differences directly. Accepted submission 11301801 took 0.015 s and used 916 KB. The simple version took 0.031 s and used 1088 KB.

Parse all six values from bytes and unpack only the four used for the two differences. Accepted submission 11301805 took 0.078 s and used 364 KB. The simple version took 0.093 s and used 384 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [2001_math.cpp](2001_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 396 KB | 11292438 |
| [2001_math.go](2001_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1088 KB | 11292439 |
| [2001_math.java](2001_math.java) | Java 1.8 | math | O(1) | AC | 0.156 s | 1608 KB | 11303362 |
| [2001_math.py](2001_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 384 KB | 11292440 |
| [2001_math.rs](2001_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 228 KB | 11292442 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [2001_math_optimized.cpp](2001_math_optimized.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 124 KB | 11303653 |
| [2001_math_optimized.java](2001_math_optimized.java) \* | Java 1.8 | math | O(1) | AC | 0.078 s | 364 KB | 11327769 |
| [2001_math_optimized.go](2001_math_optimized.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 916 KB | 11301801 |
| [2001_math_optimized.py](2001_math_optimized.py) \* | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 364 KB | 11301805 |

\* Accepted; the separate rating target is not yet met: C++ requires top ten or top 15% in both time and memory, and the other language families require first place in both. This marker is separate from the admission criteria; the version may be optimized further.
