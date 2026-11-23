# 1493. One Step from Happiness

[Timus 1493](https://acm.timus.ru/problem.aspx?space=1&num=1493) · difficulty 47 · implementation

Original problem by Vladimir Yakovlev, from the Thirteenth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 14, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A ticket has a six-digit number, leading zeros included; it is lucky if
its first three digits and its last three digits have equal sums. The
given ticket's two sums differ by exactly one. Print "Yes" if the
previous or the next ticket is lucky, and "No" otherwise.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The six digits of the ticket.

## Output

"Yes" or "No".

## Examples

### Example 1

Input:

```
715068
```

Output:

```
Yes
```

### Example 2

Input:

```
445219
```

Output:

```
No
```

### Example 3

Input:

```
012200
```

Output:

```
Yes
```

## Solution

Check the two neighbours directly: take the number minus one and plus
one, write each with six digits, and compare the sums of the halves.
The sums of the given ticket differ, so it is neither 000000 nor 999999,
and both neighbours are real tickets. Carries can change several digits
at once, which is why the neighbours are recomputed rather than
adjusted by one digit. `O(1)`.

Pitfalls:

- the number may start with zeros, and they still count as digits
  (test 03); a reader that treats a leading 0 as octal breaks it;
- a carry or a borrow across the middle changes both halves, as from
  100000 to 099999 (tests 06, 08, 09);
- the neighbours 000000 and 999999 are lucky tickets too (tests 04, 05).

## Optimized solutions

The optimized solutions (Java, Rust) check the same two neighbours
without the range check: the ticket is neither 000000 nor 999999, so
both neighbours are tickets. Rust writes the answer as a byte string
with `write_all`: 0.031 s instead of 0.062 s, with the same memory.

The optimized Java solution parses the six digits byte by byte from
`System.in` instead of using `Scanner`: 0.078 s instead of 0.140 s and
308 KB instead of 1596 KB.

Calculate the digit sums by division and remainders, without constructing decimal strings for the neighbours. Accepted submission 11302025 took 0.078 s and used 372 KB. The simple version took 0.062 s and used 376 KB. The recorded runtime is higher than for the simple version.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1493_math_parsing_optimized.go`. Compute the digit sums of both three-digit halves once. Update the neighboring sums with exact carry/borrow counts and guard the six-digit endpoints, avoiding two repeated full neighbor digit sums. Specialize token conversion and numeric output to the types actually used, removing unused generic branches while retaining the algorithm and comments.

Accepted #11329147 (Go 1.14 x64): **0.015 s / 792 KB**. Archived comparison: `1493_implementation.go` (Go 1.14 x64) — 0.031 s / 1064 KB (#11287207).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1493_implementation.cpp](1493_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 124 KB | 11287206 |
| [1493_implementation.go](1493_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1064 KB | 11287207 |
| [1493_implementation.java](1493_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.140 s | 1596 KB | 11287209 |
| [1493_implementation.py](1493_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.062 s | 376 KB | 11287208 |
| [1493_implementation.rs](1493_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.062 s | 224 KB | 11287210 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1493_implementation_optimized.java](1493_implementation_optimized.java) | Java 1.8 | implementation | O(1) | AC | 0.078 s | 308 KB | 11303750 |
| [1493_implementation_optimized.rs](1493_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.031 s | 224 KB | 11303611 |
| [1493_implementation_optimized.py](1493_implementation_optimized.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.078 s | 372 KB | 11302025 |
| [1493_math_parsing_optimized.go](1493_math_parsing_optimized.go) | Go 1.14 x64 | math, parsing | O(1) | AC | 0.015 s | 792 KB | 11329147 |
