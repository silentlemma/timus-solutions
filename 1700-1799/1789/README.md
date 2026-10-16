# 1789. Searching for the Dodecahedron

[Timus 1789](https://acm.timus.ru/problem.aspx?space=1&num=1789) · difficulty 220 · constructive

Original problem by Mikhail Rubinchik, from the Ural Regional Team Programming Contest 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An artifact stands on one of n pedestals in a row, and copies stand on
the others. Each turn one pedestal is touched. If the artifact is there,
it is found; if not, the artifact moves to a neighbouring pedestal, left
or right, as it likes. Print a sequence of at most 1000 touches that
finds the artifact wherever it starts and however it moves.

## Input

n (2 ≤ n ≤ 100).

## Output

The number of touches, then the touched pedestals in order.

## Examples

### Example 1

Input:

```
3
```

Output:

```
2
2 2
```

## Solution

After every unsuccessful touch the artifact moves, so the parity of its pedestal
flips every turn. Touch 2, 3, …, n − 1. If at the first touch the
artifact stands on an even pedestal, it has the same parity as the
touched one at every turn and is never to its left, so it can never jump
over it and is caught at n − 1 at the latest. Otherwise, after these
n − 2 touches it has the parity of n − 1, so touching n − 1, n − 2, …,
2 sweeps it the same way from the right. For n > 2, pedestals 1 and n
are never touched: an artifact there has to step inwards. That gives
2(n − 2) touches. With n = 2 there is no middle at all, and touching
pedestal 1 twice works. `O(n)`.

In the example both passes are the single touch of pedestal 2: an
artifact on 2 is caught at once, and one on 1 or 3 has to move to 2.

Pitfalls:

- the sweep from the left alone misses the artifact that starts with
  the other parity, which simply slips past;
- for n > 2, touching the end pedestals is wasted, as the artifact
  cannot stay on them;
- n = 2 needs its own answer, since the formula gives no touches.

The checker follows the set of pedestals where the artifact may still
be and requires it to empty out. Every n from 2 to 100 passes, and a
full search over these sets for n up to 12 confirms that no shorter
sequence exists.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1789_constructive.cpp](1789_constructive.cpp) | G++ 13.2 x64 | constructive | O(n) | AC | 0.015 s | 400 KB |
| [1789_constructive.go](1789_constructive.go) | Go 1.14 x64 | constructive | O(n) | AC | 0.031 s | 1108 KB |
| [1789_constructive.java](1789_constructive.java) | Java 1.8 | constructive | O(n) | AC | 0.109 s | 1644 KB |
| [1789_constructive.py](1789_constructive.py) | Python 3.12 x64 | constructive | O(n) | AC | 0.062 s | 396 KB |
| [1789_constructive.rs](1789_constructive.rs) | Rust 1.75 x64 | constructive | O(n) | AC | 0.046 s | 204 KB |
