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

Read the final character as the letter and the preceding digits as
the row. Select one of three row ranges and use this classification:

| Rows | `window` | `aisle` | `neither` |
| --- | --- | --- | --- |
| 1–2 | A D | B C | none |
| 3–20 | A F | B C D E | none |
| 21–65 | A K | C D G H | B E F J |

These sets follow directly from the two ends of each row and the
neighbors of each aisle. In rows 1–2, A and D are next to both a window
and an aisle; the required window priority gives the table above.
Each valid letter is assigned exactly the required result.

The number of checks and the input size are bounded by constants, so
both time and extra memory are `O(1)`.

In the examples, row 3 has an aisle between B and C, so `3C` is `aisle`.
Seat `64A` is at the left window. Seat `21F` is in the middle block
between the aisles and touches neither one, so it is `neither`.

Pitfalls:

- rows 2/3 and 20/21 use different layouts;
- the rightmost window letter changes from D to F to K;
- there is no seat I in rows 21–65;
- check windows before aisles, especially for A and D in rows 1–2.

The answers agree with a separate model of the seating layout on all 566
valid seats.

## Language notes

All five versions parse the digits before the final ASCII letter as
the row number and use the same fixed-size classification. Go and Rust
can safely index the designation by bytes because valid input contains
only decimal digits and one uppercase English letter.

Java uses `Scanner` for this single short token. No special fast-input
routine or large integer type is needed; membership tests examine only
the fixed seat-letter sets.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1893_implementation.cpp](1893_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.031 s | 348 KB |
| [1893_implementation.go](1893_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1104 KB |
| [1893_implementation.java](1893_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.156 s | 1580 KB |
| [1893_implementation.py](1893_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.109 s | 468 KB |
| [1893_implementation.rs](1893_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.046 s | 228 KB |
