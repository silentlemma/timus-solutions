# 1001. Square roots in reverse order

[Timus 1001](https://acm.timus.ru/problem.aspx?space=1&num=1001) · difficulty 14 · math

Original problem prepared by Dmitry Kovalev.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The input is a sequence of integers `A1, A2, ..., An` with `0 ≤ Ai ≤ 10^18`.
Print their square roots in reverse order: `√An` first, `√A1` last.

The count `n` is not given: the numbers continue up to the end of the input,
whose total size is at most 256 KB (so `n` is at most about 131 000).

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

The integers `Ai`, separated by any number of spaces and line breaks
(including empty lines).

## Output

`n` lines: `√An, √An-1, ..., √A1`, one per line, each with at least four digits
after the decimal point.

## Checking

Each square root must be printed with at least four digits after the decimal
point.

## Examples

### Example 1

Input:

```
  16   2

 1000000000000000000   
0
```

Output:

```
0.0000
1000000000.0000
1.4142
4.0000
```

### Example 2

Input:

```
7
```

Output:

```
2.6458
```

## Solution

Read all numbers up to the end of the input into an array, then walk it
backwards and print `sqrt(Ai)` with four decimals. Time and memory are `O(n)`.

A double-precision `sqrt` is accurate enough: converting a value up to `10^18`
to a double loses at most a relative `2^-53`, so the root (at most `10^9`) is
off by less than `10^-6`, far below `10^-4` (four decimal places).

Pitfalls:

- the count is not given, so read until the end of the input;
- the separators are arbitrary: several spaces, line breaks, empty lines;
- the values do not fit in 32 bits: use 64-bit integers;
- up to about 131 000 output lines: the output must be buffered.

## Optimized solutions

The optimized solutions (C++, Go, Java, Rust) keep the input as text
instead of an array of numbers. C++, Go and Java read it into one buffer
and parse the numbers from its end backwards, which is exactly the order
of the output; Rust walks the tokens of the text in reverse. The root is
printed by hand: multiplied by `10^4`, rounded, and written as the integer
part and four digits of the fraction, without the slow formatting of
floating-point numbers. Instead of an array of up to 131 000 numbers only
the 256 KB of input stay in memory. C++: 0.031 s instead of 0.125 s and
356 KB instead of 1576 KB; Go: 0.015 s instead of 0.125 s and 1180 KB
instead of 6588 KB; Java: 0.125 s instead of 0.593 s and 872 KB instead
of 11728 KB; Rust: 0.015 s instead of 0.046 s and 464 KB instead of
3072 KB.

The optimized Python solution writes the answers in blocks from the end
of the input: it cuts about 4 KB of numbers at a time, at a separator,
so the list of all square roots is never built at once: 2052 KB instead
of 11492 KB, although the time grows from 0.125 s to 0.156 s.

## Language notes

- **C++**: the simple solution uses `scanf("%llu")` in a loop and
  `printf("%.4f\n")`.
- **Go**: the simple solution reads with `fmt.Fscan` over a
  `bufio.Reader` and writes with `fmt.Fprintf` into a `bufio.Writer`;
  calling `fmt.Printf` on the unbuffered output per line is slow.
- **Python**: the simple solution reads the whole input with
  `sys.stdin.buffer.read().split()`, builds all lines and writes them with
  one `join`.
- **Java**: the simple solution reads with `BufferedReader` and
  `StringTokenizer` and collects the output in a `StringBuilder`; it
  formats with `Locale.US`, otherwise the decimal separator may be a
  comma.
- **Rust**: the simple solution reads the whole input into a `String`,
  parses `u64` and formats with `{:.4}` into one output string.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1001_math.cpp](1001_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.125 s | 1576 KB | 11277417 |
| [1001_math.go](1001_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.125 s | 6588 KB | 11303052 |
| [1001_math.java](1001_math.java) | Java 1.8 | math | O(n) | AC | 0.593 s | 11728 KB | 11303054 |
| [1001_math.py](1001_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.125 s | 11492 KB | 11277419 |
| [1001_math.rs](1001_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.046 s | 3072 KB | 11303271 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1001_math_optimized.cpp](1001_math_optimized.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.031 s | 356 KB | 11303536 |
| [1001_math_optimized.go](1001_math_optimized.go) | Go 1.14 x64 | math | O(n) | AC | 0.015 s | 1180 KB | 11303537 |
| [1001_math_optimized.java](1001_math_optimized.java) | Java 1.8 | math | O(n) | AC | 0.125 s | 872 KB | 11303449 |
| [1001_math_optimized.py](1001_math_optimized.py) | Python 3.12 x64 | math | O(n) | AC | 0.156 s | 2052 KB | 11303694 |
| [1001_math_optimized.rs](1001_math_optimized.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.015 s | 464 KB | 11303538 |
