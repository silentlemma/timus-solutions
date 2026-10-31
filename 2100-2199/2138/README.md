# 2138. Swapping the byte order of a 32-bit number

[Timus 2138](https://acm.timus.ru/problem.aspx?space=1&num=2138) · difficulty 111 · math

Original problem by Aidar Islamov, from the Ural Team Programming Contest 2019.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A number up to 2³² − 1 is sent as four base-256 digits. "Good" computers
read the digits from the most significant one, "bad" computers from the
least significant one. A computer of one type received a number from a
computer of the other type and read it as v. Print the number that was
actually sent. The limits are 0.5 seconds and 256 MB.

## Input

The sender type, GOOD or BAD, and then v, 0 ≤ v ≤ 4 294 967 295.

## Output

The number that was sent.

## Examples

### Example 1

Input:

```
GOOD
16777216
```

Output:

```
1
```

### Example 2

Input:

```
BAD
1000
```

Output:

```
3892510720
```

## Solution

Whichever side is the sender, the receiver reads the same four digits in
the opposite order. So the answer is v with its four base-256 digits
reversed, and the sender type does not matter. Take the digits of v from
the lowest one with % 256 and / 256 and build the result from the top,
or use a byte swap.

In the first example 16 777 216 has the digits 1;0;0;0, and reversed
they give 1.

## Optimized solutions

The optimized Java solution reads the input byte by byte straight from
`System.in` instead of creating a `Scanner`, and since GOOD and BAD
contain no digits it simply collects every digit it meets into v, a
`long`, which holds any value up to 2³² − 1: {2138_math_optimized.java}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `2138_math_optimized.java`: time reduction +0.00%; memory reduction
  +78.23%; base: `2138_math.java`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [2138_math.cpp](2138_math.cpp).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2138_math.cpp](2138_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 132 KB | 11304054 |
| [2138_math.go](2138_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1068 KB | 11294918 |
| [2138_math.java](2138_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 1580 KB | 11304060 |
| [2138_math.py](2138_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 424 KB | 11294919 |
| [2138_math.rs](2138_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 236 KB | 11294921 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2138_math_optimized.java](2138_math_optimized.java) \* | Java 1.8 | math | O(1) | AC | 0.109 s | 344 KB | 11304333 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
