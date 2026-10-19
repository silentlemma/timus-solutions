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

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2073_implementation.cpp](2073_implementation.cpp) | G++ 13.2 x64 | implementation | O(input) | AC | 0.015 s | 380 KB |
| [2073_implementation.go](2073_implementation.go) | Go 1.14 x64 | implementation | O(input) | AC | 0.015 s | 1832 KB |
| [2073_implementation.java](2073_implementation.java) | Java 1.8 | implementation | O(input) | AC | 0.078 s | 2308 KB |
| [2073_implementation.py](2073_implementation.py) | Python 3.12 x64 | implementation | O(input) | AC | 0.062 s | 1324 KB |
| [2073_implementation.rs](2073_implementation.rs) | Rust 1.75 x64 | implementation | O(input) | AC | 0.015 s | 748 KB |
