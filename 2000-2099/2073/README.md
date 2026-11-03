# 2073. A summary table of contest logs

[Timus 2073](https://acm.timus.ru/problem.aspx?space=1&num=2073) · difficulty 242 · implementation

Original problem by Kirill Borozdin, prepared by Kirill Borozdin and Alexey Danilyuk, from the Ural Regional Team Programming Contest 2015.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n ≤ 100 contest logs are given: a name of 1 to 30 letters, digits and
spaces, a date DD.MM.YY, the number of problems p ≤ 13 and of submits
s ≤ 100, then s submits, each a problem letter and a verdict. Print a
table drawn with `+`, `-` and `|`: a header row and one row per contest
with the name padded to 30 characters, the date (8 characters) and 13
marks, one per letter A … M. A mark is `o` if the problem was accepted
at least once, `x` if it was submitted but never accepted, `.` if it was
in the contest but not submitted, and a space if the contest had no
such problem. The limits are 1 second and 64 MB.

## Input

n, then for each contest the name line, the date line, the line "p s"
and s lines "letter verdict". A verdict is one of `Accepted`,
`Wrong Answer`, `Runtime Error`, `Time Limit Exceeded`,
`Memory Limit Exceeded`, `Compilation Error`.

## Output

The table, laid out as in the example, with a border line before the
header, after it and after every contest.

## Checking

Compare the complete output exactly, including spaces and line breaks.

## Examples

### Example 1

Input:

```
2
Codeforces Gamma Round 512
29.02.16
5 4
A Accepted
B Accepted
C Accepted
E Accepted
URKOP
17.10.15
12 11
A Accepted
B Wrong Answer
B Time Limit Exceeded
J Accepted
B Accepted
J Time Limit Exceeded
J Accepted
F Accepted
E Runtime Error
H Accepted
E Runtime Error
```

Output:

```
+------------------------------+--------+-------------+
|Contest name                  |Date    |ABCDEFGHIJKLM|
+------------------------------+--------+-------------+
|Codeforces Gamma Round 512    |29.02.16|ooo.o        |
+------------------------------+--------+-------------+
|URKOP                         |17.10.15|oo..xo.o.o.. |
+------------------------------+--------+-------------+
```

## Solution

Every contest starts with p dots followed by 13 − p spaces. A submit
sets its mark to `o` when the verdict is `Accepted`; any other verdict
sets `x` unless the mark is already `o`. The rows are then printed with
the name padded by spaces to 30 characters. The time complexity is
O(input).

The names may contain spaces, so input is read line by line, and
trailing spaces and carriage returns are removed (a name never ends with
a space). The marks keep their trailing spaces: in the example the
second row ends with `.. ` before the border.

## Optimized solutions

The contest marks and exact table layout are unchanged. Read and emit one contest at a time with bounded line and ASCII row buffers instead of retaining every input line and a complete output string. Preserve names and date text exactly and keep the same padding widths. Buffer bounds follow the stated maximum field lengths; numeric fields use their own parser rather than being truncated to a text-field bound.

- `2073_implementation_optimized.cpp`: 0.015 s / 112 KB; base `2073_implementation.cpp`: 0.001 s / 356 KB; relative change: time -0.0%, memory -68.5%.
- `2073_implementation_optimized.java`: 0.093 s / 440 KB; base `2073_implementation.java`: 0.093 s / 2224 KB; relative change: time -0.0%, memory -80.2%.
- `2073_implementation_optimized.py`: 0.078 s / 464 KB; base `2073_implementation.py`: 0.062 s / 1196 KB; relative change: time +25.8%, memory -61.2%.
- `2073_implementation_optimized.rs`: 0.015 s / 224 KB; base `2073_implementation.rs`: 0.015 s / 732 KB; relative change: time -0.0%, memory -69.4%.

## Language notes

The saved rating snapshot is from 1–2 November 2026. C++ requires the top 15% or the first 10 places in both time and memory; other families require first place in both. Equal results share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `2073_implementation.cpp`; covering source `2073_implementation_optimized.cpp`; time/memory places 1/1, other-author entries 32/32.

- Go: preferred teaching base `2073_implementation.go`; covering source `2073_implementation.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `2073_implementation.java`; covering source `2073_implementation.java`; time/memory places 1/1, other-author entries 2/2.

- Python/PyPy: preferred teaching base `2073_implementation.py`; covering source `2073_implementation_optimized.py`; time/memory places 1/2, other-author entries 9/9.

- Rust: preferred teaching base `2073_implementation.rs`; covering source `2073_implementation.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

The simple table includes the preferred teaching sources and preserved Accepted alternatives. The language notes identify the preferred base for each family.

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2073_implementation.cpp](2073_implementation.cpp) | G++ 13.2 x64 | implementation | O(input) | AC | 0.001 s | 356 KB | 11309231 |
| [2073_implementation.go](2073_implementation.go) | Go 1.14 x64 | implementation | O(input) | AC | 0.015 s | 1832 KB | 11294474 |
| [2073_implementation.java](2073_implementation.java) | Java 1.8 | implementation | O(input) | AC | 0.093 s | 2224 KB | 11309232 |
| [2073_implementation.py](2073_implementation.py) | Python 3.12 x64 | implementation | O(input) | AC | 0.062 s | 1196 KB | 11309233 |
| [2073_implementation.rs](2073_implementation.rs) | Rust 1.75 x64 | implementation | O(input) | AC | 0.015 s | 732 KB | 11309234 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2073_implementation_optimized.cpp](2073_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(input+output) | AC | 0.015 s | 112 KB | 11308727 |
| [2073_implementation_optimized.java](2073_implementation_optimized.java) | Java 1.8 | implementation | O(input+output) | AC | 0.093 s | 440 KB | 11308732 |
| [2073_implementation_optimized.py](2073_implementation_optimized.py) \* | Python 3.12 x64 | implementation | O(input+output) | AC | 0.078 s | 464 KB | 11308735 |
| [2073_implementation_optimized.rs](2073_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(input+output) | AC | 0.015 s | 224 KB | 11308736 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
