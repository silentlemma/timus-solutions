# 1048. Adding two numbers of a million digits

[Timus 1048](https://acm.timus.ru/problem.aspx?space=1&num=1048) · difficulty 201 · implementation

Original problem by Stanislav Vasiliev and Alexander Klepinin, from the Ural State University Collegiate Programming Contest, March 25, 2000.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two positive integers have `N` digits each (`1 ≤ N ≤ 10^6`, leading zeros
allowed), and their sum also fits in `N` digits. They are given in
columns: line `i` holds the `i`-th digit of each number. Print the sum as
exactly `N` digits.

Time limit: 2 seconds. Memory limit: 16 MB.

## Input

`N`, then `N` lines with two digits separated by a space.

## Output

The `N` digits of the sum on one line.

## Checking

Output is compared token by token and contains exactly `N` digits.
The actual Python candidate was checked on 610 additions: 600 random
positive operands of up to 300 digits against arbitrary-precision integer
addition, and ten analytic carry/leading-zero cases at lengths
2, 3, 31, 1000 and 1000000. The long carry case propagates through the
whole number; the other extreme preserves many leading zeros. Inputs
respect the no-overflow promise, and the million-digit expectations do
not rely on converting those operands to integers. The actual Python
and Rust candidates each passed 14 repository inputs in Docker and
received their own exact-source Accepted. The 610 oracle executions
were Python runs, not 610 runs of every compiled language.

## Examples

### Example 1

Input:

```
4
0 4
4 2
6 8
3 7
```

Output:

```
4750
```

### Example 2

Input:

```
3
0 0
4 5
5 5
```

Output:

```
100
```

## Solution

Add columns from right to left. For column sum `s` and incoming
carry `c`, write `(s + c) mod 10` and pass `(s + c) div 10` to the left.
Initially the carry is zero. Since `0 ≤ s ≤ 18`, every carry is 0 or 1
and the temporary value is at most 19. Inductively the processed suffix
contains exactly the low digits of its sum, with the remaining carry
passed left. The promise that the sum fits `N` digits makes the final
carry zero. Keep all `N` digits, including leading zeros; do not strip
them or output an extra carry digit.

The native bases store column sums in bytes and reuse that array for
output. The last byte of their `N + 1` buffer holds the newline, not
an extra leading digit. Python's readable base instead reads the input,
removes whitespace, separates two operand byte strings, and runs the
same reverse carry loop. Rust's base retains the whole input as well
as its column-sum/output array. All versions use `O(N)` time and space.
All five original Accepted bases are preserved unchanged.

## Optimized solutions

The new Python and Rust programs discard input while reading,
retaining only the column sums `0..18` in one `N + 1` byte buffer.
Their reverse carry pass overwrites these bytes with ASCII answer digits;
the final byte remains a newline. Separate operand arrays and the full
input are unnecessary: addition depends on each digit pair only through
its sum. The buffer itself uses `N + 1` bytes, excluding runtime and
I/O buffers. Time and space remain `O(N)`; this is a storage and I/O
optimization of the same schoolbook algorithm, hence `_optimized`.

Python reads the stated digit-pair lines one at a time; Rust filters
ASCII digits from a locked input stream after reading `N`. Both write
the completed byte buffer directly, without converting either million-
digit operand to a single integer.

Python's exact-source Accepted is 0.593 s / 1392 KB versus the base's
0.406 s / 10360 KB: 86.6% less memory, but 46.1% more recorded time.
Rust is 0.046 s / 1144 KB versus 0.015 s / 10248 KB: 88.8% less memory,
but higher recorded time. Both qualify by memory, not by speed.
The simpler, faster recorded bases remain available.

## Language notes

Snapshot: 2 November 2026. Original C++ has time place 1 and memory
place 5 against 234 filtered other-author entries; Java is first in
both against six. Go's filtered sample is empty, so its formal coverage
is not competitive proof. Optimized Rust is first in both against one
entry. Optimized Python has places 7 and 1 against eight entries and
keeps a star: the agreed profile requires C++ top 15% or first 10 places
in both metrics, and first in both for the other language families.
The Python memory gain still satisfies admission independently of ranking.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1048_implementation.cpp](1048_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 1184 KB | 11278646 |
| [1048_implementation.go](1048_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.062 s | 1976 KB | 11278650 |
| [1048_implementation.java](1048_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.140 s | 2080 KB | 11278656 |
| [1048_implementation.py](1048_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.406 s | 10360 KB | 11278662 |
| [1048_implementation.rs](1048_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 10248 KB | 11278658 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1048_implementation_optimized.py](1048_implementation_optimized.py) \* | Python 3.12 x64 | implementation | O(N) | AC | 0.593 s | 1392 KB | 11308404 |
| [1048_implementation_optimized.rs](1048_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.046 s | 1144 KB | 11308405 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
