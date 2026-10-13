# 1496. Spammer

[Timus 1496](https://acm.timus.ru/problem.aspx?space=1&num=1496) · difficulty 49 · implementation

Original problem by Sergey Pupyrev, from the Thirteenth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 14, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N submissions (0 ≤ N ≤ 100) came in the last 10 minutes of a contest,
each from a team named by up to 30 lowercase letters and digits. Print
every team that submitted more than once, in any order.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then N team names.

## Output

The teams with more than one submission, one per line.

## Examples

### Example 1

Input:

```
11
naucoder
iceman
abikbaev
abikbaev
petr
abikbaev
abikbaev
x
abikbaev
acrush
x
```

Output:

```
x
abikbaev
```

## Solution

Count the submissions of each team in a dictionary and print the teams
with a count above one, each once. Keeping the order of first
appearance is not required, but it makes the output stable. `O(N)`.

Pitfalls:

- a team that submitted many times is still printed once (test 01);
- names are text, so "0" and "00" are different teams (test 04);
- with no repeated team the output is empty (tests 02, 03, 05).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1496_implementation.cpp](1496_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 412 KB |
| [1496_implementation.go](1496_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.015 s | 1116 KB |
| [1496_implementation.java](1496_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.156 s | 3944 KB |
| [1496_implementation.py](1496_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.062 s | 336 KB |
| [1496_implementation.rs](1496_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.031 s | 412 KB |
