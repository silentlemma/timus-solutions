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

## Optimized solutions

The three kinds start with different capital letters, E, L and M, and
the word "Penguin" and the number `N` contain none of them, so it is
enough to count these letters over the whole input and pick the largest
count. The optimized C++ solution reads no words at all and counts the
letters with `getchar`, printing the answer with `puts` instead of
`iostream`: 88 KB instead of 388 KB, with the same time. The optimized
Java solution counts them while reading 256-byte blocks: 0.109 s instead
of 0.171 s and 328 KB instead of 4576 KB.

The optimized Python solution counts the full names in the raw bytes
with `bytes.count`: 348 KB instead of 512 KB, with the same time.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1585_implementation.cpp](1585_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 388 KB | 11287935 |
| [1585_implementation.go](1585_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.015 s | 1132 KB | 11287937 |
| [1585_implementation.java](1585_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.171 s | 4576 KB | 11287943 |
| [1585_implementation.py](1585_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.062 s | 512 KB | 11287941 |
| [1585_implementation.rs](1585_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 440 KB | 11287944 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1585_implementation_optimized.cpp](1585_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 88 KB | 11303626 |
| [1585_implementation_optimized.java](1585_implementation_optimized.java) | Java 1.8 | implementation | O(N) | AC | 0.109 s | 328 KB | 11303761 |
| [1585_implementation_optimized.py](1585_implementation_optimized.py) \* | Python 3.12 x64 | implementation | O(N) | AC | 0.078 s | 348 KB | 11303762 |

\* Not in the top 10 or the top 15% of the solutions in its language on
the current judge; it may be optimized further.
