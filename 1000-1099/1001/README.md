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

Every printed number must be within `10^-4` of the exact square root
(absolute error, or relative error for large values).

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
off by less than `10^-6`, far below the allowed `10^-4`.

Pitfalls:

- the count is not given, so read until the end of the input;
- the separators are arbitrary: several spaces, line breaks, empty lines;
- the values do not fit in 32 bits: use 64-bit integers;
- up to about 131 000 output lines: the output must be buffered.

## Language notes

- **C++**: `scanf("%llu")` in a loop, `printf("%.4f\n")`.
- **Go**: a byte-level parser over `bufio.Reader`, and `strconv.AppendFloat`
  into a `bufio.Writer`; calling `fmt.Printf` per line is slow.
- **Python**: read the whole input with `sys.stdin.buffer.read().split()`, build
  all lines and write them with one `join`.
- **Java**: parse the numbers from a byte buffer and collect the output in a
  `StringBuilder`; format with `Locale.US`, otherwise the decimal separator may
  be a comma.
- **Rust**: read the whole input into a `String`, parse `u64`, format with
  `{:.4}` into one output string.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1001_math.cpp](1001_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.125 s | 1576 KB |
| [1001_math.go](1001_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.031 s | 5056 KB |
| [1001_math.java](1001_math.java) | Java 1.8 | math | O(n) | AC | 0.453 s | 11412 KB |
| [1001_math.py](1001_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.125 s | 11492 KB |
| [1001_math.rs](1001_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.046 s | 3096 KB |
