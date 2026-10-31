# 1576. Telephone Tariffs

[Timus 1576](https://acm.timus.ru/problem.aspx?space=1&num=1576) · difficulty 147 · implementation

Original problem: folklore, from the USU Junior Contest (the Fourteenth Open Team Programming Contest for Schoolchildren of the Sverdlovsk Region), October 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Three tariffs: basic, a fee N1 plus C1 per minute; combined, a fee N2
that includes T minutes, plus C2 for each minute over T; unlimited, a
fee N3. Calls of at most 6 seconds are free, and longer calls are
rounded up to whole minutes. Given up to 1000 calls as mm:ss, print the
monthly bill under each tariff.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N1 and C1, then N2, T and C2, then N3, all integers from 1 to 1000,
then K (1 ≤ K ≤ 1000) and the K call lengths as mm:ss, where
0 ≤ mm, ss ≤ 59.

## Output

Three lines in the format of the examples.

## Examples

### Example 1

Input:

```
135 1
220 10 1
300
5
00:05
00:10
09:59
07:00
01:01
```

Output:

```
Basic:     155
Combined:  230
Unlimited: 300
```

### Example 2

Input:

```
10 2
100 1 1
1000
1
03:00
```

Output:

```
Basic:     16
Combined:  102
Unlimited: 1000
```

## Solution

Add up the paid minutes: a call of s seconds adds nothing when s ≤ 6
and ⌈s / 60⌉ otherwise. With M minutes the bills are N1 + C1·M,
N2 + C2·max(0, M − T) and N3. They stay below 7·10⁷. `O(K)`.

Pitfalls:

- a call of exactly 6 seconds is free, one of 7 seconds costs a whole
  minute, and a call of exactly one minute costs one (test 03);
- the combined tariff charges nothing extra while the minutes stay
  within T, so the overage is never negative;
- the labels are padded to the same width: `Basic:` with five spaces,
  `Combined:` with two, `Unlimited:` with one.

## Optimized solutions

The optimized Java solution parses the numbers by hand from a 4 KB
buffer filled from `System.in` instead of creating a `Scanner`, so the
JVM does not load the scanner and its regular expressions. It reads a
call as two numbers, the colon ending the minutes, instead of splitting
a `String` at `:`, and reads the tariff numbers as `int`, which holds
values up to 1000, before the same `long` arithmetic:
{1576_implementation_optimized.java}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1576_implementation_optimized.java`: time reduction -14.68%; memory
  reduction +83.24%; base: `1576_implementation.java`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1576_implementation.cpp](1576_implementation.cpp).
- [1576_implementation.go](1576_implementation.go).
- [1576_implementation.rs](1576_implementation.rs).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1576_implementation.cpp](1576_implementation.cpp) | G++ 13.2 x64 | implementation | O(K) | AC | 0.015 s | 132 KB | 11287847 |
| [1576_implementation.go](1576_implementation.go) | Go 1.14 x64 | implementation | O(K) | AC | 0.015 s | 1168 KB | 11287851 |
| [1576_implementation.java](1576_implementation.java) | Java 1.8 | implementation | O(K) | AC | 0.109 s | 2244 KB | 11287858 |
| [1576_implementation.py](1576_implementation.py) | Python 3.12 x64 | implementation | O(K) | AC | 0.078 s | 508 KB | 11287853 |
| [1576_implementation.rs](1576_implementation.rs) | Rust 1.75 x64 | implementation | O(K) | AC | 0.015 s | 232 KB | 11287860 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1576_implementation_optimized.java](1576_implementation_optimized.java) | Java 1.8 | implementation | O(K) | AC | 0.125 s | 376 KB | 11304530 |
