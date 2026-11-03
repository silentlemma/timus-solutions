# 1769. Old Ural Legend

[Timus 1769](https://acm.timus.ru/problem.aspx?space=1&num=1769) · difficulty 206 · strings

Original problem by Daniil Ayzenshteyn, from the Fourteenth Ural Championship in Sports Programming, April 10, 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given a non-empty line of decimal digits, find the smallest positive
integer whose decimal notation does not occur in the line.

## Input

The line, at most 10⁵ digits.

## Output

That integer.

## Checking

Compare output tokens; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
10123456789
```

Output:

```
11
```

## Solution

A line of n digits has at most n pieces of each length, while there are
9·10⁵ numbers of six digits, so some six-digit number is always
missing and the answer has at most six digits. Every piece of one to
six digits that does not start with a zero is the notation of a number;
marking them all and then counting up from 1 to the first unmarked
number gives the answer. `O(6n)`.

In the example 1 to 9 and 10 occur, but 11 does not.

Pitfalls:

- pieces starting with 0 are not notations of numbers, though the
  number after the zero still occurs one digit later;
- a line of zeros misses 1;
- searching the line for each number in turn can be slow on long
  lines with a large answer.

The answers agree with a search of the line for 1, 2, 3 and so on on 90
random lines and with an independent accepted implementation on 20
long ones.

## Optimized solutions

Mark decimal substrings of only one length at a time using numeric rolling codes and a compact bitmap. Scan candidate numbers in increasing order and stop at the first absent number. If every number of the current length occurs, move to the next length and reuse storage. Thus leading zeros and the required smallest answer follow the original numeric definition, without allocating a string object for each substring or retaining sets for all lengths.

- `1769_strings_optimized.cpp`: 0.031 s / 376 KB; base `1769_strings.cpp`: 0.015 s / 612 KB; relative change: time +106.7%, memory -38.6%.
- `1769_strings_optimized.go`: 0.046 s / 1444 KB; base `1769_strings.go`: 0.031 s / 2740 KB; relative change: time +48.4%, memory -47.3%.
- `1769_strings_optimized.java`: 0.140 s / 556 KB; base `1769_strings.java`: 0.156 s / 2124 KB; relative change: time -10.3%, memory -73.8%.
- `1769_strings_optimized.py`: 0.250 s / 1452 KB; base `1769_strings.py`: 0.312 s / 23740 KB; relative change: time -19.9%, memory -93.9%.
- `1769_strings_optimized.rs`: 0.031 s / 468 KB; base `1769_strings.rs`: 0.031 s / 1472 KB; relative change: time -0.0%, memory -68.2%.

## Language notes

The saved rating snapshot is from 1–2 November 2026. C++ requires the top 15% or the first 10 places in both time and memory; other families require first place in both. Equal results share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `1769_strings.cpp`; covering source `1769_strings.cpp`; time/memory places 1/7, other-author entries 72/72.

- Go: preferred teaching base `1769_strings.go`; covering source `1769_strings.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1769_strings.java`; covering source `1769_strings_optimized.java`; time/memory places 2/1, other-author entries 2/2.

- Python/PyPy: preferred teaching base `1769_strings.py`; covering source `1769_strings_optimized.py`; time/memory places 7/1, other-author entries 14/14.

- Rust: preferred teaching base `1769_strings.rs`; covering source `1769_strings.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

The simple table includes the preferred teaching sources and preserved Accepted alternatives. The language notes identify the preferred base for each family.

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1769_strings.cpp](1769_strings.cpp) | G++ 13.2 x64 | strings | O(6n) | AC | 0.015 s | 612 KB | 11308926 |
| [1769_strings.go](1769_strings.go) | Go 1.14 x64 | strings | O(6n) | AC | 0.031 s | 2740 KB | 11289655 |
| [1769_strings.java](1769_strings.java) | Java 1.8 | strings | O(6n) | AC | 0.156 s | 2124 KB | 11308927 |
| [1769_strings.py](1769_strings.py) | Python 3.12 x64 | strings | O(6n) | AC | 0.312 s | 23740 KB | 11308928 |
| [1769_strings.rs](1769_strings.rs) | Rust 1.75 x64 | strings | O(6n) | AC | 0.031 s | 1472 KB | 11289658 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1769_strings_optimized.cpp](1769_strings_optimized.cpp) \* | G++ 13.2 x64 | strings | O(DN+10^D) | AC | 0.031 s | 376 KB | 11308082 |
| [1769_strings_optimized.go](1769_strings_optimized.go) | Go 1.14 x64 | strings | O(DN+10^D) | AC | 0.046 s | 1444 KB | 11308083 |
| [1769_strings_optimized.java](1769_strings_optimized.java) \* | Java 1.8 | strings | O(DN+10^D) | AC | 0.140 s | 556 KB | 11308084 |
| [1769_strings_optimized.py](1769_strings_optimized.py) \* | Python 3.12 x64 | strings | O(DN+10^D) | AC | 0.250 s | 1452 KB | 11308079 |
| [1769_strings_optimized.rs](1769_strings_optimized.rs) | Rust 1.75 x64 | strings | O(DN+10^D) | AC | 0.031 s | 468 KB | 11308085 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
