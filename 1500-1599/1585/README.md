# 1585. Penguins

[Timus 1585](https://acm.timus.ru/problem.aspx?space=1&num=1585) · difficulty 38 · implementation

Original problem by Vladimir Yakovlev, from the ACM ICPC 2007–2008 NEERC Eastern Subregional Contest, Yekaterinburg, October 27, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A notebook lists N ≤ 1000 penguins, each as "Emperor Penguin", "Little
Penguin" or "Macaroni Penguin". Print the kind that occurs most often;
it is unique.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then one kind per line.

## Output

The most frequent kind.

## Examples

### Example 1

Input:

```
7
Emperor Penguin
Macaroni Penguin
Little Penguin
Emperor Penguin
Macaroni Penguin
Macaroni Penguin
Little Penguin
```

Output:

```
Macaroni Penguin
```

## Solution

Count the records by their first word and print the kind with the
largest count, followed by "Penguin". `O(N)`.

Pitfalls:

- every record has a space inside, so it is either read as a whole line
  or as two words;
- a kind may be missing entirely (test 03).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1585_implementation.cpp](1585_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 388 KB |
| [1585_implementation.go](1585_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.015 s | 1132 KB |
| [1585_implementation.java](1585_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.171 s | 4576 KB |
| [1585_implementation.py](1585_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.062 s | 512 KB |
| [1585_implementation.rs](1585_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 440 KB |
