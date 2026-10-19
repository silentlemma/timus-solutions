# 1877. Bicycle Codes

[Timus 1877](https://acm.timus.ru/problem.aspx?space=1&num=1877) · difficulty 19 · implementation

Original problem by Denis Mukhametianov, from the Ural Regional Team Programming Contest 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Den has two four-digit bicycle locks and uses them on alternate nights,
starting with the first lock on the night a thief first comes. The
thief tries code 0000 on that night, 0001 on the next, and so on. Will
the thief ever open the lock?

## Input

The codes of the first and the second lock, four digits each.

## Output

"yes" if the thief opens a lock some night, "no" otherwise.

## Examples

### Example 1

Input:

```
0001
0000
```

Output:

```
no
```

### Example 2

Input:

```
0002
0001
```

Output:

```
yes
```

## Solution

On night k (counting from 0) the thief tries code k, and the bicycle
is on the first lock when k is even and on the second when k is odd.
So the first lock falls if its code is even, the second if its code is
odd, and otherwise the bicycle is safe. `O(1)`.

In the first example the first code is odd and the second even, so
neither lock is ever tried with its own code.

Pitfalls:

- codes with leading zeros must be read as decimal numbers; Go's
  `fmt.Scan` can read "0009" as 0 and 9, so the Go solution reads
  strings;
- only the parity of each code matters, not which one is smaller.

The answers agree with an independent accepted implementation on all
tests.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1877_implementation.cpp](1877_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 120 KB |
| [1877_implementation.go](1877_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1064 KB |
| [1877_implementation.java](1877_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.109 s | 1572 KB |
| [1877_implementation.py](1877_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.093 s | 404 KB |
| [1877_implementation.rs](1877_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.031 s | 216 KB |
