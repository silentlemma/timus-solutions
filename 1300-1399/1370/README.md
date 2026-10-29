# 1370. Magician

[Timus 1370](https://acm.timus.ru/problem.aspx?space=1&num=1370) · difficulty 89 · implementation

Original problem by Stanislav Vasiliev, from the Ninth Ural Team Student Programming Championship, Yekaterinburg, April 19–24, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A wheel carries N digits, 11 ≤ N ≤ 1000, around its rim, and a window
shows 10 consecutive ones, at first digits 1 to 10. Every click turns
the wheel by one digit, so after one click the window shows digits 2 to
11. Given M clicks (1 ≤ M ≤ 32 767), print the 10 digits in the window.

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

## Optimized solutions

The optimized Java solution parses the numbers by hand instead of
`Scanner`, keeps the digits as bytes and writes the ten digits of the
window as one byte array: 0.093 s instead of 0.125 s and 340 KB instead
of 1892 KB.

The optimized C++ solution reads the digits as characters into a fixed
array and prints the ten of them with `putchar`, with no conversion to
numbers and no `std::string`: 120 KB instead of 196 KB, with the same
time.

## Language notes

- The simple C++ solution stores digits as integers, the other simple
  solutions as text. All join the ten in the window.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1370_implementation.cpp](1370_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 196 KB | 11285595 |
| [1370_implementation.go](1370_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.015 s | 1108 KB | 11285596 |
| [1370_implementation.java](1370_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.125 s | 1892 KB | 11285599 |
| [1370_implementation.py](1370_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.062 s | 404 KB | 11285597 |
| [1370_implementation.rs](1370_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 244 KB | 11285600 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1370_implementation_optimized.cpp](1370_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 120 KB | 11303744 |
| [1370_implementation_optimized.java](1370_implementation_optimized.java) | Java 1.8 | implementation | O(N) | AC | 0.093 s | 340 KB | 11303603 |
