# 1581. Teamwork

[Timus 1581](https://acm.timus.ru/problem.aspx?space=1&num=1581) · difficulty 41 · implementation

Original problem by Alex Samsonov, from the USU Junior Contest (the Fourteenth Open Team Programming Contest for Schoolchildren of the Sverdlovsk Region), October 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A sequence of 1 ≤ N ≤ 1000 numbers from 1 to 10 is dictated as runs: for
each run of equal numbers, first how many there are and then which
number. Print the dictated numbers.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then the N numbers.

## Output

The lengths and values of the runs, in order, on one line.

## Examples

### Example 1

Input:

```
8
1 1 2 3 3 3 10 10
```

Output:

```
2 1 1 2 3 3 2 10
```

## Solution

Walk through the numbers and cut them into maximal runs of equal
values; for each run print its length and then its value. `O(N)`.

Pitfalls:

- a run may be the whole sequence, up to 1000 long (test 05);
- equal numbers that are not neighbours make separate runs (test 04);
- 10 is one number, so read numbers, not characters.

## Optimized solutions

The optimized solutions (Java, Rust) do not store the numbers: they
compare each number with the previous one while reading and finish a run
as soon as it ends; Java appends it to a `StringBuilder` with the whole
answer, Rust writes it to a `BufWriter`. The numbers are parsed by hand,
in Java from a 1 KB buffer instead of `Scanner`, in Rust from the bytes
of the input instead of splitting a `String`. Java: 0.093 s instead of
0.125 s and 436 KB instead of 2404 KB; Rust: 208 KB instead of 308 KB,
with the same time.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1581_implementation.cpp](1581_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 196 KB | 11287897 |
| [1581_implementation.go](1581_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.031 s | 1268 KB | 11287898 |
| [1581_implementation.java](1581_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.125 s | 2404 KB | 11287900 |
| [1581_implementation.py](1581_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.062 s | 372 KB | 11303372 |
| [1581_implementation.rs](1581_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 308 KB | 11303373 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1581_implementation_optimized.java](1581_implementation_optimized.java) | Java 1.8 | implementation | O(N) | AC | 0.093 s | 436 KB | 11303624 |
| [1581_implementation_optimized.rs](1581_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.031 s | 208 KB | 11303625 |
