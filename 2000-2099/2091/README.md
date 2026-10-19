# 2091. Two courses that split the programs most evenly

[Timus 2091](https://acm.timus.ru/problem.aspx?space=1&num=2091) · difficulty 271 · bruteforce

Original problem by Dmitry Ivankov, from the Open Ural FU Personal Contest 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An n × m table says which of m courses each of n programs includes.
Choose two different courses A and B; they split the programs into four
groups: with both, with A only, with B only, with neither. Make the
largest group as small as possible and output its size and the two
courses. Any optimal pair is accepted. The limits are 1 second and
64 MB.

## Input

n and m, 4 ≤ n, m ≤ 100, then the n rows of m zeros and ones.

## Output

The smallest possible size of the largest group, then the two courses.

## Checking

A checker compares the size and recounts the groups of the printed pair.

## Examples

### Example 1

Input:

```
6 4
0 0 0 1
0 0 1 0
0 1 1 1
1 1 1 1
0 0 0 0
1 0 0 1
```

Output:

```
2
1 3
```

## Solution

There are fewer than 5000 pairs of courses, and the groups of a pair are
counted in one pass over the programs, with the group number
2·[A] + [B]. Trying every pair costs O(m² n), half a million steps.

In the example courses 1 and 3 give the groups {4}, {6}, {2, 3} and
{1, 5}, so the largest has 2 programs.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2091_bruteforce.cpp](2091_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(m^2 n) | AC | 0.015 s | 252 KB |
| [2091_bruteforce.go](2091_bruteforce.go) | Go 1.14 x64 | bruteforce | O(m^2 n) | AC | 0.031 s | 1200 KB |
| [2091_bruteforce.java](2091_bruteforce.java) | Java 1.8 | bruteforce | O(m^2 n) | AC | 0.140 s | 5712 KB |
| [2091_bruteforce.py](2091_bruteforce.py) | Python 3.12 x64 | bruteforce | O(m^2 n) | AC | 0.140 s | 776 KB |
| [2091_bruteforce.rs](2091_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(m^2 n) | AC | 0.015 s | 436 KB |
