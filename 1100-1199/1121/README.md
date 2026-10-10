# 1121. The types of the nearest branches on a street grid

[Timus 1121](https://acm.timus.ru/problem.aspx?space=1&num=1121) · difficulty 352 · bruteforce

Original problem by Leonid Volkov and Alexander Somov, from the USU Open Collegiate Programming Contest, October 2001, Junior Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A grid of `H × W` crossings (`1 ≤ H, W ≤ 150`) holds at each crossing a
bit mask of the branch types standing there (types are powers of two, at
most 11 of them; 0 means no branch). Distance is the number of street
segments walked, that is the Manhattan distance. For every crossing with
branches print `-1`; for every empty one print the bitwise union of the
types of its nearest branches, or `0` if none is within distance 5.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`H W`, then `H` lines of `W` masks.

## Output

`H` lines of `W` numbers.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
5 5
0 0 2 0 2
0 0 0 0 0
0 0 0 0 0
0 0 0 5 0
1 0 0 4 0
```

Output:

```
2 2 -1 2 -1
3 2 2 7 2
1 7 7 5 7
1 5 5 -1 5
-1 1 4 -1 4
```

## Solution

Only distances 1 to 5 matter, so for each empty crossing look at the
crossings at distance 1, then 2, and so on: the ring at distance `d` has
`4d` cells, 60 within distance 5. At the first distance where any branch
appears, the answer is the bitwise OR of the masks on that ring; stop
there. The offsets of each ring are listed once in advance.
`O(H · W · 60)`, about 1.4 million checks.

Pitfalls:

- the types are combined with OR, not added: two branches of the same type
  at the nearest distance count once (in `3 0 6` the middle gets `7`,
  not `9`);
- only the nearest distance counts, even if farther branches add types;
- branches six or more streets away give `0`, not their types.

The answers were checked against a multi-source BFS from all branches up
to distance 5, where a crossing's nearest types are the union of those of
its neighbours one layer closer, on every test and 40 random maps.

## Language notes

- All languages scan the same precomputed rings.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1121_bruteforce.cpp](1121_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(H·W·60) | AC | 0.031 s | 256 KB |
| [1121_bruteforce.go](1121_bruteforce.go) | Go 1.14 x64 | bruteforce | O(H·W·60) | AC | 0.031 s | 1376 KB |
| [1121_bruteforce.java](1121_bruteforce.java) | Java 1.8 | bruteforce | O(H·W·60) | AC | 0.109 s | 3664 KB |
| [1121_bruteforce.py](1121_bruteforce.py) | Python 3.12 x64 | bruteforce | O(H·W·60) | AC | 0.406 s | 2512 KB |
| [1121_bruteforce.rs](1121_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(H·W·60) | AC | 0.015 s | 628 KB |
