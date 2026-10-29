# 2056. Determine the scholarship category

[Timus 2056](https://acm.timus.ru/problem.aspx?space=1&num=2056) · difficulty 41 · implementation

Folklore problem, from the Ural Sport Programming Championship 2015.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A student passed n exams with grades from 3 to 5. Name the scholarship:
`None` if there is any 3, otherwise `Named` if all grades are 5,
otherwise `High` if the average is at least 4.5, and `Common` in all
other cases. The limits are 1 second and 64 MB.

## Input

The number of exams n, 1 ≤ n ≤ 10, and then n lines with one grade each.

## Output

One word, case-sensitive.

## Checking

Outputs are compared token by token.

## Examples

```
3
5
5
4
```

```
High
```

```
3
3
3
3
```

```
None
```

For the first example the sum is fourteen and `2·14≥9·3`, so the average
exceeds 4.5. There is no three and not every grade is five, hence
`High`. In the second example a three is present, so the
highest-priority rule gives `None`.

## Solution

Read the grades keeping their sum S and their minimum. Then apply the
rules in order: a 3 anywhere gives `None`; all fives give `Named`; an
average of at least 4.5 gives `High`, checked in integers as 2S ≥ 9n;
everything else is `Common`. `O(n)`.

Pitfalls:

- a 3 beats any average;
- all fives is `Named`, not `High`;
- the 4.5 threshold is inclusive: one 4 and one 5 give `High`.

## Optimized solutions

The optimized C++ solution reads with `scanf` and prints with `puts`
instead of `iostream` and `std::string`: 116 KB instead of 420 KB, with
the same time.

## Language notes

No language needs anything special.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [2056_implementation.cpp](2056_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 420 KB | 11293663 |
| [2056_implementation.go](2056_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.046 s | 1096 KB | 11293666 |
| [2056_implementation.java](2056_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.093 s | 420 KB | 11303532 |
| [2056_implementation.py](2056_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 472 KB | 11293667 |
| [2056_implementation.rs](2056_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.015 s | 224 KB | 11293678 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [2056_implementation_optimized.cpp](2056_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 116 KB | 11303966 |
