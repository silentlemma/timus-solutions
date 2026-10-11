# 1224. Turns of a robot that sweeps a rectangle in a spiral

[Timus 1224](https://acm.timus.ru/problem.aspx?space=1&num=1224) · difficulty 66 · math

Original problem from the Central Russia regional quarterfinal of the ACM ICPC 2002–2003, Rybinsk, October 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A robot starts at the top left cell of a field of `N` rows and `M`
columns, both up to `2³¹ − 1`, heading right, and covers every cell along
a clockwise spiral that winds towards the middle. Count its turns.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N` and `M`.

## Output

The number of turns.

## Examples

### Example 1

Input:

```
3 5
```

Output:

```
4
```

## Solution

The path alternates horizontal and vertical runs, starting with a
horizontal one, and turns once between two runs. Each horizontal run
uses up a row and each vertical run a column, as the spiral peels the
field from the outside.

If `N ≤ M`, the rows run out first, after `N` horizontal and `N − 1`
vertical runs, which is `2N − 1` runs and `2(N − 1)` turns. Otherwise the
columns run out first, after `M` runs of each kind: `2M` runs and
`2M − 1` turns. `O(1)`.

Pitfalls:

- a single row needs no turn at all, but a single column needs one,
  since the robot starts heading right;
- the answer reaches about `4.3·10⁹`, beyond 32-bit integers.

The formula was checked by simulating the robot on every field up to
14 × 14, and compared with a separately written solution on every test.

## Language notes

- All languages apply the same formula with 64-bit integers.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1224_math.cpp](1224_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB |
| [1224_math.go](1224_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1076 KB |
| [1224_math.java](1224_math.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 1564 KB |
| [1224_math.py](1224_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 372 KB |
| [1224_math.rs](1224_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 208 KB |
