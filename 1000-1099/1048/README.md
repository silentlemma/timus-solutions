# 1048. Adding two numbers of a million digits

[Timus 1048](https://acm.timus.ru/problem.aspx?space=1&num=1048) · difficulty 200 · implementation

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

The output is compared token by token; extra whitespace does not matter.

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

Schoolbook addition: store the column sums (0 to 18) in a byte array,
then walk from the last column to the first, adding the carry and keeping
`t mod 10` with the new carry `t div 10`. The array of `N` bytes is
reused for the output digits. `O(N)` time and `N` bytes of memory.

The difficulty is only the size: about 4 MB of input and a 16 MB memory
limit. Reading must be fast, and no per-digit objects or 4-byte integers
per digit should be kept.

Pitfalls:

- leading zeros of the sum are printed: the output has exactly `N` digits;
- a carry can run through all million digits (`0999…9 + 000…1`);
- converting the numbers to a big integer type is unnecessary and, in
  many languages, quadratic.

## Language notes

- **C++**, **Java**: buffered byte reading with `fread` /
  `DataInputStream`; **Go**: `bufio.Reader.ReadByte`; **Rust**: the whole
  input in one byte vector.
- **Python**: the whole input is one `bytes` object; `translate` deletes
  the whitespace, slicing with step 2 separates the two numbers, and the
  carry loop writes into a `bytearray`. Converting with `int()` would be
  quadratic (and Python 3.12 refuses strings longer than 4300 digits by
  default).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1048_implementation.cpp](1048_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 1184 KB |
| [1048_implementation.go](1048_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.062 s | 1976 KB |
| [1048_implementation.java](1048_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.140 s | 2080 KB |
| [1048_implementation.py](1048_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.406 s | 10360 KB |
| [1048_implementation.rs](1048_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 10248 KB |
