# 1545. Hieroglyphs

[Timus 1545](https://acm.timus.ru/problem.aspx?space=1&num=1545) · difficulty 50 · implementation

Original problem by Evgeny Krokhalev, from the Eleventh Ural Collegiate Team Programming Championship, Ekaterinburg, April 21, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A dictionary holds N ≤ 1000 hieroglyphs, each written as two lowercase
letters. Given a typed letter, print the hieroglyphs that start with it.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, the N two-letter entries, then the letter.

## Output

The matching entries, one per line, in any order; nothing if there are
none.

## Examples

### Example 1

Input:

```
6
na
no
ni
ki
ka
ku
k
```

Output:

```
ka
ki
ku
```

## Solution

Compare the first letter of every entry with the typed one and print
the matches in input order. `O(N)`.

Pitfalls:

- with no match the output is empty (tests 02, 05);
- an entry that appears twice is printed twice (test 03);
- the letter must be first: a match in the second place does not count
  (test 05).

## Optimized solutions

The optimized C++ solution keeps the two-letter entries in a local array
of three-byte C strings instead of `std::string`, reads them with
`scanf("%2s")` and prints them with `puts`: 120 KB instead of 392 KB,
with the same time.

Every hieroglyph is two letters. The optimized Java solution keeps them
in byte arrays filled from 256-byte blocks and writes the answer from
one byte array, with no `Scanner` and no strings: 392 KB instead of
1804 KB, with the same time. The optimized Rust solution keeps each
hieroglyph as a pair of bytes and writes through a `BufWriter` with a
small buffer: 0.015 s instead of 0.046 s and 196 KB instead of 236 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1545_implementation.cpp](1545_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 392 KB | 11287555 |
| [1545_implementation.go](1545_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.031 s | 1104 KB | 11287556 |
| [1545_implementation.java](1545_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.093 s | 1804 KB | 11287558 |
| [1545_implementation.py](1545_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.062 s | 460 KB | 11287557 |
| [1545_implementation.rs](1545_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.046 s | 236 KB | 11287559 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1545_implementation_optimized.cpp](1545_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 120 KB | 11303617 |
| [1545_implementation_optimized.java](1545_implementation_optimized.java) | Java 1.8 | implementation | O(N) | AC | 0.109 s | 392 KB | 11303759 |
| [1545_implementation_optimized.rs](1545_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 196 KB | 11303760 |
