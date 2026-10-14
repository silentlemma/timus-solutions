# 1546. Japanese Sorting

[Timus 1546](https://acm.timus.ru/problem.aspx?space=1&num=1546) · difficulty 887 · sorting

Original problem by Vladimir Yakovlev, from the Eleventh Ural Collegiate Team Programming Championship, Ekaterinburg, April 21, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Sort strings of lowercase letters and digits (at most 100 KB in total)
in "Japanese" order, where numbers inside the strings compare by value:
photox2 comes before photox10. The statement does not spell the rules
out; it offers a program that sorts small inputs.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The strings, one per line.

## Output

The same strings in Japanese order.

## Examples

### Example 1

Input:

```
photox10
photox1
photo2
photox2
```

Output:

```
photo2
photox1
photox2
photox10
```

## Solution

The rules are those of natural sorting as in a file manager, and the
details below agree with the program given in the statement as quoted on
the judge's discussion board:

- split a string into letters and maximal runs of digits;
- compare piece by piece: a number comes before a letter, numbers
  compare by value (by length without leading zeros, then digit by
  digit, as they may be very long), letters by their code;
- a string that ends earlier comes first;
- only if all pieces are equal, compare the numbers' leading zeros run
  by run, and more zeros come first: 000 < 00 < 0, a001 < a01, and
  01w01 < 01w1.

Each string gets a key: the list of pieces and the list of minus the
zero counts; a stable sort by the key does the rest.
`O(L log n)` for total length L.

Pitfalls:

- zeros only break ties: z001pp00 comes after z0pp01 (test 02);
- a string of zeros is a number, and 000 sorts before 0 (test 03);
- numbers may exceed 64 bits (test 04);
- digits come before letters: 1, 2, 10, a, a1, aa (test 06).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1546_sorting.cpp](1546_sorting.cpp) | G++ 13.2 x64 | sorting | O(L log n) | AC | 0.031 s | 5476 KB |
| [1546_sorting.go](1546_sorting.go) | Go 1.14 x64 | sorting | O(L log n) | AC | 0.093 s | 7628 KB |
| [1546_sorting.java](1546_sorting.java) | Java 1.8 | sorting | O(L log n) | AC | 0.312 s | 11504 KB |
| [1546_sorting.py](1546_sorting.py) | Python 3.12 x64 | sorting | O(L log n) | AC | 0.140 s | 9448 KB |
| [1546_sorting.rs](1546_sorting.rs) | Rust 1.75 x64 | sorting | O(L log n) | AC | 0.031 s | 4692 KB |
