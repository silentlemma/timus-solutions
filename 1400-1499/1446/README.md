# 1446. Sorting Hat

[Timus 1446](https://acm.timus.ru/problem.aspx?space=1&num=1446) · difficulty 91 · implementation

Original problem by Stanislav Vasiliev, from the Tenth Ural Collegiate Team Programming Championship, March 24–25, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N first-years (1 ≤ N ≤ 1000) were sorted into houses; for each, in the
order of the ceremony, a line holds the name (Latin letters, spaces and
hyphens, at most 200 characters) and the next line the house. Print the
lists of Slytherin, Hufflepuff, Gryffindor and Ravenclaw in this order:
the house name with a colon, then its students one per line in the order
of the ceremony, with an empty line between the lists. Every house gets
at least one student.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then 2N lines: a name and a house for each student.

## Output

The four lists.

## Examples

### Example 1

Input:

```
7
Ivan Ivanov
Gryffindor
Mac Go Nagolo
Hufflepuff
Zlobeus Zlei
Slytherin
Um Bridge
Slytherin
Tatiana Henrihovna Grotter
Ravenclaw
Garry Potnyj
Gryffindor
Herr Mionag-Ranger
Gryffindor
```

Output:

```
Slytherin:
Zlobeus Zlei
Um Bridge

Hufflepuff:
Mac Go Nagolo

Gryffindor:
Ivan Ivanov
Garry Potnyj
Herr Mionag-Ranger

Ravenclaw:
Tatiana Henrihovna Grotter
```

## Solution

Read the input line by line, since names contain spaces, and append each
name to the list of its house; then print the lists in the required
order. Only the line break is removed from a name, so spaces inside it
stay as they are. `O(N)` lines.

Pitfalls:

- reading by words splits names apart (tests 01, 03, 04);
- a student may be called like a house (test 03);
- the house order of the output is not alphabetical.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1446_implementation.cpp](1446_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.031 s | 520 KB |
| [1446_implementation.go](1446_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.015 s | 1672 KB |
| [1446_implementation.java](1446_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.125 s | 2324 KB |
| [1446_implementation.py](1446_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.062 s | 1520 KB |
| [1446_implementation.rs](1446_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 980 KB |
