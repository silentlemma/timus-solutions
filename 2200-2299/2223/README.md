# 2223. How many calls an XOR-and-carry addition makes

[Timus 2223](https://acm.timus.ru/problem.aspx?space=1&num=2223) · difficulty 936 · bitmask

Original problem by Vadim Barinov, from the Ural Championship 2025.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The recursive function f(x, y) returns x when y = 0 and otherwise calls
f(x xor y, (x and y) << 1), on unbounded integers. For positive X and Y
given in binary with up to 10⁶ digits, print the number of calls made
by f(X, Y), or "infinity". The limits are 1 second and 256 MB.

## Input

X and Y in binary, 1 ≤ X, Y < 2^1000000.

## Output

The number of calls.

## Examples

### Example 1

Input:

```
1011
100
```

Output:

```
2
```

### Example 2

Input:

```
101
1
```

Output:

```
3
```

## Solution

This is addition by repeated carry propagation: x xor y is the sum
without carries and (x and y) << 1 is the carry. The sum x + y never
changes and both arguments stay nonnegative, so the recursion always
ends, and "infinity" never happens for these inputs.

A carry is born at a bit where both numbers have a 1, and each further
call moves it one bit up, as long as the bit above is a 1 in exactly
one of the numbers. It stops at the first bit that is equal in both:
two zeros absorb it, and two ones are where another carry is born. So
the number of rounds with a nonzero carry is the length of the longest
chain made of a common 1 followed by a run of differing bits above it,
counting the common bit.

One scan from the highest bit keeps the length of the current run of
differing bits; at every common 1 it closes a chain of that length plus
one, and every equal bit resets the run. The answer is the longest chain
plus 2, for the first call and for the last call with y = 0.

In the second example 101 + 1 has a common 1 in the lowest bit and the
bit above it is 0 in both, so the chain has length 1 and there are
3 calls.

This takes O(L) for L binary digits.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2223_bitmask.cpp](2223_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(L) | AC | 0.015 s | 3580 KB |
| [2223_bitmask.go](2223_bitmask.go) | Go 1.14 x64 | bitmask | O(L) | AC | 0.093 s | 8124 KB |
| [2223_bitmask.java](2223_bitmask.java) | Java 1.8 | bitmask | O(L) | AC | 0.203 s | 11272 KB |
| [2223_bitmask.py](2223_bitmask.py) | Python 3.12 x64 | bitmask | O(L) | AC | 0.171 s | 5580 KB |
| [2223_bitmask.rs](2223_bitmask.rs) | Rust 1.75 x64 | bitmask | O(L) | AC | 0.046 s | 2960 KB |
