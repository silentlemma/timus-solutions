# 1991. Count unused supplies and unmatched targets

[Timus 1991](https://acm.timus.ru/problem.aspx?space=1&num=1991) · difficulty 48 · implementation

Original problem by Denis Dublennykh, prepared by Egor Shchelkonogov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `n` independent groups, each with exactly `k` targets. Group
`i` receives `a_i` supplies, each usable once to remove one target in
that same group. Every use succeeds. Supplies cannot be transferred
between groups. After every group removes as many targets as possible,
count the supplies left unused and the targets left unmatched.

The bounds are `1≤n,k≤10000` and `0≤a_i≤100000`. Time limit: 1 second;
memory limit: 64 MB.

## Input

The first line contains `n k`. The next line contains the `n` supply counts.

## Output

Two integers: total unused supplies, followed by total remaining targets.

## Checking

Outputs are compared token by token.

## Examples

Input:

```
4 5
2 7 5 0
```

Output:

```
2 8
```

The groups leave `(unused,targets)` equal to `(0,3)`, `(2,0)`, `(0,0)`,
`(0,5)`. Their sum is `(2,8)`.

## Solution

A group can use no more than its `a_i` supplies and no more than its `k`
targets. Matching one supply to one target repeatedly achieves exactly
`b_i=min(a_i,k)` matches: after that, one of the two sides is empty.
Thus this group leaves `a_i−b_i=max(a_i−k,0)` supplies and
`k−b_i=max(k−a_i,0)` targets.

Keep two totals, initially zero. If `a_i>k`, add `a_i−k` to unused
supplies; otherwise add `k−a_i` to remaining targets. After processing
the first `j` groups, the totals equal their true leftover counts,
because the formula is correct for one group and groups do not exchange
supplies. This invariant proves the final totals after all `n` groups.

Do not merge all supplies before computing the result: one group may
have unused supplies while another still has targets. Equality `a_i=k`
contributes zero to both totals; `a_i=0` leaves all `k` targets. As a
check, `unused−remaining=Σa_i−nk`, but this identity alone does not
determine both outputs.

## Language notes

Time is `O(n)`, with `O(1)` auxiliary state for the two totals. C++, Go
and Java consume counts from a buffered stream. Python retains `O(n)`
parsed input values; Rust retains `I` input bytes, so their actual input
storage is `O(n)` and `O(I)` respectively. Python's slice is another
`O(n)` temporary and does not affect the time bound.

The largest unused total is `10000·(100000−1)=999990000`; the largest
remaining total is `10000²=100000000`. Both fit signed 32 bits, and
compiled versions use wider integer totals. Rust only subtracts after
comparing the operands, preventing unsigned underflow. Java's tokenizer
reads these small integer tokens exactly. There is no need for sorting,
redistribution or floating-point output.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1991_implementation.cpp](1991_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 448 KB |
| [1991_implementation.go](1991_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 1236 KB |
| [1991_implementation.java](1991_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.093 s | 496 KB |
| [1991_implementation.py](1991_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.093 s | 1380 KB |
| [1991_implementation.rs](1991_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.046 s | 480 KB |
