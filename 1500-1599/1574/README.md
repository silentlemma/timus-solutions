# 1574. Mathematicians and Brackets

[Timus 1574](https://acm.timus.ru/problem.aspx?space=1&num=1574) · difficulty 354 · strings

Original problem by Alexander Toropov, from the USU Junior Contest (the Fourteenth Open Team Programming Contest for Schoolchildren of the Sverdlovsk Region), October 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given a line of up to 100000 brackets, count the cyclic shifts, by 0 to
n − 1 characters, that turn it into a correct bracket sequence. Shifts
by different amounts count separately even when they give the same line.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The line of brackets.

## Output

The number of such shifts.

## Examples

### Example 1

Input:

```
)(()
```

Output:

```
1
```

### Example 2

Input:

```
)()(
```

Output:

```
2
```

### Example 3

Input:

```
()
```

Output:

```
1
```

## Solution

If the numbers of opening and closing brackets differ, no shift works.
Otherwise take the balance after each prefix: opening brackets minus
closing ones. A shift that starts right after position i changes every
balance by −p(i), where p(i) is the balance there, so it never goes
below zero exactly when p(i) is the lowest balance of all. The answer is
the number of prefixes whose balance equals that minimum. `O(n)`.

Pitfalls:

- a line such as `)()(` gives the same correct line by two different
  shifts, and both count (the second example);
- the shift by zero counts too (the third example);
- an unbalanced line has no answer but 0, even when a shift keeps every
  balance non-negative (tests 04, 05).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1574_strings.cpp](1574_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.031 s | 500 KB |
| [1574_strings.go](1574_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 1768 KB |
| [1574_strings.java](1574_strings.java) | Java 1.8 | strings | O(n) | AC | 0.125 s | 1196 KB |
| [1574_strings.py](1574_strings.py) | Python 3.12 x64 | strings | O(n) | AC | 0.093 s | 5252 KB |
| [1574_strings.rs](1574_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.046 s | 2068 KB |
