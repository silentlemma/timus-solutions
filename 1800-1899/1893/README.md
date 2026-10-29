# 1893. A380

[Timus 1893](https://acm.timus.ru/problem.aspx?space=1&num=1893) · difficulty 60 · implementation

Original problem by Denis Dublennykh, from the NEERC 2011 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Classify one valid seat by its row number and letter. The seating plan
depends on the row:

| Rows | Seat letters in order | Aisles between |
| --- | --- | --- |
| 1–2 | A B C D | A/B and C/D |
| 3–20 | A B C D E F | B/C and D/E |
| 21–65 | A B C D E F G H J K | C/D and G/H |

The first and last seats in every row are next to windows. A seat on
either side of an aisle is next to that aisle. Print `window` for a
window seat; otherwise print `aisle` for an aisle seat, or `neither`
for any other seat. Window classification takes priority.

The limits are 1 second and 64 MB.

## Input

One seat designation: its row number followed immediately by its
uppercase letter, for example `3C`. The row is between 1 and 65,
and the letter is valid for that row. Economy rows omit the letter I.

## Output

Print exactly one of `window`, `aisle` or `neither`.

## Checking

Outputs are compared token by token.

## Examples

### Example 1

Input:

```
3C
```

Output:

```
aisle
```

### Example 2

Input:

```
64A
```

Output:

```
window
```

### Example 3

Input:

```
21F
```

Output:

```
neither
```

## Solution

The row is the number before the last character, the seat is the last
letter. The plane has three layouts, and each sets which seats are by a
window and which are by an aisle:

| Rows | `window` | `aisle` | `neither` |
| --- | --- | --- | --- |
| 1–2 | A D | B C | none |
| 3–20 | A F | B C D E | none |
| 21–65 | A K | C D G H | B E F J |

In rows 1–2 the seats A and D touch both a window and an aisle; a window
comes first, so they are `window`. `O(1)`.

Pitfalls:

- the layouts change after rows 2 and 20;
- there is no seat I in rows 21–65.

## Optimized solutions

The optimized C++ solution reads the seat with `scanf("%d%c")` and
prints with `puts` instead of using `iostream` and `std::string`: 120 KB
instead of 348 KB. The layouts are the same.

The optimized Java solution reads the seat byte by byte, the digits
making the row and the next byte the letter, instead of reading a
string: 0.109 s instead of 0.156 s and 380 KB instead of 1580 KB.

## Language notes

No language needs anything special.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1893_implementation.cpp](1893_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.031 s | 348 KB | 11291153 |
| [1893_implementation.go](1893_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1104 KB | 11291155 |
| [1893_implementation.java](1893_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.156 s | 1580 KB | 11291159 |
| [1893_implementation.py](1893_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.109 s | 468 KB | 11291157 |
| [1893_implementation.rs](1893_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.046 s | 228 KB | 11291163 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1893_implementation_optimized.cpp](1893_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 120 KB | 11303647 |
| [1893_implementation_optimized.java](1893_implementation_optimized.java) | Java 1.8 | implementation | O(1) | AC | 0.109 s | 380 KB | 11303785 |
