# 1563. Bayan

[Timus 1563](https://acm.timus.ru/problem.aspx?space=1&num=1563) · difficulty 54 · hashing

Original problem by Vladimir Yakovlev, from the Twelfth Ural State University Programming Championship, October 6, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Angela walks past N shops (N ≤ 1000) in order and says "Bayan" at every
shop whose name was already seen. Count how many times Angela says it.
A name is a string of 1 to 30 Latin letters and spaces, and no two names
differ only in letter case.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then one shop name per line.

## Output

The number of repeated shops.

## Examples

### Example 1

Input:

```
12
ESPRIT
Nice Connection
Camelot
Adilisik
Lady and Gentleman City
MEXX
Camelot
Sultanna Frantsuzova
Camaieu
MEXX
Axara
Camelot
```

Output:

```
3
```

## Solution

Every shop past the first of its name is a repeat, so the answer is N
minus the number of different names, counted with a hash set. A name is
the whole line, spaces included, so lines are read whole and only the
line end is cut off. `O(N)` expected time.

Pitfalls:

- names contain spaces, so reading them word by word breaks them up
  (tests 03, gen3);
- one space more or less makes another name (test 03);
- a name may be a prefix of another one (test 05).

## Optimized solutions

The optimized C++ solution keeps the same set of names. It reads each
line character by character into a buffer of 30 characters instead of
`getline` and sizes the set for `N` names in advance: 300 KB instead of
512 KB, with the same time.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1563_hashing.cpp](1563_hashing.cpp) | G++ 13.2 x64 | hashing | O(N) | AC | 0.015 s | 512 KB | 11287691 |
| [1563_hashing.go](1563_hashing.go) | Go 1.14 x64 | hashing | O(N) | AC | 0.031 s | 1144 KB | 11287693 |
| [1563_hashing.java](1563_hashing.java) | Java 1.8 | hashing | O(N) | AC | 0.078 s | 660 KB | 11287696 |
| [1563_hashing.py](1563_hashing.py) | Python 3.12 x64 | hashing | O(N) | AC | 0.078 s | 516 KB | 11287695 |
| [1563_hashing.rs](1563_hashing.rs) | Rust 1.75 x64 | hashing | O(N) | AC | 0.046 s | 476 KB | 11287697 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1563_hashing_optimized.cpp](1563_hashing_optimized.cpp) | G++ 13.2 x64 | hashing | O(N) | AC | 0.015 s | 300 KB | 11303620 |
