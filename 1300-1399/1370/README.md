# 1370. Magician

[Timus 1370](https://acm.timus.ru/problem.aspx?space=1&num=1370) · difficulty 88 · implementation

Original problem by Stanislav Vasiliev, from the Ninth Ural Team Student Programming Championship, Yekaterinburg, April 19–24, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A wheel carries N digits, 11 ≤ N ≤ 1000, around its rim, and a window
shows 10 consecutive ones, at first digits 1 to 10. Every click turns
the wheel by one digit, so after one click the window shows digits 2 to
11. Given M ≤ 32 767 clicks, print the 10 digits in the window.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and M, then the N digits, one per line.

## Output

The 10 digits in the window, leading zeros included.

## Examples

### Example 1

Input:

```
12 7
1
2
3
4
5
6
7
8
9
0
7
7
```

Output:

```
8907712345
```

## Solution

After M clicks the window starts at digit M (counting from 0), and the
wheel wraps around, so the answer is digits (M + i) mod N for
i = 0 … 9. `O(1)` after reading the input.

Pitfalls:

- M can be many times larger than N (test 05);
- the window can wrap past the last digit (example);
- the answer is printed as digits, with its leading zeros (test 03).

## Language notes

- All five solutions keep the digits as text and join the ten in the
  window.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1370_implementation.cpp](1370_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 196 KB |
| [1370_implementation.go](1370_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.015 s | 1108 KB |
| [1370_implementation.java](1370_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.125 s | 1892 KB |
| [1370_implementation.py](1370_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.062 s | 404 KB |
| [1370_implementation.rs](1370_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.015 s | 244 KB |
