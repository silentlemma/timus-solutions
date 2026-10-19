# 1837. Isenbaev's Number

[Timus 1837](https://acm.timus.ru/problem.aspx?space=1&num=1837) · difficulty 60 · bfs

Original problem: folklore, from the Fifteenth Ural Championship in Sports Programming, April 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Isenbaev's number is 0 for Vladislav Isenbaev, 1 for Isenbaev's
teammates, 2 for their teammates who never played with Isenbaev, and so
on. Given the teams, print the number of every contestant, or
"undefined" if there is no chain of teams to Isenbaev.

## Input

n (1 ≤ n ≤ 100), then n teams of three surnames (an uppercase letter
followed by lowercase ones, at most 20 letters). Isenbaev's surname is
"Isenbaev".

## Output

Every contestant with the number, sorted by surname.

## Examples

### Example 1

Input:

```
7
Isenbaev Oparin Toropov
Ayzenshteyn Oparin Samsonov
Ayzenshteyn Chevdar Samsonov
Fominykh Isenbaev Oparin
Dublennykh Fominykh Ivankov
Burmistrov Dublennykh Kurpilyanskiy
Cormen Leiserson Rivest
```

Output:

```
Ayzenshteyn 2
Burmistrov 3
Chevdar 3
Cormen undefined
Dublennykh 2
Fominykh 1
Isenbaev 0
Ivankov 2
Kurpilyanskiy 3
Leiserson undefined
Oparin 1
Rivest undefined
Samsonov 2
Toropov 1
```

## Solution

Join every two members of a team in a graph. The number is the
distance from Isenbaev, found by a breadth-first search; contestants it
never reaches are undefined. Print the names in sorted order. With at
most 300 contestants, any approach is fast. `O(n log n)` for the
sorting.

In the example Oparin played with Isenbaev (1), Ayzenshteyn with Oparin
(2), Chevdar with Ayzenshteyn (3), and Cormen's team is cut off.

Pitfalls:

- Isenbaev may be missing from the input; then everyone is undefined;
- the same team may appear twice;
- names compare as plain strings, all starting with a capital.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1837_bfs.cpp](1837_bfs.cpp) | G++ 13.2 x64 | bfs | O(n log n) | AC | 0.015 s | 552 KB |
| [1837_bfs.go](1837_bfs.go) | Go 1.14 x64 | bfs | O(n log n) | AC | 0.031 s | 1420 KB |
| [1837_bfs.java](1837_bfs.java) | Java 1.8 | bfs | O(n log n) | AC | 0.171 s | 4192 KB |
| [1837_bfs.py](1837_bfs.py) | Python 3.12 x64 | bfs | O(n log n) | AC | 0.093 s | 560 KB |
| [1837_bfs.rs](1837_bfs.rs) | Rust 1.75 x64 | bfs | O(n log n) | AC | 0.046 s | 468 KB |
