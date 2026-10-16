# 1792. Hamming Code

[Timus 1792](https://acm.timus.ru/problem.aspx?space=1&num=1792) · difficulty 84 · implementation

Original problem by Sofia Tekhazheva (prepared by Olga Soboleva), from the Ural Regional School Programming Contest 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Four overlapping disks hold a bit each, and three petals, the regions
shared by three disks, hold the parity of the sum over the disks that
cover them. In the order of the figure in the statement, petal j lies
in every disk except disk j, and the fourth disk covers all three
petals. At most one of the seven bits was changed. Restore a valid
code.

## Input

Seven bits: the four disks, then the three petals.

## Output

The seven bits of a valid code that differs from the input in at most
one place.

## Examples

### Example 1

Input:

```
0 1 0 1 1 0 1
```

Output:

```
0 1 0 0 1 0 1
```

### Example 2

Input:

```
1 1 1 1 1 1 1
```

Output:

```
1 1 1 1 1 1 1
```

## Solution

Check the word as given: petal j must equal the sum of the disks other
than disk j, modulo 2. If it fails, try changing each of the seven bits
in turn and keep the first change that makes the word valid. Two valid
words always differ in at least three places, so the answer is unique.
`O(1)`.

In the first example all three petals are wrong, and only the fourth
disk lies under all of them; changing it from 1 to 0 makes the petals
1, 0, 1, as written.

Pitfalls:

- a wrong petal may be the changed bit itself, not a disk;
- the word may already be valid, and then it is printed unchanged.

Every one of the 128 possible inputs gives the same answer as an
independent accepted implementation.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1792_implementation.cpp](1792_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 400 KB |
| [1792_implementation.go](1792_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1168 KB |
| [1792_implementation.java](1792_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.156 s | 1600 KB |
| [1792_implementation.py](1792_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.109 s | 472 KB |
| [1792_implementation.rs](1792_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.015 s | 220 KB |
