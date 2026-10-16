# 1738. Computer Security

[Timus 1738](https://acm.timus.ru/problem.aspx?space=1&num=1738) · difficulty 1001 · implementation

Original problem by Daniil Ayzenshteyn, from the XIV Open USU Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Employees are numbered 1 to n, and each has a distinct pin of four hex
digits. Two numbers are similar if one becomes the other by inserting,
deleting or replacing one decimal digit, with no leading zeros. For
every pair of employees with similar numbers count the positions where
their pins differ, and report how many pairs differ in 1, 2, 3 and 4
positions.

## Input

n (2 ≤ n ≤ 65 536), then the pins of employees 1 to n.

## Output

Four numbers: how many similar pairs have pins differing in 1, 2, 3
and 4 positions.

## Examples

### Example 1

Input:

```
3
dead
beef
f00d
```

Output:

```
0 0 2 1
```

## Solution

Count each pair from its smaller number i. The larger number j is then
either i with one digit raised in place, or i with one digit inserted;
a deletion would give a smaller number, and that pair is counted from
the other side.

- A raised digit gives j = i + (d − old)·10^q. Different positions or
  digits give different numbers, so nothing repeats, and the digits are
  raised in order until j passes n.
- An insertion makes j one digit longer, so it is only needed when i
  is shorter than n. Inserting the same digit next to an equal digit
  gives the same number twice, so these candidates go through a set,
  and those with a leading zero are dropped.

The pins are read as numbers, and the positions where two pins differ
are the nonzero hex digits of their XOR, from a table of 65 536
entries. Each number has about 25 candidates. `O(n·L)` for L decimal
digits.

In the example, 1, 2 and 3 are all similar by replacing a digit; `dead`
and `beef` differ in 3 positions, `dead` and `f00d` in 3, `beef` and
`f00d` in 4.

Pitfalls:

- 1 and 11 are similar in two ways (inserting the second 1 on either
  side), but they are one pair;
- 10 is similar to 1 by deleting the zero, but 01 is not a number, so
  deleting the 1 of 10 gives nothing;
- the counts reach about 1.2 million, still fine for 32 bits.

The counts match a check of all pairs on random sets of up to 200
employees and an independent accepted implementation on the large
tests. The Python solution runs on PyPy; on CPython it needs about
0.5 s here for 65 536 employees, too close to the limit.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1738_implementation.cpp](1738_implementation.cpp) | G++ 13.2 x64 | implementation | O(n·L) | AC | 0.171 s | 728 KB |
| [1738_implementation.go](1738_implementation.go) | Go 1.14 x64 | implementation | O(n·L) | AC | 0.187 s | 7008 KB |
| [1738_implementation.java](1738_implementation.java) | Java 1.8 | implementation | O(n·L) | AC | 0.265 s | 5820 KB |
| [1738_implementation.py](1738_implementation.py) | PyPy 3.10 x64 | implementation | O(n·L) | AC | 0.328 s | 9528 KB |
| [1738_implementation.rs](1738_implementation.rs) | Rust 1.75 x64 | implementation | O(n·L) | AC | 0.125 s | 1996 KB |
